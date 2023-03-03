# Generated by Django 3.2.18 on 2023-03-02 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='aum',
            field=models.IntegerField(null=True, verbose_name='AUM (USD)'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='inception_date',
            field=models.DateTimeField(null=True, verbose_name='Inception Date'),
        ),
    ]
