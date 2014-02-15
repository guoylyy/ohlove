from django.test import TestCase
from postbox.models import *
from datetime import datetime,date

class SimpleTest(TestCase):
    def test_add_post(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        #post(content="dsadsa fsdaf sdf sdaf dasf sdf ds fsa",datetime=datetime.now(),weekday="Sunday").save()
        d = date.today()
        dt1 = datetime(d.year,d.month,d.day)
        dt2 = datetime(d.year,d.month,d.day,23,59,59)
        #posts = post.objects.filter(datetime__startswith='2014-02-14')     
        posts = post.objects.filter(datetime__lt=dt2,datetime__gt=dt1)
        print(len(posts))
        print('%d-%d-%d'%(d.year,d.month,d.day))
        self.assertEqual(1 + 1, 2)

    def test_older_post(self):
    	d = date.today()