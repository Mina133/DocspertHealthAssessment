# Generated by Django 5.1.4 on 2024-12-15 18:36

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountTransfer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('destination_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_transfers', to='AccountTransfer.account')),
                ('source_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_transfers', to='AccountTransfer.account')),
            ],
        ),
    ]