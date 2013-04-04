#!/usr/bin/env python
import os
from novaclient.v1_1 import client

def get_client():
	username = os.getenv('NOVA_USERNAME')
	tenant_name = os.getenv('NOVA_PROJECT_ID')
	password = os.getenv('NOVA_PASSWORD')
	auth_url = os.getenv('NOVA_URL')
	return client.Client(username=username,
                         api_key=password,
                         project_id=tenant_name,
                         auth_url=auth_url)
