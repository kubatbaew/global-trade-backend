import json
from django.core.management.base import BaseCommand
from apps.clients.models import Client

class Command(BaseCommand):
    help = 'Импорт клиентов из datac.json в базу данных'

    def handle(self, *args, **kwargs):
        try:
            with open("datac.json", "r", encoding="utf-8") as file:
                clients = json.load(file)
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR("Файл datac.json не найден"))
            return
        except json.JSONDecodeError as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при чтении JSON: {e}"))
            return

        if not clients:
            self.stdout.write(self.style.WARNING("Список клиентов пуст"))
            return

        created_count = 0
        skipped_count = 0

        for client in clients:
            client_code = client.get('client_code')

            # Если client_code пуст — пропускаем
            if not client_code:
                skipped_count += 1
                continue

            # Проверка по уникальному коду
            if Client.objects.filter(client_code=client_code).exists():
                skipped_count += 1
                continue

            client_data = {
                'client_code': client_code,
                'first_name': client.get('name'),
                'last_name': client.get('surname'),
                'phone_number': client.get('phone_number'),
                'whatsapp_number': client.get('phone_number_whatsapp'),
                'city': client.get('city'),
                'china_warehouse_address': client.get('guanjou_address'),
                'address': client.get('address') or None
            }

            Client.objects.create(**client_data)
            created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Создано {created_count} клиентов, пропущено {skipped_count}"
            )
        )
