import requests
import json
import os
import subprocess as sp
from PIL import Image
import datetime
import pdb

API_VERSION = '1.0'

# Define class for API connection
class MeerkatAPI(object):
	# some constants

	def __init__(self,api_key): 
		"""
		Initialize the API using the API key of the user
		"""
		self.API_KEY = api_key
		self.headers = {'Authorization' : self.API_KEY}
	
	###############################################
	############## HELPER FUNCTIONS ###############
	###############################################

	def http_response(self,res,print_flag=True):
		"""
		Helper to do something with http response 
		"""
		if res.raise_for_status() == None:
			print "Response was a success with code: %d" % res.status_code
			if print_flag: 
				print json.dumps(res.json()['result'],indent=4,separators=(',',': '))


	def get_image_summary(self,image): 
		"""
		Helper to generate an image caption using CNN+RNN Generator
		"""

	###############################################
	############## GENERAL FUNCTIONS ##############
	###############################################

	def get_routes(self,print_flag=True):
		"""
		Get all possible commands for the API
		"""
		url = 'https://api.meerkatapp.co/routes?v=%s' % API_VERSION
		result = sp.check_output(["curl","--request", 'GET', url, '--header', 'Authorization:%s' % self.API_KEY])
		result = json.loads(result)
		print json.dumps(result,indent=4,separators=(',',': '))
		return result

	def get_leaderboard(self,print_flag=True): 
		"""
		Get the top broadcasting users from around the world.
		"""
		url = 'https://resources.meerkatapp.co/users/leaderboard?v=%s' % API_VERSION
		response = requests.get(url,headers=self.headers)
		self.http_response(response,print_flag)
		return response.json()['result']

	###############################################
	################# BROADCASTS ##################
	###############################################

	def get_live_broadcasts(self,print_flag=True):
		"""
		Get all live broadcasts from around the world
		"""
		url = 'https://resources.meerkatapp.co/broadcasts?v=%s' % API_VERSION
		response = requests.get(url,headers=self.headers)
		self.http_response(response,print_flag)
		return response.json()['result']

	def get_scheduled_broadcasts(self,print_flag=True):
		"""
		Get all broadcasts scheduled to air 
		"""
		url = 'https://resources.meerkatapp.co/schedules?v=%s' % API_VERSION
		response = requests.get(url,headers=self.headers)
		self.http_response(response,print_flag)
		return response.json()['result']

	def get_broadcast_summary(self,broadcast_id,print_flag=True):
		"""
		Get user-generated summary of broadcast
		"""
		url = 'https://resources.meerkatapp.co/broadcasts/%s/summary?v=%s' % (str(broadcast_id),API_VERSION)
		response = requests.get(url,headers=self.headers)
		self.http_response(response,print_flag)
		return response.json()['result']

	def get_broadcast_watchers(self,broadcast_id,print_flag=True):
		"""
		Get all users watching this broadcast
		"""
		url = 'https://resources.meerkatapp.co/broadcasts/%s/watchers?v=%s' % (str(broadcast_id),API_VERSION)
		response = requests.get(url,headers=self.headers)
		self.http_response(response,print_flag)
		return response.json()['result']

	def get_broadcast_restreams(self,broadcast_id,print_flag=True):
		"""
		Get all restreams of this broadcast
		"""
		url = 'https://channels.meerkatapp.co/broadcasts/%s/restreams?v=%s' % (str(broadcast_id),API_VERSION)
		response = requests.get(url,headers=self.headers)
		self.http_response(response,print_flag)
		return response.json()['result']

	def get_broadcast_likes(self,broadcast_id,print_flag=True):
		"""
		Get all likes for this broadcast
		"""
		url = 'https://channels.meerkatapp.co/broadcasts/%s/likes?v=%s' % (str(broadcast_id),API_VERSION)
		response = requests.get(url,headers=self.headers)
		self.http_response(response,print_flag)
		return response.json()['result']

	def get_broadcast_comments(self,broadcast_id,print_flag=True):
		"""
		Get all comments for this broadcast
		"""
		url = 'https://channels.meerkatapp.co/broadcasts/%s/comments?v=%s' % (str(broadcast_id),API_VERSION)
		response = requests.get(url,headers=self.headers)
		self.http_response(response,print_flag)
		return response.json()['result']

	def get_broadcast_activities(self,broadcast_id,print_flag=True):
		"""
		Get all activities for this broadcast
		"""
		url = 'https://resources.meerkatapp.co/broadcasts/%s/activities?v=%s' % (str(broadcast_id),API_VERSION)
		response = requests.get(url,headers=self.headers)
		self.http_response(response,print_flag)
		return response.json()['result']

	def get_broadcast_auto_summary(self,broadcast_id):
		"""
		Get auto-generated summary from image + context using deep learning for broadcast
		"""

	##########################################
	########### STREAM PROCESSING ############
	##########################################

	def get_broadcast_stream_link(self,broadcast_id):
		"""
		Construct the stream link from the broadcast id
		"""
		return 'http://cdn.meerkatapp.co/broadcast/' + str(broadcast_id) + '/live.m3u8' 


	# Change to save image stream - and specify location to save
	def save_live_stream(self, broadcast_id, delay_milliseconds, output_dir, display=True): 
		"""
		save the image stream (video) with the given delay between frames
		"""
		import cv2
		import numpy as np

		broadcast_summary = self.get_broadcast_summary(broadcast_id,print_flag=False)

		VIDEO_URL = self.get_broadcast_stream_link(broadcast_id)

		fps = float(1000)/delay_milliseconds

		if display: # display window only if specified
			cv2.startWindowThread()
			cv2.namedWindow(broadcast_summary['caption'],cv2.CV_WINDOW_AUTOSIZE)

		pipe = sp.Popen([ 'ffmpeg', "-i", VIDEO_URL,
		           "-loglevel", "quiet", # no text output
		           "-an",   # disable audio
		           "-f", "image2pipe",
		           "-r", str(fps),
		           "-pix_fmt", "bgr24",
		           "-vcodec", "rawvideo", "-"],
		           stdin = sp.PIPE, stdout = sp.PIPE)
		
		# create image directory IF NOT present
		if not os.path.exists(output_dir): 
			os.mkdir(output_dir)

		# create broadcast directory IF NOT present
		if not os.path.exists(os.path.join(output_dir,broadcast_id)):
			os.mkdir(os.path.join(output_dir,broadcast_id))
		image_save_path = os.path.join(output_dir,broadcast_id)

		while True:
		    raw_image = pipe.stdout.read(360*640*3) # read 360*640*3 bytes (= 1 frame)
		    image =  np.fromstring(raw_image, dtype='uint8').reshape((640,360,3))

		    pil_img = Image.fromarray(image)
		    # save image with timestamp
		    pil_img.save(os.path.join(image_save_path,datetime.datetime.now().isoformat()+'.png'))

		    if display: # display only if specified
			    cv2.imshow("test",image)
			    if cv2.waitKey(delay_milliseconds) == 27:
			        break


	# Add more options to live stream link (no audio, different intervals etc.)
	def play_live_stream(self,broadcast_id):
		""" 
		Play live stream using ffplay (if installed)
		"""
		VIDEO_URL = self.get_broadcast_stream_link(broadcast_id)
		sp.call(['ffplay',VIDEO_URL])


	def kill_live_stream(self):
		"""
		Destroy any remaining cv2 windows
		"""
		import cv2
		cv2.destroyAllWindows()


	###############################################
	################### USERS #####################
	###############################################

	def get_user_profile(self, user_id,print_flag=True):
		"""
		Get profile for the given user
		"""
		url = 'https://resources.meerkatapp.co/users/%s/profile?v=%s' % (str(broadcast_id),API_VERSION) 
		response = requests.get(url,self.headers)
		self.http_response(response,print_flag)
		return response.json()['result']


