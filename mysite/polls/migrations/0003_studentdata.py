# Generated by Django 2.2.2 on 2019-06-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20190619_0722'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=40)),
                ('email_address', models.EmailField(max_length=100)),
                ('student_password', models.CharField(max_length=20)),
            ],
        ),
    ]
