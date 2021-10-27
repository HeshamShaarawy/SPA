# Generated by Django 3.2.8 on 2021-10-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_treatment_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='category',
            field=models.IntegerField(choices=[(1, 'Facial and Skin Treatments'), (2, 'Massage'), (3, 'Lazer Treatments'), (4, 'Hand and Foot Treatments'), (5, 'Hair Services')], default=1),
        ),
    ]
