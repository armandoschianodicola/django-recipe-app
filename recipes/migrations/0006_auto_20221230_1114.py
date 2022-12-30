# Generated by Django 3.2.15 on 2022-12-30 11:14

from django.db import migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20221230_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]