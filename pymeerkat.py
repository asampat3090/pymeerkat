import requests
import json

API_KEY = '0d35d995e1b14f72868cadae539a2789'
API_VERSION = '1.0'

headers = {'Authorization' : API_KEY}

def http_response(res):
	if res.raise_for_status() == None:
		print "Response was a success with code: %d" % res.status_code
		print json.dumps(res.json()['result'],indent=4,separators=(',',': '))

def get_routes():
	url = 'http://api.meerkatapp.co/routes?v=%s' % API_VERSION
	response = requests.get(url,headers)
	http_response(response)
	return response.json()['result']

def get_leaderboard(): 
	url = 'https://resources.meerkatapp.co/users/leaderboard?v=%s' % API_VERSION
	response = requests.get(url,headers)
	http_response(response)
	return response.json()['result']

def get_live_broadcasts():
	url = 'https://resources.meerkatapp.co/broadcasts?v=%s' % API_VERSION
	response = requests.get(url,headers)
	http_response(response)
	return response.json()['result']

def get_scheduled_broadcasts():
	url = 'https://resources.meerkatapp.co/schedules?v=%s' % API_VERSION
	response = requests.get(url,headers)
	http_response(response)
	return response.json()['result']

def get_broadcast_summary(broadcast_id):
	url = 'https://resources.meerkatapp.co/broadcasts/%s/summary?v=%s' % (str(broadcast_id),API_VERSION)
	response = requests.get(url,headers)
	http_response(response)
	return response.json()['result']

def get_broadcast_watchers(broadcast_id):
	url = 'https://resources.meerkatapp.co/broadcasts/%s/watchers?v=%s' % (str(broadcast_id),API_VERSION)
	response = requests.get(url,headers)
	http_response(response)
	return response.json()['result']

def get_broadcast_restreams(broadcast_id):
	url = 'https://channels.meerkatapp.co/broadcasts/%s/restreams?v=%s' % (str(broadcast_id),API_VERSION)
	response = requests.get(url,headers)
	http_response(response)
	return response.json()['result']

def get_broadcast_likes(broadcast_id):
	url = 'https://channels.meerkatapp.co/broadcasts/%s/likes?v=%s' % (str(broadcast_id),API_VERSION)
	response = requests.get(url,headers)
	http_response(response)
	return response.json()['result']

def get_broadcast_comments(broadcast_id):
	url = 'https://channels.meerkatapp.co/broadcasts/%s/comments?v=%s' % (str(broadcast_id),API_VERSION)
	response = requests.get(url,headers)
	http_response(response)
	return response.json()['result']

def get_broadcast_activities(broadcast_id):
	url = 'https://resources.meerkatapp.co/broadcasts/%s/activities?v=%s' % (str(broadcast_id),API_VERSION)
	response = requests.get(url,headers)
	http_response(response)
	return response.json()['result']

def get_user_profile(user_id):
	url = 'https://resources.meerkatapp.co/users/%s/profile?v=%s' % (str(broadcast_id),API_VERSION) 
	response = requests.get(url,headers)
	http_response(response)
	return response.json()['result']

