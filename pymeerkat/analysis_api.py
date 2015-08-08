import requests
import re
import json
import os
import subprocess as sp
from PIL import Image
import datetime
import speech_recognition as sr

# Data Analysis extends the MeerkatAPI class
class MeerkatAnalysisAPI(MeerkatAPI):

    def live_stream_to_text(self, broadcast_id, audio_dir, duration):
        """
        Returns a string of text from the audio processed.
        """
        self.save_live_stream_audio(broadcast_id, audio_dir, duration)

        audio_path = os.path.join(audio_dir, broadcast_id + '.mp3')

        # Read from the file being created
        r = sr.Recognizer()
        with sr.WavFile(audio_path) as source:              # use "test.wav" as the audio source
            audio = r.record(source)                        # extract audio data from the file

        try:
            list = r.recognize(audio,True)                  # generate a list of possible transcriptions
            print("Possible transcriptions:")
            for prediction in list:
                print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
        except LookupError:                                 # speech is unintelligible
            print("Could not understand audio")

        return prediction['text']