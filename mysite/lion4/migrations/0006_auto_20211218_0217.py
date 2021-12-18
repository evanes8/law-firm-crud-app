# Generated by Django 3.2.7 on 2021-12-18 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lion4', '0005_auto_20211130_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='')),
                ('firm', models.TextField(blank=True, default='')),
                ('phone', models.TextField(blank=True, default='')),
                ('fax', models.TextField(blank=True, default='')),
                ('email', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='record',
            name='attorney',
        ),
        migrations.RemoveField(
            model_name='record',
            name='attorney_firm',
        ),
        migrations.RemoveField(
            model_name='record',
            name='attorney_phone',
        ),
        migrations.RemoveField(
            model_name='record',
            name='broker',
        ),
        migrations.RemoveField(
            model_name='record',
            name='broker_firm',
        ),
        migrations.RemoveField(
            model_name='record',
            name='broker_phone',
        ),
        migrations.RemoveField(
            model_name='record',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='record',
            name='buyer_firm',
        ),
        migrations.RemoveField(
            model_name='record',
            name='buyer_phone',
        ),
        migrations.RemoveField(
            model_name='record',
            name='client',
        ),
        migrations.RemoveField(
            model_name='record',
            name='lender',
        ),
        migrations.RemoveField(
            model_name='record',
            name='lender_phone',
        ),
        migrations.RemoveField(
            model_name='record',
            name='loan_office',
        ),
        migrations.RemoveField(
            model_name='record',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='record',
            name='seller_firm',
        ),
        migrations.RemoveField(
            model_name='record',
            name='seller_phone',
        ),
        migrations.AlterField(
            model_name='record',
            name='matter_no',
            field=models.IntegerField(blank=True, default=''),
        ),
        migrations.CreateModel(
            name='Record_Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_client', models.BooleanField(default=0)),
                ('role', models.CharField(choices=[('BY', 'Buyer'), ('SL', 'Seller'), ('AT', 'Attorney'), ('LN', 'Lender'), ('BR', 'Broker'), ('OT', 'Other')], max_length=2)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lion4.contact')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lion4.standard_record')),
            ],
        ),
    ]