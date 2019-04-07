from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser

def get_conf(filename='conf.ini'):
	parser=ConfigParser()
	parser.read(filename)

	conf={}
	section='mysql'
	if parser.has_section(section):
		items=parser.items(section)
		for key, value in items:
			conf[key]=value
	
	return conf

def make_connection(ini_file='conf.ini'):
	conf=get_conf(ini_file)	
	try:
		conn=MySQLConnection(**conf)
		if conn.is_connected():
			print("MariaDB is connected")
	except 	Error as e:
		print(e)
	
	return conn


