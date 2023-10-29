# Generated by Django 2.1 on 2023-07-12 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('styl_cd', models.CharField(max_length=30)),
                ('img1', models.CharField(max_length=100)),
                ('img2', models.CharField(max_length=100)),
                ('img3', models.CharField(max_length=100)),
                ('img4', models.CharField(max_length=100)),
                ('img5', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReviewD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('styl_cd', models.CharField(default='', max_length=30)),
                ('reviewdetail', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('styl_cd', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('brand_nm', models.CharField(max_length=30)),
                ('material_cd', models.CharField(max_length=100)),
                ('season_cd', models.CharField(max_length=20)),
            ],
        ),
    ]