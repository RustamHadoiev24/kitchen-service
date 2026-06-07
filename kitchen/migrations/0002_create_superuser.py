from django.db import migrations
import os


def create_superuser_and_load_data(apps, schema_editor):
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
        print("=== Суперюзера 'user' успішно створено! ===")

    from django.core.management import call_command
    from django.conf import settings

    fixture_path = os.path.join(settings.BASE_DIR, 'datadump.json')

    if os.path.exists(fixture_path):
        try:
            print(f"=== Знайдено файл даних за шляхом: {fixture_path}. Починаємо імпорт... ===")
            call_command('loaddata', fixture_path)
            print("=== Усі локальні дані успішно перенесені на Render! ===")
        except Exception as e:
            print(f"⚠️ Помилка під час виконання loaddata: {e}")
    else:
        print(f"⚠️ Файл {fixture_path} не знайдено в корені проєкту. Пропускаємо імпорт даних.")


class Migration(migrations.Migration):
    dependencies = [
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser_and_load_data),
    ]
