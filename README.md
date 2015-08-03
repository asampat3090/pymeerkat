# Pymeerkat: Python Wrapper for Meerkat API

![CircleCI build status shield master](https://circleci.com/gh/asampat3090/pymeerkat/tree/master.svg?style=shield&circle-token=c511560200c8c015b9eb3aae45d9da5c682f5e2a)
[![Documentation Status](https://readthedocs.org/projects/pymeerkat/badge/?version=latest)](http://pymeerkat.readthedocs.org)

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
See [docs](http://pymeerkat.readthedocs.org)

## License
The MIT License (MIT)

Copyright (c) 2015
