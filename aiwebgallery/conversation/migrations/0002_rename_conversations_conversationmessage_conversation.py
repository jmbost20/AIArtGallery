# Generated by Django 4.2.2 on 2023-07-04 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='conversations',
            new_name='conversation',
        ),
    ]
