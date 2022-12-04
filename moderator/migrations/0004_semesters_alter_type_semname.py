# Generated by Django 4.1.1 on 2022-11-30 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moderator', '0003_type_alter_papers_semester_delete_semesters'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semesters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestername', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='type',
            name='semname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moderator.semesters'),
        ),
    ]
