#!/usr/bin/env python
import helper
from novaclient.v1_1.client import servers
import time, uuid


def main():
	client = helper.get_client()	
	for i in range(1,6):
		createTorqueServer(client)
	#deleteServer(client)
	monitorServers(client)
		
def createTorqueServer(client=None):
	image = getImage(client)
	flavor = getFlavor(client)
	key_name = "minnesota"
	id = str(uuid.uuid1())
	
	servers = client.servers
	
	name = "Torque_"+id
	createServer(servers, name, image, flavor, key_name)
			
def createServer(servers=None, name=None, image=None, flavor=None, key_name=None):
		servers.create(name=name,image=image, flavor=flavor, key_name=key_name)
		print "Server Created: " + name
		
def deleteServer(client=None):
	# Iterate through all of the servers and delete them
	servers = client.servers
	serverList = servers.list()
	
	for server in serverList:
		servers.delete(server)
		print "Deleting server"
	
def listServers(servers=None):
	# Print out the current list of servers
	serverList = servers.list()
	for server in serverList:
		print server
		
def getImage(client=None):
	# Fetch the Ubuntu 12.04 image and return it
	ubuntu_1204 = client.images.get(48335)
	return ubuntu_1204
	
def getFlavor(client=None):
	# Fetch the XSmall flavor type
	xsmall = client.flavors.get(100)
	return xsmall
	
def monitorServers(client=None):
	while True:
		serverList = client.servers.list()
		serverCount = len(serverList)
		if serverCount < 5:
			print "Create a new server"
			createTorqueServer(client)
		else:
			print "Doing nothing"
		time.sleep(5)
		
if __name__ == '__main__':
	main()