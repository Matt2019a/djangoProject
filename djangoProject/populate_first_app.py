import datetime
import os
import django
import random

from faker import Faker
import uuid
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangoProject.settings')


django.setup()

fakeGen = Faker()

from base.models import Activity

def populate(N=10):
    for entry in range(N):
        id = str(entry)
        fake_date = fakeGen.date()
        fake_time = fakeGen.time()
        dateTime = datetime.datetime.now()
        fake_title = fakeGen.company()
        fake_text = fakeGen.text()

        activity = Activity.objects.get_or_create(id=id, title=fake_title, text=fake_text, date=dateTime)


if __name__ == '__main__':
    populate()