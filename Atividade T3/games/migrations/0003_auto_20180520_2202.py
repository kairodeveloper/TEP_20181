# Generated by Django 2.0.5 on 2018-05-20 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20180516_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='game',
        ),
        migrations.RemoveField(
            model_name='score',
            name='player',
        ),
        migrations.AlterModelOptions(
            name='game',
            options={},
        ),
        migrations.AlterField(
            model_name='game',
            name='game_category',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='GameCategory',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='Score',
        ),
    ]
