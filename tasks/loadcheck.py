#!/usr/bin/python

import os

class LoadCheck(object):
	def __init__(self, max_load = len(open("/proc/cpuinfo").read().split("processor"))):
		self.max_load = max_load
	def test(self):
		load = os.getloadavg()[0]
		if load > self.max_load:
			return False
		else:
			return True

	def action(self):

    		os.system("/etc/init.d/nginx stop")
    		os.system("/etc/init.d/apache2 stop")
    		os.system("/etc/init.d/mysql stop")

    		os.system("/etc/init.d/mysql start")
    		os.system("/etc/init.d/apache2 start")
    		os.system("/etc/init.d/nginx start")

    		os.system("/etc/init.d/varnish restart")
