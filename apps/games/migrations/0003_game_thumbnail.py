# Generated by Django 2.1.5 on 2019-02-14 22:31


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='thumbnail'),
        ),
    ]
