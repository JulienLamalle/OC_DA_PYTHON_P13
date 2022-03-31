# Generated by Django 3.0 on 2022-03-31 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    
    def transfer_old_profiles_to_new_table(apps, schema_editor):
        Profile = apps.get_model('profiles', 'Profile')
        
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM oc_lettings_site_profile''')
        users = cursor.fetchall()
        
        for user in users:
            Profile.objects.create(
                id=user[0],
                favorite_city=user[1],
                user_id=user[2],
            )

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_city', models.CharField(blank=True, max_length=64)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        
        migrations.RunPython(transfer_old_profiles_to_new_table),
    ]