# Generated by Django 4.0.4 on 2022-04-23 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_post_postimage_x'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='testblog',
            new_name='Post',
        ),
        migrations.RenameField(
            model_name='postimage',
            old_name='x',
            new_name='post',
        ),
    ]
