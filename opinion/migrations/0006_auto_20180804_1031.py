# Generated by Django 2.1 on 2018-08-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0005_auto_20180804_0948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opinion',
            options={'ordering': ('-publish_date',)},
        ),
        migrations.AlterField(
            model_name='item',
            name='type_text',
            field=models.CharField(choices=[('product', 'Product'), ('service', 'Service'), ('', 'Select type')], max_length=7),
        ),
    ]
