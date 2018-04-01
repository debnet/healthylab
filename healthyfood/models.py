# coding: utf-8
from common.models import CommonModel, Entity
from datetime import date
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FoodGroup(CommonModel):
    """
    Groupe d'aliments
    """
    LEVELS = (
        (1, _("groupe")),
        (2, _("sous-groupe")),
        (3, _("sous-sous-groupe")),
    )

    code = models.CharField(
        max_length=6, primary_key=True,
        verbose_name=_("code"))
    name = models.CharField(
        max_length=1000,
        verbose_name=_("nom"))
    level = models.PositiveSmallIntegerField(
        default=1, choices=LEVELS,
        verbose_name=_("niveau"))
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name='subgroups',
        verbose_name=_("parent"))

    class Meta:
        verbose_name = _("groupe d'aliments")
        verbose_name_plural = _("groupe d'aliments")


class Food(CommonModel):
    """
    Aliment
    """
    code = models.SmallIntegerField(
        primary_key=True,
        verbose_name=_("code"))
    name = models.CharField(
        max_length=1000,
        verbose_name=_("nom"))
    group = models.ForeignKey(
        'FoodGroup', on_delete=models.CASCADE, related_name='foods',
        verbose_name=_("groupe"))
    energy_eu = models.FloatField(
        default=0.0,
        verbose_name=_("énergie (UE)"),
        help_text=_("énergie selon le réglement UE N°1169/2001 (kcal/100g)"))
    energy_kj = models.FloatField(
        default=0.0,
        verbose_name=_("énergie (Jones)"),
        help_text=_("énergie N x facteur Jones avec fibres (kJ/100g)"))
    energy_kcal = models.FloatField(
        default=0.0,
        verbose_name=_("énergie (Jones)"),
        help_text=_("énergie N x facteur Jones avec fibres (kcal/100g)"))
    water = models.FloatField(
        default=0.0,
        verbose_name=_("eau"),
        help_text=_("eau (g/100g)"))
    protein = models.FloatField(
        default=0.0,
        verbose_name=_("protéines"),
        help_text=_("protéines (g/100g)"))
    raw_protein = models.FloatField(
        default=0.0,
        verbose_name=_("protéines brutes"),
        help_text=_("protéines brutes N x 6.25 (g/100g)"))
    carb = models.FloatField(
        default=0.0,
        verbose_name=_("glucides"),
        help_text=_("glucides (g/100g)"))
    lipid = models.FloatField(
        default=0.0,
        verbose_name=_("lipides"),
        help_text=_("lipides (g/100g)"))
    sugar = models.FloatField(
        default=0.0,
        verbose_name=_("sucres"),
        help_text=_("sucres (g/100g)"))
    starch = models.FloatField(
        default=0.0,
        verbose_name=_("amidons"),
        help_text=_("amidons (g/100g)"))
    fiber = models.FloatField(
        default=0.0,
        verbose_name=_("fibres alimentaires"),
        help_text=_("fibres alimentaires (g/100g)"))
    sugar_alcohol = models.FloatField(
        default=0.0,
        verbose_name=_("polyols"),
        help_text=_("polyols totaux (g/100g)"))
    ash = models.FloatField(
        default=0.0,
        verbose_name=_("cendres"),
        help_text=_("cendres (g/100g)"))
    alcohol = models.FloatField(
        default=0.0,
        verbose_name=_("alcool"),
        help_text=_("alcool (g/100g)"))
    organic_acid = models.FloatField(
        default=0.0,
        verbose_name=_("acide organique"),
        help_text=_("acide organique (g/100g)"))
    saturated_fat = models.FloatField(
        default=0.0,
        verbose_name=_("acide gras saturé"),
        help_text=_("acide gras saturé (g/100g)"))
    unsaturated_fat = models.FloatField(
        default=0.0,
        verbose_name=_("acide gras monoinsaturé"),
        help_text=_("acide gras monoisaturé (g/100g)"))
    polyunsaturated_fat = models.FloatField(
        default=0.0,
        verbose_name=_("acide gras polyinsaturé"),
        help_text=_("acide gras polyinsaturé (g/100g)"))
    butyric_acid = models.FloatField(
        default=0.0,
        verbose_name=_("acide butyrique"),
        help_text=_("acide butyrique (acide gras saturé 4:0) (g/100g)"))
    caproic_acid = models.FloatField(
        default=0.0,
        verbose_name=_("acide caproïque"),
        help_text=_("acide caproïque (acide gras saturé 6:0) (g/100g)"))
    caprylic_acid = models.FloatField(
        default=0.0,
        verbose_name=_("acide caprylique"),
        help_text=_("acide caprylique (acide gras saturé 8:0) (g/100g)"))
    capric_acid = models.FloatField(
        default=0.0,
        verbose_name=_("acide caprique"),
        help_text=_("acide caprique (acide gras saturé 10:0) (g/100g)"))
    lauric_acid = models.FloatField(
        default=0.0,
        verbose_name=_("acide laurique"),
        help_text=_("acide laurique (acide gras saturé 12:0) (g/100g)"))
    myristic_acid = models.FloatField(
        default=0.0,
        verbose_name=_("acide myristique"),
        help_text=_("acide myristique (acide gras saturé 14:0) (g/100g)"))
    palmitic_acid = models.FloatField(
        default=0.0,
        verbose_name=_("acide palmitique"),
        help_text=_("acide palmitique (acide gras saturé 16:0) (g/100g)"))
    stearic_acid = models.FloatField(
        default=0.0,
        verbose_name=_("acide stéarique"),
        help_text=_("acide stéarique (acide gras saturé 18:0) (g/100g)"))
    oleic_acid = models.FloatField(
        default=0.0,
        verbose_name=_("acide oléique"),
        help_text=_("acide oléique (acide gras insaturé 18:1) (g/100g)"))
    linoleic_acid = models.FloatField(
        default=0.0,
        verbose_name=_("acide linoléique"),
        help_text=_("acide linoléique (acide gras insaturé 18:2) (g/100g)"))
    alpha_linoleic_acid = models.FloatField(
        default=0.0,
        verbose_name=_("acide alpha-linoléique"),
        help_text=_("acide alpha-linoléique (acide gras insaturé 18:3) (g/100g)"))
    arachidic_acid = models.FloatField(
        default=0.0,
        verbose_name=_("acide arachidonique"),
        help_text=_("acide arachidonique (acide gras saturé 20:3) (g/100g)"))
    epa = models.FloatField(
        default=0.0,
        verbose_name=_("EPA"),
        help_text=_("acide eicosapentaénoïque (acide gras insaturé 20:4) (g/100g)"))
    dha = models.FloatField(
        default=0.0,
        verbose_name=_("DHA"),
        help_text=_("acide docosahexaénoïque (acide gras insaturé 22:6) (g/100g)"))
    cholesterol = models.FloatField(
        default=0.0,
        verbose_name=_("cholestérol"),
        help_text=_("cholestérol (mg/100g)"))
    salt = models.FloatField(
        default=0.0,
        verbose_name=_("sel"),
        help_text=_("sel/chlorure de sodium (g/100g)"))
    calcium = models.FloatField(
        default=0.0,
        verbose_name=_("calcium"),
        help_text=_("calcium (mg/100g)"))
    chloride = models.FloatField(
        default=0.0,
        verbose_name=_("chlorure"),
        help_text=_("chlorure (mg/100g)"))
    copper = models.FloatField(
        default=0.0,
        verbose_name=_("cuivre"),
        help_text=_("cuivre (mg/100g)"))
    iron = models.FloatField(
        default=0.0,
        verbose_name=_("fer"),
        help_text=_("fer (mg/100g)"))
    iodide = models.FloatField(
        default=0.0,
        verbose_name=_("iodure"),
        help_text=_("iodure (µg/100g)"))
    magnesium = models.FloatField(
        default=0.0,
        verbose_name=_("magnésium"),
        help_text=_("magnésium (mg/100g)"))
    manganese = models.FloatField(
        default=0.0,
        verbose_name=_("manganèse"),
        help_text=_("manganèse (mg/100g)"))
    phosphorus = models.FloatField(
        default=0.0,
        verbose_name=_("phosphore"),
        help_text=_("phosphore (mg/100g)"))
    potassium = models.FloatField(
        default=0.0,
        verbose_name=_("potassium"),
        help_text=_("potassium (mg/100g)"))
    selenium = models.FloatField(
        default=0.0,
        verbose_name=_("sélénium"),
        help_text=_("sélénium (µg/100g)"))
    sodium = models.FloatField(
        default=0.0,
        verbose_name=_("sodium"),
        help_text=_("sodium (mg/100g)"))
    zinc = models.FloatField(
        default=0.0,
        verbose_name=_("zinc"),
        help_text=_("zinc (mg/100g)"))
    retinol = models.FloatField(
        default=0.0,
        verbose_name=_("rétinol"),
        help_text=_("rétinol (vitamine A) (µg/100g)"))
    beta_carotene = models.FloatField(
        default=0.0,
        verbose_name=_("béta-carotène"),
        help_text=_("béta-carotène (vitamine A) (µg/100g)"))
    vitamin_d = models.FloatField(
        default=0.0,
        verbose_name=_("vitamine D"),
        help_text=_("vitamine D (µg/100g)"))
    vitamin_e = models.FloatField(
        default=0.0,
        verbose_name=_("vitamine E"),
        help_text=_("vitamine E (mg/100g)"))
    vitamin_k1 = models.FloatField(
        default=0.0,
        verbose_name=_("vitamine K1"),
        help_text=_("vitamine K1 (µg/100g)"))
    vitamin_k2 = models.FloatField(
        default=0.0,
        verbose_name=_("vitamine K2"),
        help_text=_("vitamine K2 (µg/100g)"))
    vitamin_c = models.FloatField(
        default=0.0,
        verbose_name=_("vitamine C"),
        help_text=_("vitamine C (mg/100g)"))
    vitamin_b1 = models.FloatField(
        default=0.0,
        verbose_name=_("vitamine B1"),
        help_text=_("vitamine B1 (thiamine) (mg/100g)"))
    vitamin_b2 = models.FloatField(
        default=0.0,
        verbose_name=_("vitamine B2"),
        help_text=_("vitamine B2 (riboflavine) (mg/100g)"))
    vitamin_b3 = models.FloatField(
        default=0.0,
        verbose_name=_("vitamine B3"),
        help_text=_("vitamine B3 (niacine) (mg/100g)"))
    vitamin_b5 = models.FloatField(
        default=0.0,
        verbose_name=_("vitamine B5"),
        help_text=_("vitamine B5 (acide penthothénique) (mg/100g)"))
    vitamin_b6 = models.FloatField(
        default=0.0,
        verbose_name=_("vitamine B6"),
        help_text=_("vitamine B6 (mg/100g)"))
    vitamin_b9 = models.FloatField(
        default=0.0,
        verbose_name=_("vitamine B9"),
        help_text=_("vitamine B9 (folates totaux) (µg/100g)"))
    vitamin_b12 = models.FloatField(
        default=0.0,
        verbose_name=_("vitamine B12"),
        help_text=_("vitamine B12 (µg/100g)"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("aliment")
        verbose_name_plural = _("aliments")


class Gym(CommonModel):
    """
    Salle de sport
    """
    name = models.CharField(
        max_length=100,
        verbose_name=_("nom"))
    adress = models.CharField(
        max_length=100,
        verbose_name=_("adresse"))
    coordinates = models.CharField(
        max_length=50, blank=True,
        verbose_name=_("coordonnées"))
    phone = models.CharField(
        max_length=20, blank=True,
        verbose_name=_("téléphone"))
    mail = models.EmailField(
        blank=True,
        verbose_name=_("e-mail"))
    delivery_time = models.PositiveSmallIntegerField(
        blank=True, null=True,
        verbose_name=_("temps de livraison"))
    active = models.BooleanField(
        default=True,
        verbose_name=_("actif"))

    class Meta:
        verbose_name = _("salle de sport")
        verbose_name_plural = _("salles de sport")


class MealConsumption(CommonModel):
    """
    Consommation de nourriture
    """
    MEAL_TYPES = (
        (1, _("déjeuner")),
        (2, _("brunch")),
        (3, _("dîner")),
        (4, _("collation")),
        (5, _("souper")),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name=_("utilisateur"))
    date = models.DateField(
        default=date.today(),
        verbose_name=_("date"))
    type = models.PositiveSmallIntegerField(
        blank=True, null=True, choices=MEAL_TYPES,
        verbose_name=_("type"))
    protein = models.FloatField(
        default=0.0,
        verbose_name=_("protéines"))
    carb = models.FloatField(
        default=0.0,
        verbose_name=_("glucides"))
    lipid = models.FloatField(
        default=0.0,
        verbose_name=_("lipides"))

    class Meta:
        verbose_name = _("consommation de nourriture")
        verbose_name_plural = _("consommations de nourriture")
        unique_together = ('user', 'date', 'type')


class WaterConsumption(CommonModel):
    """
    Consommation d'eau
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name=_("utilisateur"))
    date = models.DateField(
        default=date.today(),
        verbose_name=_("date"))
    quantity = models.IntegerField(
        default=0,
        verbose_name=_("quantité"))

    class Meta:
        verbose_name = _("consommation d'eau")
        verbose_name_plural = _("consommations d'eau")
        unique_together = ('user', 'date')


class Meal(Entity):
    """
    Repas
    """
    name = models.CharField(
        max_length=100,
        verbose_name=_("nom"))
    description = models.TextField(
        blank=True,
        verbose_name=_("description"))
    image = models.ImageField(
        blank=True, upload_to='meals',
        verbose_name=_("image"))
    energy_kcal = models.FloatField(
        default=0.0,
        verbose_name=_("énergie"))
    protein = models.FloatField(
        default=0.0,
        verbose_name=_("protéines"))
    carb = models.FloatField(
        default=0.0,
        verbose_name=_("glucides"))
    lipid = models.FloatField(
        default=0.0,
        verbose_name=_("lipides"))
    active = models.BooleanField(
        default=True,
        verbose_name=_("actif"))
    quantity_low = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_("perte de poids"))
    quantity_base = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_("stabilisation de poids"))
    quantity_high = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_("prise de poids"))

    class Meta:
        verbose_name = _("repas")
        verbose_name_plural = _("repas")


# Liste de tous les modèles connus
MODELS = (FoodGroup, Food, Gym, MealConsumption, WaterConsumption, Meal, )
