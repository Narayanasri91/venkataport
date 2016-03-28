# [START imports]
import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import memcache
import json
import difflib
import json as m_json
import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'



class Mail(ndb.Model):
    """Models a Guestbook entry with an author, content, avatar, and date."""
    question = ndb.TextProperty()
    email = ndb.StringProperty()

class Feedback(ndb.Model):
    """Models a Guestbook entry with an author, content, avatar, and date."""
    comment = ndb.TextProperty()
    points = ndb.TextProperty()
    email = ndb.StringProperty()

def guestbook_key(guestbook_name=None):
    """Constructs a Datastore key for a Guestbook entity with name."""
    return ndb.Key('Guestbook', guestbook_name or 'default_guestbook')


class MainPage(webapp2.RequestHandler):

    def get(self):

        template = JINJA_ENVIRONMENT.get_template('index.html')

        template_values = {

        }
        self.response.write(template.render(template_values))


class Guestbook(webapp2.RequestHandler):

    def post(self):
        info = self.request.get('question')
        selection = self.request.get('email')
        greeting = Mail(parent=guestbook_key('browse'))
        greeting.question = info
        greeting.email = selection
        greeting.put()

class Feed(webapp2.RequestHandler):

    def post(self):
        info = self.request.get('comment')
        point = self.request.get('points')       
        selection = self.request.get('email')
        greeting = Feedback(parent=guestbook_key('browse'))
        greeting.comment = info
        greeting.points = point
        greeting.email = selection
        greeting.put()

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/submit', Guestbook),
    ('/feed', Feed),
], debug=True)
