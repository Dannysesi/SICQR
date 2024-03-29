# Generated by Django 4.2.2 on 2024-02-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdbm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='guardian_add',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Guardian Home Address'),
        ),
        migrations.AlterField(
            model_name='student',
            name='if_not_healthy',
            field=models.CharField(blank=True, help_text='If not healthy kindly state the aligment', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='next_of_kin_address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='next_of_kin_email',
            field=models.EmailField(blank=True, help_text='Next of Kin emaill address', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='next_of_kin_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='other_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
