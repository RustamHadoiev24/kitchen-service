from django.db import migrations

def create_superuser_cook(apps, schema_editor):
    from django.contrib.auth import get_user_model
    Cook = get_user_model()
    if not Cook.objects.filter(username="user").exists():
        user = Cook.objects.create(
            username="user",
            email="admin@kitchen.com",
            is_superuser=True,
            is_staff=True,
            is_active=True,
            first_name="Test",
            last_name="User",
            years_of_experience=5
        )
        user.set_password("user12345")
        user.save()

class Migration(migrations.Migration):
    dependencies = [
        ('kitchen', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_superuser_cook),
    ]
