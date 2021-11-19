# Generated by Django 2.1 on 2021-09-25 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matter_ref', models.TextField(blank=True, null=True)),
                ('code', models.TextField(blank=True, null=True)),
                ('matter_no', models.TextField(blank=True, null=True)),
                ('county', models.TextField(blank=True, null=True)),
                ('staff', models.TextField(blank=True, null=True)),
                ('buyer', models.TextField(blank=True, null=True)),
                ('buyer_firm', models.TextField(blank=True, null=True)),
                ('buyer_phone', models.TextField(blank=True, null=True)),
                ('seller', models.TextField(blank=True, null=True)),
                ('seller_firm', models.TextField(blank=True, null=True)),
                ('seller_phone', models.TextField(blank=True, null=True)),
                ('client', models.TextField(blank=True, null=True)),
                ('property', models.TextField(blank=True, null=True)),
                ('lot_no', models.TextField(blank=True, null=True)),
                ('purchase', models.TextField(blank=True, null=True)),
                ('downpay', models.TextField(blank=True, null=True)),
                ('attorney', models.TextField(blank=True, null=True)),
                ('attorney_firm', models.TextField(blank=True, null=True)),
                ('attorney_phone', models.TextField(blank=True, null=True)),
                ('lender', models.TextField(blank=True, null=True)),
                ('loan_office', models.TextField(blank=True, null=True)),
                ('lender_phone', models.TextField(blank=True, null=True)),
                ('broker', models.TextField(blank=True, null=True)),
                ('broker_firm', models.TextField(blank=True, null=True)),
                ('broker_phone', models.TextField(blank=True, null=True)),
            ],
        ),
    ]