# Generated by Django 4.0 on 2022-04-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmaoBaseApp', '0026_categoriepreventif_cout_magasin_soustraitence_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intervenctioncurative',
            old_name='typeDePann',
            new_name='typeDePanne',
        ),
        migrations.AlterField(
            model_name='intervenctioncurative',
            name='dateCloture',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intervenctioncurative',
            name='dateDebutAction',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intervenctioncurative',
            name='dateFinAction',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]