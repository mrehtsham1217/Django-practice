import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Udemy.settings")
django.setup()
from myApp.models import UsersModel
from faker import Faker

fakegen=Faker()

def populate(N=5):
    for i in range(N):
        fake_name=fakegen.name().split()
        fake_first_name=fake_name[0]
        fake_last_name=fake_name[1]
        fake_emails=fakegen.email()
        users=UsersModel.objects.get_or_create(firstname=fake_first_name,lastname=fake_last_name,email=fake_emails)[0]
        
if __name__=="__main__":
    print("Start creating fake data")
    populate(100)
    print("data is created")

