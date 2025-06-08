from django.test import TestCase
from django.utils import timezone
from .models import WaiterCall, MenuItem
# Create your tests here.

#may need to double check this
#https://docs.djangoproject.com/en/5.0/topics/testing/overview/
class TestWaiterCall(TestCase):

    # assumption is expiration is still 12 hours
    # should change to use some externally strored variable later.

    def testRecent(self):
        recentTimestamp = timezone.now() - timezone.timedelta(hours=2)
        waiterCall = WaiterCall(timestamp=recentTimestamp)

        self.assertFalse(waiterCall.isStale())

    def testStale(self):
        oldTimestamp = timezone.now() - timezone.timedelta(hours=30)
        waiterCall = WaiterCall(timestamp=oldTimestamp)

        self.assertTrue(waiterCall.isStale())


class testTrue(TestCase):
    def testTrue(self):
        self.assertTrue(True==True)

