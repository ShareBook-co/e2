# Generated by Django 3.2.8 on 2021-10-19 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sharebookApp', '0003_auto_20211017_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='sharebookApp.user'),
            preserve_default=False,
        ),
    ]
