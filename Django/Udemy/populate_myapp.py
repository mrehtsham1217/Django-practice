import os
import django

# Set the default Django settings module
# Udemy is project name
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Udemy.settings")
django.setup()

# Creating fake scripts
import random
from myApp.models import Webpage, Topics, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Democracy', 'Computer', 'Games', 'Marketplace', 'Social']

def add_topics():
    top = Topics.objects.get_or_create(topic_name=random.choice(topics))[0]
    top.save()
    return top

def populate(N=5):
    for i in range(N):
        top = add_topics()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        records = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == "__main__":
    print("Start populating script")
    populate(20)
    print("End populating script")
