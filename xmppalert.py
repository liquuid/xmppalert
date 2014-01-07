#!/usr/bin/env python

import xmpp
import os
import sys
import socket
import settings
import tasks.mysqlcheck
import tasks.loadcheck

class Monitor(object):

	def __init__(self):
		self.cnx = xmpp.Client(settings.xmpp_host, debug=[])
		self.cnx.connect( server=(settings.xmpp_host,settings.xmpp_port) )
		self.cnx.auth(settings.xmpp_user, settings.xmpp_password, 'botty')

	def run_tests(self):
		if "mysql_check" in settings.tasks:
			for db in settings.mysql:
				myCh = tasks.mysqlcheck.MysqlCheck(db["mysql_host"], db["mysql_user"], db["mysql_password"], db["mysql_database"])
				if not myCh.test():
					self._send_message("Problemas no banco %s" % db["mysql_host"])		

		if "load_check" in settings.tasks:
			myCh = tasks.loadcheck.LoadCheck(settings.max_load)
			if not myCh.test():
				self._send_message("Load Muito alto %s" % os.getloadavg()[0])		

	def _send_message(self, msg):
		roster = self.cnx.getRoster()
        	for peer in roster.keys():
            		roster.Authorize(peer)
			self.cnx.send( xmpp.Message( peer ,"[%s] %s" % (socket.gethostname(), msg) ) )		
			
mon=Monitor()
mon.run_tests()

