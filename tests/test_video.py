import numpy as np
import pytest
from pynanny.video import VideoManager

rtsp_url = "http://195.196.36.242/mjpg/video.mjpg"


def test_get_frame():
    man = VideoManager(rtsp_url)
    man.start()
    frame = man.read()
    assert isinstance(frame, np.ndarray)
