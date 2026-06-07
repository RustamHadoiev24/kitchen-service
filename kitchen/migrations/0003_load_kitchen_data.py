from django.db import migrations
import os


def load_local_data(apps, schema_editor):
    from django.core.management import call_command
    from django.conf import settings

    fixture_path = os.path.join(settings.BASE_DIR, 'datadump.json')

    if os.path.exists(fixture_path):
        try:
            print("=== Починаємо імпорт даних на Render... ===")
            call_command('loaddata', fixture_path)
            print("=== Усі дані успішно відновлено! ===")
        except Exception as e:
            print(f"⚠️ Помилка loaddata: {e}")
    else:
        print(f"⚠️ Файл {fixture_path} не знайдено.")


class Migration(migrations.Migration):
    dependencies = [
        ('kitchen', '0002_create_superuser'),
    ]
    operations = [
        migrations.RunPython(load_local_data),
    ]
