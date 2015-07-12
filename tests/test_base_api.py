"""
Test cases for the base_api.py file
"""
# Import generic libraries
import unittest

# Add relevant dirs to the sys path
import env

# Import library to test
import base_api

API_VERSION = '1.0'
# Read API_KEY from 'my_api_key' in 'tests/' directory
with open('my_api_key', 'rb') as f:
    API_KEY = f.readline()

MEERKAT_API = base_api.MeerkatAPI(API_KEY)

# Global test vars
TEST_HEADER = {'Authorization': API_KEY}
TEST_CODE = 200


class MeerkatAPITests(unittest.TestCase):
    """
    Test class with test cases for the MeerkatAPI class
    """
    # Test methods that use the HTTP requests library

    def test_get_leaderboard(self):
        """
        Tests get_leaderboard() function
        """
        # Set url for this function
        test_url = MEERKAT_API.leaderboard_url + '?v=%s' % API_VERSION

        # Execute the actual code and get status code
        called_header = MEERKAT_API.headers
        called_code, called_url, _ = MEERKAT_API.get_leaderboard(print_flag=False)

        # verify the results
        self.assertEqual(called_header, TEST_HEADER)
        self.assertEqual(called_code, TEST_CODE)
        self.assertEqual(called_url, test_url)

    def test_get_live_broadcasts(self):
        """
        Test for get_live_broadcasts()
        """
        # Set url for this function
        test_url = MEERKAT_API.live_now_url + '?v=%s' % API_VERSION

        # Execute the actual code and get status code
        called_header = MEERKAT_API.headers
        called_code, called_url, _ = MEERKAT_API.get_live_broadcasts(print_flag=False)

        # verify the results
        self.assertEqual(called_header, TEST_HEADER)
        self.assertEqual(called_code, TEST_CODE)
        self.assertEqual(called_url, test_url)

    def test_get_scheduled_broadcasts(self):
        """
        Test for get_scheduled_broadcasts()
        """
        # Set url for this function
        test_url = MEERKAT_API.scheduled_streams_url + '?v=%s' % API_VERSION

        # Execute the actual code and get status code
        called_header = MEERKAT_API.headers
        called_code, called_url, _ = MEERKAT_API.get_scheduled_broadcasts(print_flag=False)

        # verify the results
        self.assertEqual(called_header, TEST_HEADER)
        self.assertEqual(called_code, TEST_CODE)
        self.assertEqual(called_url, test_url)

    def test_get_broadcast_summary(self):
        """
        Test for get_broadcast_summary(broadcast_id)
        """
        # Get the first broadcast id from most recent live broadcast
        broadcast_id = MEERKAT_API.get_live_broadcasts(print_flag=False)[2][0]['id']

        # Set url for this function
        test_url = MEERKAT_API.stream_summary_template_url.replace(
            '{broadcastId}',
            str(broadcast_id)) + '?v=%s' % API_VERSION

        # Execute the actual code and get status code
        called_header = MEERKAT_API.headers
        called_code, called_url, _ = MEERKAT_API.get_broadcast_summary(
            broadcast_id,
            print_flag=False)

        # verify the results
        self.assertEqual(called_header, TEST_HEADER)
        self.assertEqual(called_code, TEST_CODE)
        self.assertEqual(called_url, test_url)

    def test_get_broadcast_watchers(self):
        """
        Test for get_broadcast_watchers(broadcast_id)
        """
        # Get the first broadcast id from most recent live broadcast
        broadcast_id = MEERKAT_API.get_live_broadcasts(print_flag=False)[2][0]['id']

        # Set url for this function
        test_url = MEERKAT_API.broadcast_watchers_url.replace(
            '{broadcastId}',
            str(broadcast_id)) + '?v=%s' % API_VERSION

        # Execute the actual code and get status code
        called_header = MEERKAT_API.headers
        called_code, called_url, _ = MEERKAT_API.get_broadcast_watchers(
            broadcast_id,
            print_flag=False)

        # verify the results
        self.assertEqual(called_header, TEST_HEADER)
        self.assertEqual(called_code, TEST_CODE)
        self.assertEqual(called_url, test_url)

    def test_get_broadcast_restreams(self):
        """
        Test for get_broadcast_restreams(broadcast_id)
        """
        # Get the first broadcast id from most recent live broadcast
        broadcast_id = MEERKAT_API.get_live_broadcasts(print_flag=False)[2][0]['id']

        # Set url for this function
        test_url = MEERKAT_API.broadcast_restreams_url.replace('{broadcastId}',str(broadcast_id)) + '?v=%s' % API_VERSION

        # Execute the actual code and get status code
        called_header = MEERKAT_API.headers
        called_code, called_url, _ = MEERKAT_API.get_broadcast_restreams(broadcast_id, print_flag=False)

        # verify the results
        self.assertEqual(called_header, TEST_HEADER)
        self.assertEqual(called_code, TEST_CODE)
        self.assertEqual(called_url, test_url)

    def test_get_broadcast_likes(self):
        """
        Test for get_broadcast_likes(broadcast_id)
        """
        # Get the first broadcast id from most recent live broadcast
        broadcast_id = MEERKAT_API.get_live_broadcasts(print_flag=False)[2][0]['id']

        # Set url for this function
        test_url = MEERKAT_API.broadcast_likes_url.replace(
            '{broadcastId}',
            str(broadcast_id)) + '?v=%s' % API_VERSION

        # Execute the actual code and get status code
        called_header = MEERKAT_API.headers
        called_code, called_url, _ = MEERKAT_API.get_broadcast_likes(broadcast_id, print_flag=False)

        # verify the results
        self.assertEqual(called_header, TEST_HEADER)
        self.assertEqual(called_code, TEST_CODE)
        self.assertEqual(called_url, test_url)

    def test_get_broadcast_comments(self):
        """
        Test for get_broadcast_comments(broadcast_id)
        """
        # Get the first broadcast id from most recent live broadcast
        broadcast_id = MEERKAT_API.get_live_broadcasts(print_flag=False)[2][0]['id']

        # Set url for this function
        test_url = MEERKAT_API.broadcast_comments_url.replace(
            '{broadcastId}',
            str(broadcast_id)) + '?v=%s' % API_VERSION

        # Execute the actual code and get status code
        called_header = MEERKAT_API.headers
        called_code, called_url, _ = MEERKAT_API.get_broadcast_comments(
            broadcast_id,
            print_flag=False)

        # verify the results
        self.assertEqual(called_header, TEST_HEADER)
        self.assertEqual(called_code, TEST_CODE)
        self.assertEqual(called_url, test_url)

    def test_get_broadcast_activities(self):
        """
        Test for get_broadcast_activities(broadcast_id)
        """
        # Get the first broadcast id from most recent live broadcast
        broadcast_id = MEERKAT_API.get_live_broadcasts(print_flag=False)[2][0]['id']

        # Set url for this function
        test_url = MEERKAT_API.broadcast_activities_url.replace(
            '{broadcastId}',
            str(broadcast_id)) + '?v=%s' % API_VERSION

        # Execute the actual code and get status code
        called_header = MEERKAT_API.headers
        called_code, called_url, _ = MEERKAT_API.get_broadcast_activities(
            broadcast_id,
            print_flag=False)

        # verify the results
        self.assertEqual(called_header, TEST_HEADER)
        self.assertEqual(called_code, TEST_CODE)
        self.assertEqual(called_url, test_url)

    def test_get_broadcast_stream_link(self):
        """
        Test for get_broadcast_stream_link(broadcast_id)
        """
        # Get the first broadcast id from most recent live broadcast
        broadcast_id = MEERKAT_API.get_live_broadcasts(print_flag=False)[2][0]['id']

        # test url
        test_link = 'http://cdn.meerkatapp.co/broadcast/' + str(broadcast_id) + '/live.m3u8'

        # Execute code to get link
        called_link = MEERKAT_API.get_broadcast_stream_link(broadcast_id)
        self.assertEqual(called_link, test_link)

    def test_get_user_profile(self):
        """
        Test for get_user_profile(user_id)
        """
        # Get the first user id from leaderboard
        user_id = MEERKAT_API.get_leaderboard(print_flag=False)[2][0]['id']

        # Set url for this function
        test_url = MEERKAT_API.profile_url.replace('{userId}', str(user_id)) + '?v=%s' % API_VERSION

        # Execute the actual code and get status code
        called_header = MEERKAT_API.headers
        called_code, called_url, _ = MEERKAT_API.get_user_profile(user_id, print_flag=False)

        # verify the results
        self.assertEqual(called_header, TEST_HEADER)
        self.assertEqual(called_code, TEST_CODE)
        self.assertEqual(called_url, test_url)

    # # Test method that saves the live stream as images.
    # def test_save_live_stream():
    #   # check number of files in the directory
        # pass
if __name__ == '__main__':
    unittest.main()
