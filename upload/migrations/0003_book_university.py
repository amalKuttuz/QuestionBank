# Generated by Django 4.1.1 on 2022-12-02 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moderator', '0008_delete_prevqstns'),
        ('upload', '0002_remove_book_author_remove_book_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moderator.universities'),
        ),
    ]
