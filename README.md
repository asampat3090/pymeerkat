# Pymeerkat: Python Wrapper for Meerkat API

(https://circleci.com/gh/asampat3090/pymeerkat.png?circle-token=c511560200c8c015b9eb3aae45d9da5c682f5e2a)

## Introduction
This projects is meant to aid python junkies to easily access the [Meerkat API](https://meerkatapp.co/developers).
In particular we aim to provide access to a stream of images for each broadcast for image processing/vision tasks.
Our goal is to enable people to utlize this information to come up with better heuristics to categorize streams.

## Python Dependencies (Verified on Install)
- requests
- Pillow

## External Dependencies
Make sure to install these before installing the package.

- ffmpeg
- opencv

Mac:
```bash
brew install ffmpeg opencv
```

Ubuntu:
```bash
sudo apt-get install ffmpeg opencv
```

## Installation

Run the following code

```bash
sudo python setup.py install
```

## What's New?
Nothing...this is v 0.1

## Usage

### get_leaderboard(print_flag = True)

### get_live_broadcasts(print_flag = True)

### get_scheduled_broadcasts(print_flag = True)

### get_broadcast_summary(broadcast_id, print_flag = True)

### get_broadcast_watchers(broadcast_id, print_flag = True)

### get_broadcast_restreams(broadcast_id, print_flag = True)

### get_broadcast_likes(broadcast_id, print_flag = True)

### get_broadcast_comments(broadcast_id, print_flag = True)

### get_broadcast_activities(broadcast_id, print_flag = True)

### get_broadcast_stream_link(broadcast_id)

### save_live_stream(broadcast_id, delay_milliseconds, num_images, output_dir, display = True)

### play_live_stream(broadcast_id, audio = True, video = True)

### kill_live_stream()

### get_user_profile(user_id, print_flag = True)

## License
The MIT License (MIT)

Copyright (c) 2015

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
