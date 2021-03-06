
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
                ('alive', models.IntegerField(default=True, verbose_name='在售')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['create_time'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='数量')),
                ('amount', models.DecimalField(decimal_places=8, max_digits=10, verbose_name='金额')),
                ('alive', models.IntegerField(default=True, verbose_name='有效')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('shops', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='order.shops', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL, verbose_name='用户id')),
            ],
            options={
                'ordering': ['create_time'],
            },
        ),
    ]
