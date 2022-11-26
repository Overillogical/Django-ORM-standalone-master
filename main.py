import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

amount_active_passcards = 0


if __name__ == '__main__':
    passcards = Passcard.objects.all()
    some_passcard = passcards[0]
    print(f'Owner name : {some_passcard.owner_name}\n'
        f'Passcode : {some_passcard.passcode}\n'
        f'Created_at : {some_passcard.created_at}\n'
        f'Is active : {some_passcard.is_active}')
    for passcard in passcards:
        if passcard.is_active == True:
            amount_active_passcards += 1 
    print(f'Всего пропусков: {len(passcards)}\n'
        f'Активных пропусков: {amount_active_passcards}')

