# Generated by Django 3.0 on 2022-03-31 15:51

from django.conf import settings
from django.db import OperationalError, migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]
    
    def transfer_old_adresses_data_to_adresses_model(apps, schema_editor):
        Address = apps.get_model('lettings', 'Address')
        
        from django.db import connection
        cursor = connection.cursor()
        try:
            cursor.execute('''SELECT * FROM oc_lettings_site_address''')
            addresses = cursor.fetchall()
            
            for address in addresses:
                Address.objects.create(
                    id=address[0],
                    number=address[1],
                    street=address[2],
                    city=address[3],
                    state=address[4],
                    zip_code=address[5],
                    country_iso_code=address[6],
                )
        except OperationalError:
            print("No old data to transfer")
    
    def transfer_lettings_data_to_lettings(apps, schema_editor):
        Letting = apps.get_model('lettings', 'Letting')
        
        from django.db import connection
        cursor = connection.cursor()
        try:
            cursor.execute('''SELECT * FROM oc_lettings_site_letting''')
            lettings = cursor.fetchall()
            
            for letting in lettings:
                Letting.objects.create(
                    id=letting[0],
                    title=letting[1],
                    address_id=letting[2],
                )
        except OperationalError:
            print("No old data to transfer")

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('street', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('zip_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                ('country_iso_code', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        
        migrations.RunPython(transfer_old_adresses_data_to_adresses_model),
        
        migrations.CreateModel(
            name='Letting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lettings.Address')),
            ],
            options={
                'verbose_name': 'Letting',
                'verbose_name_plural': 'Lettings',
            },
        ),
        
        migrations.RunPython(transfer_lettings_data_to_lettings),
    ]