# Generated by Django 2.1.5 on 2019-01-05 02:04

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Homme'), ('F', 'Femme')], help_text="le sexe influence le calcul de l'indice de masse grasse et du poids idéal", max_length=1, null=True, verbose_name='Sexe')),
                ('birth_date', models.DateField(blank=True, help_text="l'âge influence le calcul de l'indice de masse grasse et du métabolisme de base", null=True, verbose_name='date de naissance')),
                ('weight', models.FloatField(blank=True, help_text='(en kg)', null=True, verbose_name='poids actuel')),
                ('objective_weight', models.FloatField(blank=True, help_text='(en kg)', null=True, verbose_name='poids souhaité')),
                ('height', models.SmallIntegerField(blank=True, help_text='(en cm)', null=True, verbose_name='taille')),
                ('activity', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'sédentaire'), (2, 'légèrement actif'), (3, 'actif'), (4, 'très actif'), (5, 'extrêmement actif')], help_text="le niveau d'activité physique influence le calcul du métabolisme de base", null=True, verbose_name='activité')),
                ('objective', models.SmallIntegerField(blank=True, choices=[(-1, 'perdre du poids'), (0, 'maintenir le poids'), (1, 'prendre du poids')], help_text="l'objectif permet d'adapter la quantité des plats et de l'activité physique", null=True, verbose_name='objectif')),
                ('progress', models.FloatField(blank=True, choices=[(0.25, '0,25 kg / semaine'), (0.5, '0,50 kg / semaine'), (1.0, '1,00 kg / semaine')], help_text="la progression du poids est fonction de l'objectif et permet d'adapter les quantités", null=True, verbose_name='progression')),
                ('points', models.PositiveSmallIntegerField(default=0, help_text='points de fidélité accumulés', verbose_name='points')),
                ('balance', models.DecimalField(decimal_places=2, default=0, help_text='solde (eu euros) approvisionné sur le compte', max_digits=5, verbose_name='solde')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Standard'), (1, 'Argent'), (2, 'Or')], default=0, help_text='niveau de fidélité du compte', verbose_name='statut')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'profil',
                'verbose_name_plural': 'profils',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, help_text="date et heure de pratique de l'activité physique", verbose_name='date')),
                ('type', models.CharField(choices=[('001', 'Agriculture, mise en boules de foin, nettoyage de la grange'), ('002', 'Agriculture, pelleter les grains'), ('003', 'Agriculture, traite à la main'), ('004', "Aquabiking (vélo dans l'eau)"), ('005', 'Aquagym (aqua-aérobic)'), ('006', 'Aviron, position assise, allure lente'), ('007', 'Aviron, position assise, allure modérée'), ('008', 'Aviron, position assise, allure très vigoureuse'), ('009', 'Aviron, position assise, allure vigoureuse'), ('010', 'Aérobic, enseignement dans une classe'), ('011', 'Aérobic, faible impact'), ('012', 'Aérobic, fort impact'), ('013', 'Aérobic, général'), ('014', 'Badminton, en compétition'), ('015', 'Badminton, hors compétition'), ('016', 'Balle au prisonier'), ('017', 'Barman, serveur'), ('018', 'Baseball'), ('019', 'Basket-ball, arbitrage'), ('020', 'Basket-ball, en fauteuil roulant'), ('021', 'Basket-ball, en match'), ('022', 'Basket-ball, général'), ('023', 'Basket-ball, tirs aux paniers'), ('024', 'Billard'), ('025', 'Bobsleigh'), ('026', 'Bolo, jeu normal'), ('027', 'Bolo, mode compétition'), ('028', 'Bowling'), ('029', 'Boxe, entraînement (mode sparring partner)'), ('030', 'Boxe, frappant les sacs'), ('031', 'Boxe, sur le ring, général'), ('032', 'Broomball, ballon-balai, ballon sur glace'), ('033', 'Canoë-kayak, allure lente'), ('034', 'Canoë-kayak, allure modérée'), ('035', 'Canoë-kayak, en équipe, mode compétition'), ('036', 'Catch, lutte'), ('037', 'Chasse, général'), ('038', 'Club de remise en forme, exercices, général'), ('039', 'Conduire un camion (position assise)'), ('040', "Construction, à l'extérieur, remodelage"), ('041', 'Corde à sauter, allure lente'), ('042', 'Corde à sauter, allure modérée, général'), ('043', 'Corde à sauter, allure rapide'), ('044', "Course d'orientation"), ('045', 'Course à pied'), ('046', 'Course à pied, 10,8 km/h'), ('047', 'Course à pied, 11,25 km/h'), ('048', 'Course à pied, 12 km/h'), ('049', 'Course à pied, 13 km/h'), ('050', 'Course à pied, 13,8 km/h'), ('051', 'Course à pied, 14,5 km/h'), ('052', 'Course à pied, 16 km/h'), ('053', 'Course à pied, 17,5 km/h'), ('054', 'Course à pied, 8 km/h'), ('055', 'Course à pied, 9,5 km/h'), ('056', 'Course à pied, cross country'), ('057', 'Course à pied, en montant les escaliers'), ('058', 'Course à pied, général'), ('059', 'Course à pied, sur une piste, pratique en équipe'), ('060', 'Courses de chevaux, galopant'), ('061', 'Cricket'), ('062', 'Croquet'), ('063', 'Crosse'), ('064', 'Cuisson ou préparation des plats'), ('065', 'Curling'), ('066', 'Cyclisme, 19 à 22 km/h, allure modérée'), ('067', 'Cyclisme, 22 à 25 km/h, allure vigoureuse'), ('068', 'Cyclisme, 25 à 30 km/h, très rapide, en course'), ('069', 'Cyclisme, < 16 km/h, loisirs'), ('070', 'Cyclisme, > 32 km/h, courses'), ('071', 'Cyclisme, de 16 à 19 km/h, allure lente'), ('072', 'Cyclisme, VTT en montagne ou BMX'), ('073', "Cyclisme, vélo d'appartement, allure lente"), ('074', "Cyclisme, vélo d'appartement, allure modérée"), ('075', "Cyclisme, vélo d'appartement, allure très lente"), ('076', "Cyclisme, vélo d'appartement, allure très vigoureuse"), ('077', "Cyclisme, vélo d'appartement, allure vigoureuse"), ('078', "Cyclisme, vélo d'appartement, général"), ('079', 'Danse (aérobic, ballet ou moderne)'), ('080', 'Danse (salle de bal, lente)'), ('081', 'Danse (salle de bal, rapide)'), ('082', 'Danse de salon (en couple), lente'), ('083', 'Danse de salon (en couple), rapide'), ('084', 'Danse, général'), ('085', "Descendre l'escalier en marchant"), ('086', 'Dormir'), ('087', 'Déménager (déballant les cartons)'), ('088', "Déplacement d'objets ménagers en portant les objets"), ('089', "Déplacement d'objets ménagers, par escalier"), ('090', 'Déplacement de meubles, dans la maison'), ('091', 'Entraînement en circuit, général, peu de repos'), ('092', 'Equitation, général'), ('093', 'Equitation, marche'), ('094', 'Equitation, trot'), ('095', 'Escalade, varappe, ascension de rochers'), ('096', 'Escalade, varappe, descente en rappel'), ('097', 'Escrime'), ('098', 'Etirements, hatha yoga'), ('099', 'Etirements, léger'), ('100', 'Exercices corporels, à la maison, allure légère ou modérée'), ('101', 'Exercices corporels, à la maison, allure vigoureuse'), ('102', 'Extraction du charbon (de la mine)'), ('103', 'Faire la cuisine'), ('104', 'Faire la queue (debout)'), ('105', 'Faire les courses (avec un chariot)'), ('106', 'Fléchettes (mur ou pelouse)'), ('107', 'Footbag'), ('108', 'Football (exercices, course drapeaux, général)'), ('109', 'Football, mode compétition'), ('110', 'Football, occasionnel, général'), ('111', 'Foresterie'), ('112', 'Frisbee (mode rythmé)'), ('113', 'Frisbee, général'), ('114', 'Frisbee, ultimate'), ('115', 'Gainage (sur les mains)'), ('116', 'Golf (mini-série ou frapper au loin)'), ('117', 'Golf (tirant les clubs)'), ('118', 'Golf (transportant des clubs)'), ('119', 'Golf (utilisant le chariot)'), ('120', 'Golf, général'), ('121', 'Grattage, plâtrage, peinture, mettre du papier mural'), ('122', 'Gymnastique suédoise, maison, effort léger/modéré'), ('123', 'Gymnastique, général'), ('124', 'Haltérophilie, allure modérée'), ('125', 'Haltérophilie, allure vigoureuse'), ('126', 'Handball (jeu en équipe)'), ('127', 'Handball, général'), ('128', 'Hockey sur gazon'), ('129', 'Hockey sur glace'), ('130', 'Hors-bord'), ('131', 'Jardinage, général'), ('132', 'Jaï-alaï (pelote basque)'), ('133', 'Jeu de palet, de boulingrin'), ('134', "Jogging, dans l'eau (aquajogging)"), ('135', 'Jogging, général'), ('136', 'Jonglage'), ('137', 'Jouer un instrument tout en marchant (ex. : parade)'), ('138', 'Judo, jujitsu'), ('139', 'Karaté'), ('140', 'Kayak'), ('141', 'Kick Boxing'), ('142', 'Kickball'), ('143', 'Laver le chien'), ('144', 'Les Mills BodyAttack'), ('145', 'Les Mills BodyBalance/BodyFlow'), ('146', 'Les Mills BodyCombat'), ('147', 'Les Mills BodyPump'), ('148', 'Les Mills BodyStep'), ('149', 'Les Mills Grit'), ('150', 'Les Mills RPM'), ('151', "Lire (en s'asseyant)"), ('152', 'Luge'), ('153', 'Marche rapide (ex. : parade militaire)'), ('154', 'Marcher/Courir, jouant avec enfant, allure modérée'), ('155', 'Marcher/Courir, jouant avec enfant, allure vigoureuse'), ('156', 'Masseur (position debout)'), ('157', 'Maçonnerie'), ('158', 'Menuiserie, charpenterie, général'), ('159', 'Monocycle'), ('160', 'Moto-cross'), ('161', 'Motoneige'), ('162', 'Musculation'), ('163', 'Musique, batterie'), ('164', 'Musique, guitare, classique (assis)'), ('165', 'Musique, guitare, rock and roll (debout)'), ('166', 'Musique, piano, orgue, violon'), ('167', 'Musique, violoncelle, flûte, cor'), ('168', 'Natation sychronisée'), ('169', 'Natation, brasse papillon, général'), ('170', 'Natation, brasse, général'), ('171', 'Natation, dos, général'), ('172', 'Natation, laps, allure modérée'), ('173', 'Natation, laps, allure rapide'), ('174', 'Natation, papillon, général'), ('175', 'Natation, pour le loisir, général'), ('176', 'Natation, sur place, allure modérée'), ('177', 'Natation, sur place, allure rapide'), ('178', 'Nettoyage (voiture, fenêtres, etc.), lourd et vigoureux'), ('179', 'Nettoyage du garage, du trottoir'), ('180', 'Nettoyage du sol, utilisant mains et genoux'), ('181', 'Nettoyage, allure lente ou modéré'), ('182', 'Nettoyage, dans la maison, général'), ('183', 'Nettoyer les gouttières'), ('184', 'Officier de police'), ('185', 'Pansage de chevaux, intense'), ('186', 'Pansage de chevaux, lent'), ('187', 'Parachutisme'), ('188', 'Patinage sur glace, 14 km/h ou moins'), ('189', 'Patinage sur glace, allure rapide (> 14 km/h)'), ('190', 'Patinage sur glace, allure rapide (mode compétition)'), ('191', 'Patinage sur glace, général'), ('192', 'Patinage, roller'), ('193', 'Pelleter la neige, à la main'), ('194', 'Pilates'), ('195', 'Plongée (sous-marine, tremplin ou plate-forme)'), ('196', 'Plongée en apnée (snorkeling)'), ('197', 'Plongée sous-marine, général'), ('198', 'Polo'), ('199', 'Pompes, intense'), ('200', "Pompier en train d'éteindre une incendie"), ('201', 'Port de charges lourdes (comme des briques)'), ('202', "Porter entre 12 et 22 kilos en montant l'escalier"), ('203', "Porter entre 7 et 11 kilos en montant l'escalier"), ('204', 'Porter un sac à dos, général'), ('205', 'Poser ou enlever les tapis/carrelages du sol'), ('206', 'Poser un double-vitrage'), ('207', 'Pousser ou tirer une poussette avec enfant'), ('208', 'Pousser un fauteuil roulant'), ('209', 'Promenade à pied, 3 km/h, allure lente'), ('210', 'Promenade à pied, 5 km/h, allure modérée'), ('211', 'Promenade à pied, 5,5 km/h, en montée'), ('212', 'Promenade à pied, 6,5 km/h, allure très rapide'), ('213', 'Promenade à pied, en montant'), ('214', "Promenade à pied, piste d'herbe"), ('215', 'Promenade à pied, transportant 1 enfant ou 7 kgs'), ('216', "Promenade à pied, à l'aide de béquilles"), ('217', 'Promenader à pied, moins de 3 km/h, allure très lente'), ('218', 'Promener le chien'), ('219', 'Pédalo'), ('220', 'Pêche dans la rivière, dans les échassiers'), ('221', 'Pêche sur bateau, position assise'), ('222', 'Pêche sur la berge des rivières, position debout'), ('223', 'Pêche, général'), ('224', 'Pêche, sur la glace, position assise'), ('225', 'Racketball, jeu normal'), ('226', 'Racketball, mode compétition'), ('227', 'Rafting'), ('228', 'Rameur; allure lente'), ('229', 'Rameur; allure modérée'), ('230', 'Rameur; allure rapide'), ('231', 'Rameur; allure très rapide'), ('232', 'Randonnée pédestre, cross country'), ('233', 'Raquette (sur neige)'), ('234', 'Ratisser la pelouse'), ('235', 'Redressement assis, intense'), ('236', 'Regarder la TV'), ('237', 'Remontée mécanique, général'), ('238', "Repeindre la maison à l'extérieur"), ('239', 'Rugby'), ('240', 'Réparation automobile'), ('241', "S'asseoir dans une classe, travail de bureau"), ('242', "S'asseoir dans une réunion"), ('243', 'Saut à ski (montée au lieu du saut en emportant les skis)'), ('244', 'Sauts avec écart (Jumping Jack), intense'), ('245', 'Skateboard'), ('246', "Ski sur l'eau, ski nautique"), ('247', 'Ski sur neige, général'), ('248', 'Ski, en descente, allure lente'), ('249', 'Ski, en descente, allure modérée'), ('250', 'Ski, en descente, allure vigoureuse'), ('251', 'Ski, ski de fond, allure course'), ('252', 'Ski, ski de fond, allure lente'), ('253', 'Ski, ski de fond, allure modéré'), ('254', 'Ski, ski de fond, allure vigoureuse'), ('255', 'Ski, ski de fond, en montée'), ('256', 'Snowboard'), ('257', 'Softball, arbitrage'), ('258', 'Softball, lancer rapide ou lent'), ('259', 'Soins des enfants (bain, nourrir, etc.), position assise'), ('260', 'Soins des enfants (bain, nourrir, etc.), position debout'), ('261', 'Sortir la poubelle'), ('262', 'Soudage, ou travailler dans une salle de cinéma'), ('263', 'Spinning'), ('264', 'Squash'), ('265', 'Step, intense'), ('266', "Stepper, machine simulateur d'escalier"), ('267', 'Surf (couché ou debout sur la planche)'), ('268', 'Séance de jeu avec enfant, mouvements légers'), ('269', 'Tae Bo'), ('270', 'Tae Kwon Do'), ('271', 'Tai chi'), ('272', 'Tennis de table, ping-pong'), ('273', 'Tennis, double'), ('274', 'Tennis, général'), ('275', 'Tennis, simple'), ('276', "Tir à l'arc (en tant que sport et non en situation de chasse)"), ('277', 'Toilettage du cheval'), ('278', 'Tondre la pelouse, assis sur la tondeuse'), ('279', 'Tondre la pelouse, général'), ('280', 'Tractions (exercice de musculation), intense'), ('281', 'Trampoline'), ('282', 'Travail (léger) dans un bureau'), ('283', "Travailler sur l'ordinateur"), ('284', "Travaux d'électricité, plomberie"), ('285', 'Tâches ménagères, faire le ménage, général'), ('286', 'Voile, bateau, planche à voile, général'), ('287', 'Voile, en mode compétition'), ('288', 'Voile, planche à voile, général'), ('289', "Volley-ball dans l'eau"), ('290', 'Volley-ball, hors compétition'), ('291', 'Volley-ball, mode compétition, dans un gymnase'), ('292', 'Volley-ball, à la plage'), ('293', 'Vélo elliptique (allure modérée)'), ('294', 'Vélo elliptique (allure vigoureuse)'), ('295', 'Wallyball, général'), ('296', 'Water polo'), ('297', 'Wii baseball'), ('298', 'Wii bowling'), ('299', 'Wii boxe'), ('300', 'Wii golf'), ('301', 'Wii tennis'), ('302', 'Zumba'), ('999', 'Autre')], help_text="type d'activité physique pratique, influence le calcul de l'énergie dépensée", max_length=3, verbose_name='type')),
                ('duration', models.DurationField(help_text="durée de l'activité physique pratique au format HH:MM:SS", verbose_name='durée')),
                ('weight', models.FloatField(blank=True, help_text="poids mesuré au moment de la pratique de l'activité physique (repris depuis le profil par défaut)", null=True, verbose_name='poids')),
                ('energy', models.FloatField(blank=True, help_text="energie dépensée lors de l'activité physique, calculé si non rempli", null=True, verbose_name='énergie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'activité physique',
                'verbose_name_plural': 'activités physiques',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, help_text='date et heure du message', verbose_name='date')),
                ('is_read', models.BooleanField(default=False, help_text='message lu par le destinataire', verbose_name='lu')),
                ('from_user', models.ForeignKey(help_text='utilisateur émetteur du message', on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL, verbose_name='expediteur')),
                ('to_user', models.ForeignKey(help_text='utilisateur récepteur du message', on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL, verbose_name='destinataire')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('C', 'coach'), ('S', 'élève'), ('F', 'ami')], help_text='type de relation', max_length=1, verbose_name='type')),
                ('date', models.DateTimeField(auto_now=True, help_text='date et heure de la relation', verbose_name='date')),
                ('valid', models.BooleanField(default=False, help_text="relation validée par l'utilisateur destinataire", verbose_name='validée')),
                ('from_user', models.ForeignKey(help_text='utilisateur émetteur', on_delete=django.db.models.deletion.CASCADE, related_name='source', to=settings.AUTH_USER_MODEL, verbose_name='source')),
                ('to_user', models.ForeignKey(help_text='utilisateur destinataire', on_delete=django.db.models.deletion.CASCADE, related_name='target', to=settings.AUTH_USER_MODEL, verbose_name='cible')),
            ],
            options={
                'verbose_name': 'relation',
                'verbose_name_plural': 'relations',
            },
        ),
        migrations.CreateModel(
            name='WeightHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, help_text='date de la mesure du poids.', verbose_name='date')),
                ('weight', models.FloatField(help_text='poids mesuré (en kg)', verbose_name='poids')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weight_history', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'historique de poids',
                'verbose_name_plural': 'historiques de poids',
            },
        ),
        migrations.AlterUniqueTogether(
            name='weighthistory',
            unique_together={('user', 'date')},
        ),
    ]
