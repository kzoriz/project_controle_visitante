# Generated by Django 3.2.8 on 2021-11-06 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitante',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO', 'Aguardando autorização'), ('EM_VISITA', 'Em visita'), ('FINALIZADO', 'Visita finalizada')], default='AGUARDANDO', max_length=10, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='visitante',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data de nascimento'),
        ),
    ]
