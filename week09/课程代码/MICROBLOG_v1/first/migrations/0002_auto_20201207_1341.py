# Generated by Django 2.2.12 on 2020-12-07 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['createtime']},
        ),
        migrations.AddField(
            model_name='articles',
            name='owner',
            field=models.CharField(default='abc', max_length=50),
        ),
        migrations.AlterField(
            model_name='articles',
            name='createtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
