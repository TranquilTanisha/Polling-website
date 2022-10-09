# Generated by Django 4.1.1 on 2022-10-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0006_adivcandidate_adivregistration_bdivcandidate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adivcandidate',
            name='div',
            field=models.CharField(blank=True, choices=[('A', 'COMPS A')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='adivcandidate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='adivcandidate',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='adivregistration',
            name='div',
            field=models.CharField(blank=True, choices=[('A', 'COMPS A')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='adivregistration',
            name='email_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='adivregistration',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='adivregistration',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='adivregistration',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bdivcandidate',
            name='div',
            field=models.CharField(blank=True, choices=[('B', 'COMPS B')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='bdivcandidate',
            name='email_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bdivcandidate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bdivcandidate',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bdivregistration',
            name='div',
            field=models.CharField(blank=True, choices=[('B', 'COMPS B')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='bdivregistration',
            name='email_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bdivregistration',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bdivregistration',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bdivregistration',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
