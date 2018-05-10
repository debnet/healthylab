# coding: utf-8
from common.models import CommonModel
from datetime import date
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _


class Profile(AbstractUser):
    """
    Profil
    """
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = (
        (MALE, _("Homme")),
        (FEMALE, _("Femme")),
    )
    ACTIVITIES = (
        (1, _("sédentaire")),
        (2, _("légèrement actif")),
        (3, _("actif")),
        (4, _("très actif")),
        (5, _("extrêmement actif")),
    )
    ACTIVITIES_DESCRIPTIONS = (
        (1, _("aucun exercice quotidien ou presque")),
        (2, _("vous faîtes parfois des exercices physiques 1 à 3 fois par semaine "
              "(ménage, jardinage, bricolage, marche)")),
        (3, _("vous faîtes régulièrement des exercices physiques : 3 à 5 fois par semaine "
              "(en plus d'une légère activité, vous faîtes 2 à 4 heures de sport par semaine)")),
        (4, _("vous faîtes quotidiennement du sport ou des exercices physiques soutenus")),
        (5, _("votre travail est extrêmement physique ou bien vous vous considérez comme un sportif (de haut niveau)")),
    )
    OBJECTIVES = (
        (-1, _("perdre du poids")),
        (+0, _("maintien du poids")),
        (+1, _("prendre du poids")),
    )
    PROGRESSES = (
        (0.25, _("0,25 kg / semaine")),
        (0.50, _("0,50 kg / semaine")),
        (1.00, _("1,00 kg / semaine")),
    )
    STATUS = (
        (0, _("Basic")),
        (1, _("Silver")),
        (2, _("Gold")),
    )
    BODY_MASS = (
        (0.0, 16.5, _("dénutrition")),
        (16.5, 18.5, _("maigreur")),
        (18.5, 25.0, _("corpulence normale")),
        (25.0, 30.0, _("surpoids")),
        (30.0, 35.0, _("obésité modérée")),
        (35.0, 40.0, _("obésité sévère")),
        (40.0, 100.0, _("obésité morbide")),
    )
    BODY_FAT = (
        (0, 15, _("trop maigre")),
        (15, 20, _("normal")),
        (20, 100, _("trop de graisse")),
    )
    IDEAL_WEIGHT_FACTOR = {MALE: 4, FEMALE: 2.5}
    BODY_FAT_FACTOR = {MALE: 16.2, FEMALE: 5.4}
    BASAL_METABOLIC_RATE_FACTOR = {
        MALE: (10.0, 6.25, 5.0, 5.0),
        FEMALE: (0.0, 6.25, 5.0, -161.0)}
    BASAL_METABOLIC_RATE_BY_ACTIVITY_FACTOR = {
        1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}

    gender = models.CharField(
        max_length=1, blank=True, null=True, choices=GENDERS,
        verbose_name=_("Sexe"))
    birth_date = models.DateField(
        blank=True, null=True,
        verbose_name=_("date de naissance"))
    weight = models.FloatField(
        blank=True, null=True,
        verbose_name=_("poids actuel"))
    objective_weight = models.FloatField(
        blank=True, null=True,
        verbose_name=_("poids souhaité"))
    height = models.SmallIntegerField(
        blank=True, null=True,
        verbose_name=_("taille"))
    activity = models.PositiveSmallIntegerField(
        blank=True, null=True, choices=ACTIVITIES,
        verbose_name=_("activité"))
    objective = models.SmallIntegerField(
        blank=True, null=True, choices=OBJECTIVES,
        verbose_name=_("objectif"))
    progress = models.FloatField(
        blank=True, null=True, choices=PROGRESSES,
        verbose_name=_("progression"))
    points = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_("points"))
    balance = models.DecimalField(
        default=0, max_digits=5, decimal_places=2,
        verbose_name=_("solde"))
    status = models.PositiveSmallIntegerField(
        default=0, choices=STATUS,
        verbose_name=_("statut"))

    @property
    def age(self):
        """
        Âge
        """
        if not self.birth_date:
            return None
        today, birth_date = date.today(), self.birth_date
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    @property
    def ideal_weight(self):
        """
        Poids idéal selon la formule de Lorentz
        """
        if self.gender and self.height:
            factor = self.IDEAL_WEIGHT_FACTOR.get(self.gender)
            return round(self.height - 100 - ((self.height - 150) / factor), 1)
        return None

    @property
    def body_mass_index(self):
        """
        Indice de masse corporelle (IMC ou BMI)
        """
        if self.height and self.weight:
            return round(self.weight / ((self.height / 100) ** 2), 2)
        return None

    @property
    def body_mass_label(self):
        """
        Libellé de l'indice de masse corporelle
        """
        bmi = self.body_mass_index
        if not bmi:
            return None
        for mini, maxi, label in self.BODY_MASS:
            if mini <= bmi < maxi:
                return label
        return None

    @property
    def body_fat_percentage(self):
        """
        Indice de masse grasse
        """
        bmi = self.body_mass_index
        if self.gender and self.birth_date and bmi:
            factor = self.BODY_FAT_FACTOR.get(self.gender)
            return round(1.2 * bmi + 0.23 * self.age - factor, 2)
        return None

    @property
    def body_fat_label(self):
        """
        Libellé de l'indice de masse grasse
        """
        bfp = self.body_fat_percentage
        if bfp:
            factor = +10 if self.gender == self.FEMALE else 0
            for mini, maxi, label in self.BODY_FAT:
                if mini + factor <= bfp < maxi + factor:
                    return label
        return None

    @property
    def basal_metabolic_rate(self):
        """
        Métabolisme de base
        """
        if self.age and self.weight and self.height and self.gender:
            f1, f2, f3, f4 = self.BASAL_METABOLIC_RATE_FACTOR.get(self.gender)
            bmr = round(f1 * self.weight + f2 * self.height - f3 * self.age + f4, 2)
            if self.activity:
                bmr *= self.BASAL_METABOLIC_RATE_BY_ACTIVITY_FACTOR.get(self.activity)
            return round(bmr, 0)
        return None

    class Meta:
        verbose_name = _("profil")
        verbose_name_plural = _("profils")


