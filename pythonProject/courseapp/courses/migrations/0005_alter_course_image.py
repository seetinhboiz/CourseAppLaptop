# Generated by Django 5.0.3 on 2024-03-28 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='courses/%Y/%m/'),
        ),
    ]
