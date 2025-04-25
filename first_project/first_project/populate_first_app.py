import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

#fake pop script
import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top = add_topic()

        #create the fake data for the entry
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()

        # create the new webpage entry
        Webpage = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #create a fake acess record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=Webpage, date=fake_date)[0]

if __name__ == '__main__':    
    print("Populating script!")
    populate(20)
    print("Populating complete!")
        