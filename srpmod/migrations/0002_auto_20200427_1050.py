# Generated by Django 2.2.9 on 2020-04-27 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srpmod', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='srppaymenttoken',
            options={'permissions': (('view_global_srp_stats', 'Can View All SRP Stats'), ('view_own_srp_stats', 'Can View Personal SRP Stats'))},
        ),
    ]
