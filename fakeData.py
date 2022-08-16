# import os, random
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empTrack.settings')
# django.setup()


# #Script to populate fake data

# from faker import Faker
# from empDetail.models import Employee
# from django.contrib.auth.models import User
# from django.utils import timezone


# def populate(N):
#     fake = Faker()
#     for x in range(N):
#         id = random.randint(1,4)
#         name = fake.name()
#         print(name)
#         username = fake.name()
#         department = fake.name()
#         role = fake.name()
#         p = Employee.objects.create(name = name, username = username, department=department, role=role)
#         p.save()
#         print("Done")

# populate(10)
# print("Populated scripts!")



# # from django.core.management.base import BaseCommand
# # from faker import Faker

# # class Command(BaseCommand):
# #     help = 'Command information'

# #     def handle(self, *args, **kwargs):
# #         print('hello')


