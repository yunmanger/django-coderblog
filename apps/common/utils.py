import datetime
from django.utils.translation import ugettext as _
from django.conf import settings

from common.models import TwitterStatus

import twitter, pickle

def clever_date(date):
    now = datetime.datetime.now()
    td = now-date
    if (td.days == 0):
        return '%s:%s' % (date.hour, date.minute)
    elif (td.days == 1):
        return '%s %s:%s' % (_("yesterday"), date.hour, date.minute)
    elif (td.days < 365):
        return '%s %s' % (_("%s." % date.strftime("%b")), date.day)
    else: 
        return date.strftime("%Y.%m.%d")
    
def download_twitter_statuses():
    username, password = settings.TWITTER_USER, settings.TWITTER_PASSWORD
    api = twitter.Api(username=username, password = password)
    all = api.GetUserTimeline(settings.TWITTER_USER)
    for x in all:
        ts, c = TwitterStatus.objects.get_or_create(tid=x.id)
        ts.pub_date = datetime.datetime.fromtimestamp(x.created_at_in_seconds)
        ts.text = x.text
        ts.pickle_zip = pickle.dumps(x)
        ts.save()
        
def post_to_twitter(string):
    username, password = settings.TWITTER_USER, settings.TWITTER_PASSWORD
    api = twitter.Api(username=username, password = password)
    x = api.PostUpdate(string)
    ts, c = TwitterStatus.objects.get_or_create(tid=x.id)
    ts.pub_date = datetime.datetime.fromtimestamp(x.created_at_in_seconds)
    ts.text = x.text
    ts.pickle_zip = pickle.dumps(x)
    ts.save()
