from django.db import migrations


def create_superuser_cook(apps, schema_editor):
    from django.contrib.auth import get_user_model
    Cook = get_user_model()

    if not Cook.objects.filter(username="user").exists():
        Cook.objects.create_superuser(
            username="user",
            email="admin@kitchen.com",
            password="user12345",
            first_name="Test",
            last_name="User",
            years_of_experience=5  # Додаємо обов'язкове поле твоєї моделі Cook
        )


class Migration(migrations.Migration):
    dependencies = [
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser_cook),
    ]