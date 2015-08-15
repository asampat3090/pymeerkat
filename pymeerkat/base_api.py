import requests
import re
import json
import os
import subprocess as sp
from PIL import Image
import datetime

API_VERSION = '1.0'


# Define class for API connection
class MeerkatAPI(object):

    ###############################################
    ############## HELPER FUNCTIONS ###############
    ###############################################

    def __http_response(self, url, print_flag=True):
        """
        Helper to do something with http response

        Input:
        res - response from requests.get function
        (optional) print_flag - print json result to stdout (default=True)

        Output:
        Response result as a tuple of (response status code, response url, JSON object).
        """

        try:
            res = requests.get(url, headers=self.headers)
            print "Response was a success with code: %d and url: %s" % (res.status_code, res.url)
            if print_flag and res.status_code != 401:
                print json.dumps(res.json()['result'], indent=4, separators=(', ', ': '))
            return (res.status_code, res.url, res.json()['result'])
        except requests.exceptions.RequestException as e:
            print(e)
            return (res.status_code, res.url, {})

    def get_routes(self, api_key, print_flag=True):
        """
        Get all possible commands for the API - use to keep API up-to-date

        Input:
        (optional) print_flag - print json result to stdout (default=True)

        Output:
        result - json object with keys as routes and values as url destination
        """
        url = 'https://api.meerkatapp.co/routes?v=%s' % API_VERSION
        while True:
            try:
                result = sp.check_output(["curl", "--request", 'GET', url, '--header', 'Authorization:%s' % api_key])
                result = json.loads(result)
                if print_flag:
                    print json.dumps(result, indent=4, separators=(', ', ': '))
                return result
            except:
                print "Failed request to API - calling it again..."
                continue

    ###############################################
    ########## INITIALIZATION FUNCTION ############
    ###############################################

    def __init__(self, api_key):
        """
        Initialize the API using the API key of the user

        Input:
        api_key - user's API key for the Meerkat API (can obtain @ http://developers.meerkatapp.co/)
        """
        self.API_KEY = api_key
        self.headers = {'Authorization': self.API_KEY}
        # set destination urls
        routes = self.get_routes(self.API_KEY, print_flag=False)
        converter = re.compile('((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))')
        for k, v in routes.iteritems():
            setattr(self, converter.sub(r'_\1', k).lower()+'_url', v)

    ###############################################
    ############## GENERAL FUNCTIONS ##############
    ###############################################

    def get_leaderboard(self, print_flag=True):
        """
        Get the top broadcasting users from around the world.

        Input:
        (optional) print_flag - print json result to stdout (default=True)

        Output:
        (response status code, response url, list of user JSON objects)
        """
        url = self.leaderboard_url + '?v=%s' % API_VERSION
        return self.__http_response(url, print_flag)

    ###############################################
    ################# BROADCASTS ##################
    ###############################################

    def get_live_broadcasts(self, print_flag=True):
        """
        Get all live broadcasts from around the world

        Input:
        (optional) print_flag - print json result to stdout (default=True)

        Output:
        (response status code, response url, list of live broadcast JSON objects)
        """
        url = self.live_now_url + '?v=%s' % API_VERSION
        return self.__http_response(url, print_flag)

    def get_scheduled_broadcasts(self, print_flag=True):
        """
        Get all broadcasts scheduled to air

        Input:
        (optional) print_flag - print json result to stdout (default=True)

        Output:
        (response status code, response url, list of scheduled broadcast JSON objects)
        """
        url = self.scheduled_streams_url + '?v=%s' % API_VERSION
        return self.__http_response(url, print_flag)

    def get_broadcast_summary(self, broadcast_id, print_flag=True):
        """
        Get user-generated summary of broadcast

        Input:
        broadcast_id - broadcast id as a string (combination of letters and numbers)
        (optional) print_flag - print json result to stdout (default=True)

        Output:
        (response status code, response url, summary of the given broadcast)
        """
        url = self.stream_summary_template_url.replace('{broadcastId}', str(broadcast_id)) + '?v=%s' % API_VERSION
        return self.__http_response(url, print_flag)

    def get_broadcast_watchers(self, broadcast_id, print_flag=True):
        """
        Get all users watching this broadcast

        Input:
        broadcast_id - broadcast id as a string (combination of letters and numbers)
        (optional) print_flag - print json result to stdout (default=True)

        Output:
        (response status code, response url, list of users watching given broadcast as JSON objects)
        """
        url = self.broadcast_watchers_url.replace('{broadcastId}', str(broadcast_id)) + '?v=%s' % API_VERSION
        return self.__http_response(url, print_flag)

    def get_broadcast_restreams(self, broadcast_id, print_flag=True):
        """
        Get all restreams of this broadcast

        Input:
        broadcast_id - broadcast id as a string (combination of letters and numbers)
        (optional) print_flag - print json result to stdout (default=True)

        Output:
        (response status code, response url, list of restreams of given broadcast as JSON objects)
        """
        url = self.broadcast_restreams_url.replace('{broadcastId}', str(broadcast_id)) + '?v=%s' % API_VERSION
        return self.__http_response(url, print_flag)

    def get_broadcast_likes(self, broadcast_id, print_flag=True):
        """
        Get all likes for this broadcast

        Input:
        broadcast_id - broadcast id as a string (combination of letters and numbers)
        (optional) print_flag - print json result to stdout (default=True)

        Output:
        (response status code, response url, list of likes for given broadcast as JSON objects)
        """
        url = self.broadcast_likes_url.replace('{broadcastId}', str(broadcast_id)) + '?v=%s' % API_VERSION
        return self.__http_response(url, print_flag)

    def get_broadcast_comments(self, broadcast_id, print_flag=True):
        """
        Get all comments for this broadcast

        Input:
        broadcast_id - broadcast id as a string (combination of letters and numbers)
        (optional) print_flag - print json result to stdout (default=True)

        Output:
        (response status code, response url, list of comments for given broadcast as JSON objects)
        """
        url = self.broadcast_comments_url.replace('{broadcastId}', str(broadcast_id)) + '?v=%s' % API_VERSION
        return self.__http_response(url, print_flag)

    def get_broadcast_activities(self, broadcast_id, print_flag=True):
        """
        Get all activities for this broadcast

        Input:
        broadcast_id - broadcast id as a string (combination of letters and numbers)
        (optional) print_flag - print json result to stdout (default=True)

        Output:
        (response status code, response url, list of activities for given broadcast as JSON objects)
        """
        url = self.broadcast_activities_url.replace('{broadcastId}', str(broadcast_id)) + '?v=%s' % API_VERSION
        return self.__http_response(url, print_flag)

    ##########################################
    ########### STREAM PROCESSING ############
    ##########################################

    def get_broadcast_stream_link(self, broadcast_id):
        """
        Construct the stream link from the broadcast id

        Input:
        broadcast_id - broadcast id as a string (combination of letters and numbers)

        Output:
        live streaming link as string
        """
        return 'http://cdn.meerkatapp.co/broadcast/' + str(broadcast_id) + '/live.m3u8'

    # Change to save image stream - and specify location to save
    def save_live_stream(self, broadcast_id, delay_milliseconds, num_images, output_dir, display=True):
        """
        Save the image stream (video) with the given delay between frames

        Input:
        broadcast_id - broadcast id as a string (combination of letters and numbers)
        delay_milliseconds - milliseconds of delay between sampled images from broadcast video
        num_images - number of total images to save
        output_dir - full path to output directory to store images
        (optional) display - show images as they are saved (default=True)
        """
        import cv2
        import numpy as np

        broadcast_summary = self.get_broadcast_summary(broadcast_id, print_flag=False)

        VIDEO_URL = self.get_broadcast_stream_link(broadcast_id)

        fps = float(1000)/delay_milliseconds

        if display:  # display window only if specified
            cv2.startWindowThread()
            cv2.namedWindow(broadcast_summary[2]['caption'], cv2.CV_WINDOW_AUTOSIZE)

        pipe = sp.Popen(['ffmpeg', "-i", VIDEO_URL,
                   "-loglevel", "quiet",  # no text output
                   "-an",  # disable audio
                   "-f", "image2pipe",
                   "-r", str(fps),
                   "-pix_fmt", "rgb24",
                   "-vcodec", "rawvideo", "-"],
                   stdin=sp.PIPE, stdout=sp.PIPE)

        # create image directory IF NOT present
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        # create broadcast directory IF NOT present
        if not os.path.exists(os.path.join(output_dir, broadcast_id)):
            os.mkdir(os.path.join(output_dir, broadcast_id))
        image_save_path = os.path.join(output_dir, broadcast_id)

        # save num_images to the output_dir
        img_index = 0
        while img_index < num_images:
            raw_image = pipe.stdout.read(360*640*3)  # read 360*640*3 bytes (= 1 frame)
            image = np.fromstring(raw_image, dtype='uint8').reshape((640, 360, 3))
            # convert to PIL image
            pil_img = Image.fromarray(image)
            # save image with timestamp
            pil_img.save(os.path.join(image_save_path, datetime.datetime.now().isoformat()+'.png'))
            # increment counter
            img_index += 1
            # display the image
            if display:  # display only if specified
                cv2.imshow("test", image)
                if cv2.waitKey(delay_milliseconds) == 27:
                    break

    def save_live_stream_audio(self, broadcast_id, audio_dir, duration):
        """
        Save the audio from the live stream in mp3 format

        Inputs:
        broadcast_id - broadcast id as a string (combination of letters and numbers)
        audio_dir - full path to output directory to store audio files
        duration - [hh:mm:ss] number of seconds you would like to capture video
        """
        broadcast_summary = self.get_broadcast_summary(broadcast_id, print_flag=False)

        VIDEO_URL = self.get_broadcast_stream_link(broadcast_id)

        audio_path = os.path.join(audio_dir, broadcast_id + '.wav')

        pipe = sp.Popen(['ffmpeg', "-i", VIDEO_URL,
                   "-loglevel", "quiet",  # no text output
                   "-vn",  # disable audio
                   "-f", "wav",
                   "-t", duration,  # record for time set in duration
                   audio_path],
                   stdin=sp.PIPE, stdout=sp.PIPE)

        return 1

    def play_live_stream(self, broadcast_id, audio=True, video=True):
        """
        Play live stream using ffplay (if installed):

        Input:
        broadcast_id - broadcast id as a string (combination of letters and numbers)
        (optional) audio - include audio when playing the live stream (default=True)
        (optional) video - include video when playing the live stream (defulat=True)

        Controls:
        q, ESC
        Quit.

        f
        Toggle full screen.

        p, SPC
        Pause.

        a
        Cycle audio channel in the current program.

        v
        Cycle video channel.

        t
        Cycle subtitle channel in the current program.

        c
        Cycle program.

        w
        Cycle video filters or show modes.

        s
        Step to the next frame.

        Pause if the stream is not already paused, step to the next video frame, and pause.

        left/right
        Seek backward/forward 10 seconds.

        down/up
        Seek backward/forward 1 minute.

        page down/page up
        Seek to the previous/next chapter. or if there are no chapters Seek backward/forward 10 minutes.

        mouse click
        Seek to percentage in file corresponding to fraction of width.
        """
        VIDEO_URL = self.get_broadcast_stream_link(broadcast_id)
        if not video:
            sp.call(['ffplay', VIDEO_URL, '-vn'])  # disable video
        elif not audio:
            sp.call(['ffplay', VIDEO_URL, '-an'])  # disable audio
        else:
            sp.call(['ffplay', VIDEO_URL])

    def kill_live_stream(self):
        """
        Destroy any remaining cv2 windows
        """
        import cv2
        cv2.destroyAllWindows()


    ###############################################
    ################### USERS #####################
    ###############################################
    def get_user_profile(self, user_id, print_flag=True):
        """
        Get profile for the given user

        Input:
        user_id - user id as a string (combination of letters and numbers)
        (optional) print_flag - print json result to stdout (default=True)

        Output:
        (response status code, response url, user info for given user id as JSON object)
        """
        url = self.profile_url.replace('{userId}', str(user_id)) + '?v=%s' % API_VERSION
        return self.__http_response(url, print_flag)

    # NOT AVAILBLE YET IN MEERKAT API
    # def get_user_streams(self, user_id, print_flag=True):
    #   """
    #   Get streams by the given user

    #   Input:
    #   user_id - user id as a string (combination of letters and numbers)
    #   (optional) print_flag - print json result to stdout (default=True)

    #   Output:
    #   list of user
    #   """
    #   url=self.user_streams_url.replace('{userId}', str(user_id)) + '?v=%s' % API_VERSION
    #   return self.__http_response(requests.get(url, self.headers), print_flag)
