# Generated by Django 2.0.5 on 2018-05-10 15:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('code', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='code')),
                ('name', models.CharField(max_length=1000, verbose_name='nom')),
                ('energy_eu', models.FloatField(default=0.0, help_text='énergie selon le réglement UE N°1169/2001 (kcal/100g)', verbose_name='énergie (UE)')),
                ('energy_kj', models.FloatField(default=0.0, help_text='énergie N x facteur Jones avec fibres (kJ/100g)', verbose_name='énergie (Jones)')),
                ('energy_kcal', models.FloatField(default=0.0, help_text='énergie N x facteur Jones avec fibres (kcal/100g)', verbose_name='énergie (Jones)')),
                ('water', models.FloatField(default=0.0, help_text='eau (g/100g)', verbose_name='eau')),
                ('protein', models.FloatField(default=0.0, help_text='protéines (g/100g)', verbose_name='protéines')),
                ('raw_protein', models.FloatField(default=0.0, help_text='protéines brutes N x 6.25 (g/100g)', verbose_name='protéines brutes')),
                ('carb', models.FloatField(default=0.0, help_text='glucides (g/100g)', verbose_name='glucides')),
                ('lipid', models.FloatField(default=0.0, help_text='lipides (g/100g)', verbose_name='lipides')),
                ('sugar', models.FloatField(default=0.0, help_text='sucres (g/100g)', verbose_name='sucres')),
                ('starch', models.FloatField(default=0.0, help_text='amidons (g/100g)', verbose_name='amidons')),
                ('fiber', models.FloatField(default=0.0, help_text='fibres alimentaires (g/100g)', verbose_name='fibres alimentaires')),
                ('sugar_alcohol', models.FloatField(default=0.0, help_text='polyols totaux (g/100g)', verbose_name='polyols')),
                ('ash', models.FloatField(default=0.0, help_text='cendres (g/100g)', verbose_name='cendres')),
                ('alcohol', models.FloatField(default=0.0, help_text='alcool (g/100g)', verbose_name='alcool')),
                ('organic_acid', models.FloatField(default=0.0, help_text='acide organique (g/100g)', verbose_name='acide organique')),
                ('saturated_fat', models.FloatField(default=0.0, help_text='acide gras saturé (g/100g)', verbose_name='acide gras saturé')),
                ('unsaturated_fat', models.FloatField(default=0.0, help_text='acide gras monoisaturé (g/100g)', verbose_name='acide gras monoinsaturé')),
                ('polyunsaturated_fat', models.FloatField(default=0.0, help_text='acide gras polyinsaturé (g/100g)', verbose_name='acide gras polyinsaturé')),
                ('butyric_acid', models.FloatField(default=0.0, help_text='acide butyrique (acide gras saturé 4:0) (g/100g)', verbose_name='acide butyrique')),
                ('caproic_acid', models.FloatField(default=0.0, help_text='acide caproïque (acide gras saturé 6:0) (g/100g)', verbose_name='acide caproïque')),
                ('caprylic_acid', models.FloatField(default=0.0, help_text='acide caprylique (acide gras saturé 8:0) (g/100g)', verbose_name='acide caprylique')),
                ('capric_acid', models.FloatField(default=0.0, help_text='acide caprique (acide gras saturé 10:0) (g/100g)', verbose_name='acide caprique')),
                ('lauric_acid', models.FloatField(default=0.0, help_text='acide laurique (acide gras saturé 12:0) (g/100g)', verbose_name='acide laurique')),
                ('myristic_acid', models.FloatField(default=0.0, help_text='acide myristique (acide gras saturé 14:0) (g/100g)', verbose_name='acide myristique')),
                ('palmitic_acid', models.FloatField(default=0.0, help_text='acide palmitique (acide gras saturé 16:0) (g/100g)', verbose_name='acide palmitique')),
                ('stearic_acid', models.FloatField(default=0.0, help_text='acide stéarique (acide gras saturé 18:0) (g/100g)', verbose_name='acide stéarique')),
                ('oleic_acid', models.FloatField(default=0.0, help_text='acide oléique (acide gras insaturé 18:1) (g/100g)', verbose_name='acide oléique')),
                ('linoleic_acid', models.FloatField(default=0.0, help_text='acide linoléique (acide gras insaturé 18:2) (g/100g)', verbose_name='acide linoléique')),
                ('alpha_linoleic_acid', models.FloatField(default=0.0, help_text='acide alpha-linoléique (acide gras insaturé 18:3) (g/100g)', verbose_name='acide alpha-linoléique')),
                ('arachidic_acid', models.FloatField(default=0.0, help_text='acide arachidonique (acide gras saturé 20:3) (g/100g)', verbose_name='acide arachidonique')),
                ('epa', models.FloatField(default=0.0, help_text='acide eicosapentaénoïque (acide gras insaturé 20:4) (g/100g)', verbose_name='EPA')),
                ('dha', models.FloatField(default=0.0, help_text='acide docosahexaénoïque (acide gras insaturé 22:6) (g/100g)', verbose_name='DHA')),
                ('cholesterol', models.FloatField(default=0.0, help_text='cholestérol (mg/100g)', verbose_name='cholestérol')),
                ('salt', models.FloatField(default=0.0, help_text='sel/chlorure de sodium (g/100g)', verbose_name='sel')),
                ('calcium', models.FloatField(default=0.0, help_text='calcium (mg/100g)', verbose_name='calcium')),
                ('chloride', models.FloatField(default=0.0, help_text='chlorure (mg/100g)', verbose_name='chlorure')),
                ('copper', models.FloatField(default=0.0, help_text='cuivre (mg/100g)', verbose_name='cuivre')),
                ('iron', models.FloatField(default=0.0, help_text='fer (mg/100g)', verbose_name='fer')),
                ('iodide', models.FloatField(default=0.0, help_text='iodure (µg/100g)', verbose_name='iodure')),
                ('magnesium', models.FloatField(default=0.0, help_text='magnésium (mg/100g)', verbose_name='magnésium')),
                ('manganese', models.FloatField(default=0.0, help_text='manganèse (mg/100g)', verbose_name='manganèse')),
                ('phosphorus', models.FloatField(default=0.0, help_text='phosphore (mg/100g)', verbose_name='phosphore')),
                ('potassium', models.FloatField(default=0.0, help_text='potassium (mg/100g)', verbose_name='potassium')),
                ('selenium', models.FloatField(default=0.0, help_text='sélénium (µg/100g)', verbose_name='sélénium')),
                ('sodium', models.FloatField(default=0.0, help_text='sodium (mg/100g)', verbose_name='sodium')),
                ('zinc', models.FloatField(default=0.0, help_text='zinc (mg/100g)', verbose_name='zinc')),
                ('retinol', models.FloatField(default=0.0, help_text='rétinol (vitamine A) (µg/100g)', verbose_name='rétinol')),
                ('beta_carotene', models.FloatField(default=0.0, help_text='béta-carotène (vitamine A) (µg/100g)', verbose_name='béta-carotène')),
                ('vitamin_d', models.FloatField(default=0.0, help_text='vitamine D (µg/100g)', verbose_name='vitamine D')),
                ('vitamin_e', models.FloatField(default=0.0, help_text='vitamine E (mg/100g)', verbose_name='vitamine E')),
                ('vitamin_k1', models.FloatField(default=0.0, help_text='vitamine K1 (µg/100g)', verbose_name='vitamine K1')),
                ('vitamin_k2', models.FloatField(default=0.0, help_text='vitamine K2 (µg/100g)', verbose_name='vitamine K2')),
                ('vitamin_c', models.FloatField(default=0.0, help_text='vitamine C (mg/100g)', verbose_name='vitamine C')),
                ('vitamin_b1', models.FloatField(default=0.0, help_text='vitamine B1 (thiamine) (mg/100g)', verbose_name='vitamine B1')),
                ('vitamin_b2', models.FloatField(default=0.0, help_text='vitamine B2 (riboflavine) (mg/100g)', verbose_name='vitamine B2')),
                ('vitamin_b3', models.FloatField(default=0.0, help_text='vitamine B3 (niacine) (mg/100g)', verbose_name='vitamine B3')),
                ('vitamin_b5', models.FloatField(default=0.0, help_text='vitamine B5 (acide penthothénique) (mg/100g)', verbose_name='vitamine B5')),
                ('vitamin_b6', models.FloatField(default=0.0, help_text='vitamine B6 (mg/100g)', verbose_name='vitamine B6')),
                ('vitamin_b9', models.FloatField(default=0.0, help_text='vitamine B9 (folates totaux) (µg/100g)', verbose_name='vitamine B9')),
                ('vitamin_b12', models.FloatField(default=0.0, help_text='vitamine B12 (µg/100g)', verbose_name='vitamine B12')),
            ],
            options={
                'verbose_name': 'aliment',
                'verbose_name_plural': 'aliments',
            },
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='code')),
                ('name', models.CharField(max_length=1000, verbose_name='nom')),
                ('level', models.PositiveSmallIntegerField(choices=[(1, 'groupe'), (2, 'sous-groupe'), (3, 'sous-sous-groupe')], default=1, verbose_name='niveau')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subgroups', to='healthyfood.FoodGroup', verbose_name='parent')),
            ],
            options={
                'verbose_name': "groupe d'aliments",
                'verbose_name_plural': "groupe d'aliments",
            },
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nom')),
                ('adress', models.CharField(max_length=100, verbose_name='adresse')),
                ('coordinates', models.CharField(blank=True, max_length=50, verbose_name='coordonnées')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='téléphone')),
                ('mail', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
                ('delivery_time', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='temps de livraison')),
                ('active', models.BooleanField(default=True, verbose_name='actif')),
            ],
            options={
                'verbose_name': 'salle de sport',
                'verbose_name_plural': 'salles de sport',
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('name', models.CharField(max_length=100, verbose_name='nom')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='meals', verbose_name='image')),
                ('energy', models.FloatField(default=0.0, verbose_name='énergie')),
                ('protein', models.FloatField(default=0.0, verbose_name='protéines')),
                ('carb', models.FloatField(default=0.0, verbose_name='glucides')),
                ('lipid', models.FloatField(default=0.0, verbose_name='lipides')),
                ('active', models.BooleanField(default=True, verbose_name='actif')),
                ('quantity_low', models.PositiveSmallIntegerField(default=0, help_text='quantité (en g.) pour la perte de poids', verbose_name='quantité basse')),
                ('quantity_base', models.PositiveSmallIntegerField(default=0, help_text='quantité (en g.) pour le maintien du poids', verbose_name='quantité moyenne')),
                ('quantity_high', models.PositiveSmallIntegerField(default=0, help_text='quantité (en g.) pour la prise de poids', verbose_name='quantité elevée')),
                ('price', models.DecimalField(decimal_places=2, default='11.90', max_digits=4, verbose_name='prix')),
                ('current_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'repas',
                'verbose_name_plural': 'repas',
            },
        ),
        migrations.CreateModel(
            name='MealConsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='nom')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'déjeuner'), (2, 'brunch'), (3, 'dîner'), (4, 'collation'), (5, 'souper')], null=True, verbose_name='type')),
                ('energy', models.FloatField(default=0.0, verbose_name='énergie')),
                ('protein', models.FloatField(default=0.0, verbose_name='protéines')),
                ('carb', models.FloatField(default=0.0, verbose_name='glucides')),
                ('lipid', models.FloatField(default=0.0, verbose_name='lipides')),
                ('meal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='healthyfood.Meal', verbose_name='repas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'consommation de nourriture',
                'verbose_name_plural': 'consommations de nourriture',
            },
        ),
        migrations.CreateModel(
            name='MealPortion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='quantité')),
                ('consumption', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portions', to='healthyfood.MealConsumption', verbose_name='consommation')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='healthyfood.Food', verbose_name='ingrédient')),
                ('meal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portions', to='healthyfood.Meal', verbose_name='repas')),
            ],
            options={
                'verbose_name': 'portion',
                'verbose_name_plural': 'portions',
            },
        ),
        migrations.CreateModel(
            name='MealReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, verbose_name='message')),
                ('note', models.PositiveSmallIntegerField(choices=[(0, 'zéro'), (1, 'un'), (2, 'deux'), (3, 'trois'), (4, 'quatre'), (5, 'cinq')], default=3, verbose_name='note')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='healthyfood.Meal', verbose_name='plat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'avis',
                'verbose_name_plural': 'avis',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('is_read', models.BooleanField(default=False, verbose_name='lu')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL, verbose_name='expediteur')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL, verbose_name='destinataire')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'en préparation'), (2, 'en cours de livraison'), (3, 'livré')], default=1, verbose_name='status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'commande',
                'verbose_name_plural': 'commandes',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('L', 'perte de poids'), ('M', 'stabilisation'), ('H', 'prise de poids')], max_length=1, verbose_name='type')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='quantité')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='healthyfood.Meal', verbose_name='plat')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='healthyfood.Order', verbose_name='commande')),
            ],
            options={
                'verbose_name': 'élément de commande',
                'verbose_name_plural': 'éléments de commande',
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('C', 'coach'), ('S', 'élève'), ('F', 'ami')], max_length=1, verbose_name='type')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('valid', models.BooleanField(default=False, verbose_name='validée')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to=settings.AUTH_USER_MODEL, verbose_name='source')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to=settings.AUTH_USER_MODEL, verbose_name='cible')),
            ],
            options={
                'verbose_name': 'relation',
                'verbose_name_plural': 'relations',
            },
        ),
        migrations.CreateModel(
            name='WaterConsumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('quantity', models.IntegerField(default=0, verbose_name='quantité')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': "consommation d'eau",
                'verbose_name_plural': "consommations d'eau",
            },
        ),
        migrations.AddField(
            model_name='food',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='healthyfood.FoodGroup', verbose_name='groupe'),
        ),
        migrations.AlterUniqueTogether(
            name='waterconsumption',
            unique_together={('user', 'date')},
        ),
        migrations.AlterUniqueTogether(
            name='mealreview',
            unique_together={('meal', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='mealconsumption',
            unique_together={('user', 'date', 'type')},
        ),
    ]
