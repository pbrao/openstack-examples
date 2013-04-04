#!/usr/bin/env python
import helper
from novaclient.v1_1.client import servers


def main():
	client = helper.get_client()
	createServer(client)
	#deleteServer(client)
	
def createServer(client=None):
	servers = client.servers
	print "Before Server List"
	print "------------------"
	listServers(servers)
	print "------------------"
	
	image = getImage(client)
	flavor = getFlavor(client)
	
	for i in range(1,6):
		servers.create("Torque_"+str(i),image, flavor, key_name="minnesota")
		print "Torque_"+str(i)+" server created."
	
	servers = client.servers
	print "After Server List"
	print "-----------------"
	listServers(servers)
	print "-----------------"

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
	
def getIPAddress(servers=None):
	"""docstring for getIPAddress"""
	serverList = servers.list()
	
	
def pingServer(servers=None):
	"""docstring for pingServer"""
	pass
	
if __name__ == '__main__':
	main()