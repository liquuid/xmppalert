#!/usr/bin/python

import _mysql
import os

class MysqlCheck(object):
	def __init__(self, host, user, password, db):
		self.host=host
		self.user=user
		self.password=password
		self.db=db

	def test(self):
		try:
    			db=_mysql.connect(self.host, self.user, self.password, self.db)
    			db.close()
			return True 
		except:
			return False
