# Generated by Django 2.1.5 on 2019-02-01 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, default='0.0', max_digits=9)),
                ('checksum', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('waiting', 'Waiting'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected'), ('error', 'Error')], default=('waiting', 'Waiting'), max_length=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'ordering': ['created'],
            },
        ),
    ]