
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shops',
            name='alive',
            field=models.BooleanField(default=True, verbose_name='在售'),
        ),
        migrations.AlterField(
            model_name='order',
            name='alive',
            field=models.BooleanField(default=True, verbose_name='有效'),
        ),
    ]
