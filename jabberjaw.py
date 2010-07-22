""" Jabber Jaw sends messages from Trac to an XMPP server of your choosing. """

from trac.core import *
from trac.util.html import html
from trac.web import IRequestHandler
from trac.web.chrome import INavigationContributor

class JabberJawPlugin(Component):
	implements(INavigationContributor, IRequestHandler)

	def get_active_navigation_item(self, req):
		return 'jabberjaw'
	def get_navigation_items(self, req):
		yield ('mainnav', 'jabberjaw',
			html.A('Jabber Jaw', href= req.href.jabberjaw()))

	def match_request(self, req):
		return req.path_info == '/helloworld'
	def process_request(self, req):
		req.send_response(200)
		req.send_header('Content-Type', 'text/html')
		req.end_headers()
		req.write('<h1>Jabber Jaw!</h1>')