class WeightHistory(CommonModel):
    """
    Historique du poids
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='histories',
        verbose_name=_("utilisateur"))
    date = models.DateField(
        auto_now_add=True,
        verbose_name=_("date"))
    weight = models.FloatField(
        verbose_name=_("poids"))

    class Meta:
        verbose_name = _("historique de poids")
        verbose_name_plural = _("historiques de poids")
        unique_together = ('user', 'date')


@receiver(post_save, sender=Profile)
def create_activity(instance, **kwargs):
    if instance.weight:
        WeightHistory.objects.update_or_create(
            user=instance, date=date.today(),
            defaults=dict(weight=instance.weight))


class Activity(CommonModel):
    """
    Activité physique
    """
    ACTIVITIES = (
        ('001', _("Agriculture, mise en boules de foin, nettoyage de la grange"), 10.17),
        ('002', _("Agriculture, pelleter les grains"), 6.99),
        ('003', _("Agriculture, traite à la main"), 3.81),
        ('004', _("Aquabiking (vélo dans l'eau)"), 10.65),
        ('005', _("Aquagym (aqua-aérobic)"), 5.08),
        ('006', _("Aviron, position assise, allure lente"), 8.9),
        ('007', _("Aviron, position assise, allure modérée"), 10.81),
        ('008', _("Aviron, position assise, allure très vigoureuse"), 15.25),
        ('009', _("Aviron, position assise, allure vigoureuse"), 12.08),
        ('010', _("Aérobic, enseignement dans une classe"), 7.63),
        ('011', _("Aérobic, faible impact"), 6.36),
        ('012', _("Aérobic, fort impact"), 8.9),
        ('013', _("Aérobic, général"), 8.26),
        ('014', _("Badminton, en compétition"), 8.9),
        ('015', _("Badminton, hors compétition"), 5.73),
        ('016', _("Balle au prisonier"), 6.36),
        ('017', _("Barman, serveur"), 3.18),
        ('018', _("Baseball"), 6.36),
        ('019', _("Basket-ball, arbitrage"), 8.9),
        ('020', _("Basket-ball, en fauteuil roulant"), 8.27),
        ('021', _("Basket-ball, en match"), 10.17),
        ('022', _("Basket-ball, général"), 7.63),
        ('023', _("Basket-ball, tirs aux paniers"), 5.73),
        ('024', _("Billard"), 3.18),
        ('025', _("Bobsleigh"), 8.9),
        ('026', _("Bolo, jeu normal"), 7.62),
        ('027', _("Bolo, mode compétition"), 12.71),
        ('028', _("Bowling"), 3.81),
        ('029', _("Boxe, entraînement (mode sparring partner)"), 11.44),
        ('030', _("Boxe, frappant les sacs"), 7.63),
        ('031', _("Boxe, sur le ring, général"), 15.25),
        ('032', _("Broomball, ballon-balai, ballon sur glace"), 8.9),
        ('033', _("Canoë-kayak, allure lente"), 3.81),
        ('034', _("Canoë-kayak, allure modérée"), 8.9),
        ('035', _("Canoë-kayak, en équipe, mode compétition"), 15.25),
        ('036', _("Catch, lutte"), 7.62),
        ('037', _("Chasse, général"), 6.36),
        ('038', _("Club de remise en forme, exercices, général"), 6.99),
        ('039', _("Conduire un camion (position assise)"), 2.54),
        ('040', _("Construction, à l'extérieur, remodelage"), 6.99),
        ('041', _("Corde à sauter, allure lente"), 10.17),
        ('042', _("Corde à sauter, allure modérée, général"), 12.72),
        ('043', _("Corde à sauter, allure rapide"), 15.25),
        ('044', _("Course d'orientation"), 11.43),
        ('045', _("Course à pied"), 8.27),
        ('046', _("Course à pied, 10,8 km/h"), 13.98),
        ('047', _("Course à pied, 11,25 km/h"), 14.62),
        ('048', _("Course à pied, 12 km/h"), 15.9),
        ('049', _("Course à pied, 13 km/h"), 17.17),
        ('050', _("Course à pied, 13,8 km/h"), 17.8),
        ('051', _("Course à pied, 14,5 km/h"), 19.07),
        ('052', _("Course à pied, 16 km/h"), 20.34),
        ('053', _("Course à pied, 17,5 km/h"), 22.89),
        ('054', _("Course à pied, 8 km/h"), 10.17),
        ('055', _("Course à pied, 9,5 km/h"), 12.72),
        ('056', _("Course à pied, cross country"), 11.44),
        ('057', _("Course à pied, en montant les escaliers"), 19.07),
        ('058', _("Course à pied, général"), 10.17),
        ('059', _("Course à pied, sur une piste, pratique en équipe"), 12.72),
        ('060', _("Courses de chevaux, galopant"), 10.17),
        ('061', _("Cricket"), 6.36),
        ('062', _("Croquet"), 3.18),
        ('063', _("Crosse"), 10.17),
        ('064', _("Cuisson ou préparation des plats"), 3.18),
        ('065', _("Curling"), 5.08),
        ('066', _("Cyclisme, 19 à 22 km/h, allure modérée"), 10.17),
        ('067', _("Cyclisme, 22 à 25 km/h, allure vigoureuse"), 12.72),
        ('068', _("Cyclisme, 25 à 30 km/h, très rapide, en course"), 15.25),
        ('069', _("Cyclisme, < 16 km/h, loisirs"), 5.08),
        ('070', _("Cyclisme, > 32 km/h, courses"), 20.34),
        ('071', _("Cyclisme, de 16 à 19 km/h, allure lente"), 7.63),
        ('072', _("Cyclisme, VTT en montagne ou BMX"), 10.81),
        ('073', _("Cyclisme, vélo d'appartement, allure lente"), 6.99),
        ('074', _("Cyclisme, vélo d'appartement, allure modérée"), 8.9),
        ('075', _("Cyclisme, vélo d'appartement, allure très lente"), 3.81),
        ('076', _("Cyclisme, vélo d'appartement, allure très vigoureuse"), 15.9),
        ('077', _("Cyclisme, vélo d'appartement, allure vigoureuse"), 13.35),
        ('078', _("Cyclisme, vélo d'appartement, général"), 6.36),
        ('079', _("Danse (aérobic, ballet ou moderne)"), 7.63),
        ('080', _("Danse (salle de bal, lente)"), 3.81),
        ('081', _("Danse (salle de bal, rapide)"), 6.99),
        ('082', _("Danse de salon (en couple), lente"), 3.81),
        ('083', _("Danse de salon (en couple), rapide"), 6.99),
        ('084', _("Danse, général"), 5.73),
        ('085', _("Descendre l'escalier en marchant"), 3.81),
        ('086', _("Dormir"), 0.79),
        ('087', _("Déménager (déballant les cartons)"), 4.45),
        ('088', _("Déplacement d'objets ménagers en portant les objets"), 8.9),
        ('089', _("Déplacement d'objets ménagers, par escalier"), 11.44),
        ('090', _("Déplacement de meubles, dans la maison"), 7.63),
        ('091', _("Entraînement en circuit, général, peu de repos"), 10.17),
        ('092', _("Equitation, général"), 5.08),
        ('093', _("Equitation, marche"), 3.18),
        ('094', _("Equitation, trot"), 8.27),
        ('095', _("Escalade, varappe, ascension de rochers"), 13.98),
        ('096', _("Escalade, varappe, descente en rappel"), 10.17),
        ('097', _("Escrime"), 7.63),
        ('098', _("Etirements, hatha yoga"), 5.08),
        ('099', _("Etirements, léger"), 3.18),
        ('100', _("Exercices corporels, à la maison, allure légère ou modérée"), 5.73),
        ('101', _("Exercices corporels, à la maison, allure vigoureuse"), 10.17),
        ('102', _("Extraction du charbon (de la mine)"), 7.62),
        ('103', _("Faire la cuisine"), 3.18),
        ('104', _("Faire la queue (debout)"), 1.61),
        ('105', _("Faire les courses (avec un chariot)"), 4.45),
        ('106', _("Fléchettes (mur ou pelouse)"), 3.18),
        ('107', _("Footbag"), 5.08),
        ('108', _("Football (exercices, course drapeaux, général)"), 10.17),
        ('109', _("Football, mode compétition"), 12.72),
        ('110', _("Football, occasionnel, général"), 8.9),
        ('111', _("Foresterie"), 10.17),
        ('112', _("Frisbee (mode rythmé)"), 4.45),
        ('113', _("Frisbee, général"), 3.81),
        ('114', _("Frisbee, ultimate"), 10.16),
        ('115', _("Gainage (sur les mains)"), 8.68),
        ('116', _("Golf (mini-série ou frapper au loin)"), 3.81),
        ('117', _("Golf (tirant les clubs)"), 6.36),
        ('118', _("Golf (transportant des clubs)"), 6.99),
        ('119', _("Golf (utilisant le chariot)"), 4.45),
        ('120', _("Golf, général"), 5.08),
        ('121', _("Grattage, plâtrage, peinture, mettre du papier mural"), 5.73),
        ('122', _("Gymnastique suédoise, maison, effort léger/modéré"), 4.45),
        ('123', _("Gymnastique, général"), 5.08),
        ('124', _("Haltérophilie, allure modérée"), 3.81),
        ('125', _("Haltérophilie, allure vigoureuse"), 7.63),
        ('126', _("Handball (jeu en équipe)"), 10.17),
        ('127', _("Handball, général"), 15.25),
        ('128', _("Hockey sur gazon"), 10.17),
        ('129', _("Hockey sur glace"), 10.17),
        ('130', _("Hors-bord"), 3.18),
        ('131', _("Jardinage, général"), 6.36),
        ('132', _("Jaï-alaï (pelote basque)"), 15.24),
        ('133', _("Jeu de palet, de boulingrin"), 3.81),
        ('134', _("Jogging, dans l'eau (aquajogging)"), 10.17),
        ('135', _("Jogging, général"), 8.9),
        ('136', _("Jonglage"), 5.08),
        ('137', _("Jouer un instrument tout en marchant (ex. : parade)"), 5.08),
        ('138', _("Judo, jujitsu"), 12.72),
        ('139', _("Karaté"), 12.72),
        ('140', _("Kayak"), 6.36),
        ('141', _("Kick Boxing"), 12.72),
        ('142', _("Kickball"), 8.89),
        ('143', _("Laver le chien"), 4.45),
        ('144', _("Les Mills BodyAttack"), 10.05),
        ('145', _("Les Mills BodyBalance/BodyFlow"), 4.9),
        ('146', _("Les Mills BodyCombat"), 10.18),
        ('147', _("Les Mills BodyPump"), 6.88),
        ('148', _("Les Mills BodyStep"), 10.12),
        ('149', _("Les Mills Grit"), 11.62),
        ('150', _("Les Mills RPM"), 9.51),
        ('151', _("Lire (en s'asseyant)"), 1.43),
        ('152', _("Luge"), 8.9),
        ('153', _("Marche rapide (ex. : parade militaire)"), 8.27),
        ('154', _("Marcher/Courir, jouant avec enfant, allure modérée"), 5.08),
        ('155', _("Marcher/Courir, jouant avec enfant, allure vigoureuse"), 6.36),
        ('156', _("Masseur (position debout)"), 5.09),
        ('157', _("Maçonnerie"), 8.9),
        ('158', _("Menuiserie, charpenterie, général"), 4.45),
        ('159', _("Monocycle"), 6.36),
        ('160', _("Moto-cross"), 5.08),
        ('161', _("Motoneige"), 4.45),
        ('162', _("Musculation"), 7.63),
        ('163', _("Musique, batterie"), 5.08),
        ('164', _("Musique, guitare, classique (assis)"), 2.55),
        ('165', _("Musique, guitare, rock and roll (debout)"), 3.81),
        ('166', _("Musique, piano, orgue, violon"), 3.18),
        ('167', _("Musique, violoncelle, flûte, cor"), 2.55),
        ('168', _("Natation sychronisée"), 10.17),
        ('169', _("Natation, brasse papillon, général"), 13.97),
        ('170', _("Natation, brasse, général"), 12.72),
        ('171', _("Natation, dos, général"), 10.17),
        ('172', _("Natation, laps, allure modérée"), 10.17),
        ('173', _("Natation, laps, allure rapide"), 12.72),
        ('174', _("Natation, papillon, général"), 13.98),
        ('175', _("Natation, pour le loisir, général"), 7.63),
        ('176', _("Natation, sur place, allure modérée"), 5.08),
        ('177', _("Natation, sur place, allure rapide"), 12.72),
        ('178', _("Nettoyage (voiture, fenêtres, etc.), lourd et vigoureux"), 5.73),
        ('179', _("Nettoyage du garage, du trottoir"), 5.08),
        ('180', _("Nettoyage du sol, utilisant mains et genoux"), 6.99),
        ('181', _("Nettoyage, allure lente ou modéré"), 3.18),
        ('182', _("Nettoyage, dans la maison, général"), 4.45),
        ('183', _("Nettoyer les gouttières"), 6.35),
        ('184', _("Officier de police"), 3.18),
        ('185', _("Pansage de chevaux, intense"), 7.63),
        ('186', _("Pansage de chevaux, lent"), 4.45),
        ('187', _("Parachutisme"), 3.81),
        ('188', _("Patinage sur glace, 14 km/h ou moins"), 6.99),
        ('189', _("Patinage sur glace, allure rapide (> 14 km/h)"), 11.44),
        ('190', _("Patinage sur glace, allure rapide (mode compétition)"), 19.07),
        ('191', _("Patinage sur glace, général"), 8.9),
        ('192', _("Patinage, roller"), 8.9),
        ('193', _("Pelleter la neige, à la main"), 7.63),
        ('194', _("Pilates"), 3.18),
        ('195', _("Plongée (sous-marine, tremplin ou plate-forme)"), 3.81),
        ('196', _("Plongée en apnée (snorkeling)"), 6.36),
        ('197', _("Plongée sous-marine, général"), 8.9),
        ('198', _("Polo"), 10.17),
        ('199', _("Pompes, intense"), 10.03),
        ('200', _("Pompier en train d'éteindre une incendie"), 15.25),
        ('201', _("Port de charges lourdes (comme des briques)"), 10.17),
        ('202', _("Porter entre 12 et 22 kilos en montant l'escalier"), 10.17),
        ('203', _("Porter entre 7 et 11 kilos en montant l'escalier"), 7.62),
        ('204', _("Porter un sac à dos, général"), 8.9),
        ('205', _("Poser ou enlever les tapis/carrelages du sol"), 5.72),
        ('206', _("Poser un double-vitrage"), 6.35),
        ('207', _("Pousser ou tirer une poussette avec enfant"), 3.18),
        ('208', _("Pousser un fauteuil roulant"), 5.08),
        ('209', _("Promenade à pied, 3 km/h, allure lente"), 3.18),
        ('210', _("Promenade à pied, 5 km/h, allure modérée"), 4.45),
        ('211', _("Promenade à pied, 5,5 km/h, en montée"), 5.08),
        ('212', _("Promenade à pied, 6,5 km/h, allure très rapide"), 7.63),
        ('213', _("Promenade à pied, en montant"), 10.17),
        ('214', _("Promenade à pied, piste d'herbe"), 6.36),
        ('215', _("Promenade à pied, transportant 1 enfant ou 7 kgs"), 4.45),
        ('216', _("Promenade à pied, à l'aide de béquilles"), 5.08),
        ('217', _("Promenader à pied, moins de 3 km/h, allure très lente"), 2.54),
        ('218', _("Promener le chien"), 3.81),
        ('219', _("Pédalo"), 5.08),
        ('220', _("Pêche dans la rivière, dans les échassiers"), 7.63),
        ('221', _("Pêche sur bateau, position assise"), 3.18),
        ('222', _("Pêche sur la berge des rivières, position debout"), 4.45),
        ('223', _("Pêche, général"), 5.08),
        ('224', _("Pêche, sur la glace, position assise"), 2.55),
        ('225', _("Racketball, jeu normal"), 8.9),
        ('226', _("Racketball, mode compétition"), 12.71),
        ('227', _("Rafting"), 6.36),
        ('228', _("Rameur; allure lente"), 4.45),
        ('229', _("Rameur; allure modérée"), 8.9),
        ('230', _("Rameur; allure rapide"), 10.81),
        ('231', _("Rameur; allure très rapide"), 15.25),
        ('232', _("Randonnée pédestre, cross country"), 7.63),
        ('233', _("Raquette (sur neige)"), 10.17),
        ('234', _("Ratisser la pelouse"), 5.08),
        ('235', _("Redressement assis, intense"), 10.03),
        ('236', _("Regarder la TV"), 0.96),
        ('237', _("Remontée mécanique, général"), 8.89),
        ('238', _("Repeindre la maison à l'extérieur"), 6.35),
        ('239', _("Rugby"), 12.72),
        ('240', _("Réparation automobile"), 3.81),
        ('241', _("S'asseoir dans une classe, travail de bureau"), 2.23),
        ('242', _("S'asseoir dans une réunion"), 2.06),
        ('243', _("Saut à ski (montée au lieu du saut en emportant les skis)"), 8.9),
        ('244', _("Sauts avec écart (Jumping Jack), intense"), 10.54),
        ('245', _("Skateboard"), 6.36),
        ('246', _("Ski sur l'eau, ski nautique"), 7.63),
        ('247', _("Ski sur neige, général"), 8.9),
        ('248', _("Ski, en descente, allure lente"), 6.36),
        ('249', _("Ski, en descente, allure modérée"), 7.63),
        ('250', _("Ski, en descente, allure vigoureuse"), 10.17),
        ('251', _("Ski, ski de fond, allure course"), 17.8),
        ('252', _("Ski, ski de fond, allure lente"), 8.9),
        ('253', _("Ski, ski de fond, allure modéré"), 10.17),
        ('254', _("Ski, ski de fond, allure vigoureuse"), 11.44),
        ('255', _("Ski, ski de fond, en montée"), 20.98),
        ('256', _("Snowboard"), 7.87),
        ('257', _("Softball, arbitrage"), 5.08),
        ('258', _("Softball, lancer rapide ou lent"), 6.36),
        ('259', _("Soins des enfants (bain, nourrir, etc.), position assise"), 3.81),
        ('260', _("Soins des enfants (bain, nourrir, etc.), position debout"), 4.45),
        ('261', _("Sortir la poubelle"), 3.81),
        ('262', _("Soudage, ou travailler dans une salle de cinéma"), 3.82),
        ('263', _("Spinning"), 8.89),
        ('264', _("Squash"), 15.25),
        ('265', _("Step, intense"), 18.54),
        ('266', _("Stepper, machine simulateur d'escalier"), 11.43),
        ('267', _("Surf (couché ou debout sur la planche)"), 3.81),
        ('268', _("Séance de jeu avec enfant, mouvements légers"), 3.18),
        ('269', _("Tae Bo"), 12.83),
        ('270', _("Tae Kwon Do"), 12.72),
        ('271', _("Tai chi"), 5.08),
        ('272', _("Tennis de table, ping-pong"), 5.08),
        ('273', _("Tennis, double"), 7.63),
        ('274', _("Tennis, général"), 8.9),
        ('275', _("Tennis, simple"), 10.17),
        ('276', _("Tir à l'arc (en tant que sport et non en situation de chasse)"), 4.45),
        ('277', _("Toilettage du cheval"), 7.62),
        ('278', _("Tondre la pelouse, assis sur la tondeuse"), 3.18),
        ('279', _("Tondre la pelouse, général"), 6.99),
        ('280', _("Tractions (exercice de musculation), intense"), 9.65),
        ('281', _("Trampoline"), 4.45),
        ('282', _("Travail (léger) dans un bureau"), 1.92),
        ('283', _("Travailler sur l'ordinateur"), 1.74),
        ('284', _("Travaux d'électricité, plomberie"), 3.82),
        ('285', _("Tâches ménagères, faire le ménage, général"), 4.45),
        ('286', _("Voile, bateau, planche à voile, général"), 3.81),
        ('287', _("Voile, en mode compétition"), 6.36),
        ('288', _("Voile, planche à voile, général"), 3.81),
        ('289', _("Volley-ball dans l'eau"), 3.81),
        ('290', _("Volley-ball, hors compétition"), 3.81),
        ('291', _("Volley-ball, mode compétition, dans un gymnase"), 5.08),
        ('292', _("Volley-ball, à la plage"), 10.17),
        ('293', _("Vélo elliptique (allure modérée)"), 8.67),
        ('294', _("Vélo elliptique (allure vigoureuse)"), 10.27),
        ('295', _("Wallyball, général"), 8.9),
        ('296', _("Water polo"), 12.72),
        ('297', _("Wii baseball"), 4.45),
        ('298', _("Wii bowling"), 3.69),
        ('299', _("Wii boxe"), 6.86),
        ('300', _("Wii golf"), 3.18),
        ('301', _("Wii tennis"), 5.08),
        ('302', _("Zumba"), 11.17),
        ('999', _("Autre"), 0.00),
    )
    TYPES = tuple((a, b) for a, b, c in ACTIVITIES)
    MET = {a: c for a, b, c in ACTIVITIES}

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activities',
        verbose_name=_("utilisateur"))
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("date"))
    type = models.CharField(
        max_length=3, choices=TYPES,
        verbose_name=_("type"))
    duration = models.DurationField(
        verbose_name=_("durée"))
    weight = models.FloatField(
        blank=True, null=True,
        verbose_name=_("poids"))
    energy = models.FloatField(
        blank=True, null=True,
        verbose_name=_("énergie"))

    @property
    def calculated_energy(self):
        weight = self.weight or self.user.weight
        if weight:
            met = self.MET.get(self.type)
            duration = self.duration.total_seconds()
            return (met * 3.5 * weight * duration) / 12000.0
        return None

    def save(self, *args, **kwargs):
        if not self.energy:
            if not self.weight:
                self.weight = self.user.weight
            self.energy = self.calculated_energy or None
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("activité physique")
        verbose_name_plural = _("activités physiques")


# Liste de tous les modèles connus
MODELS = (WeightHistory, Activity,)
