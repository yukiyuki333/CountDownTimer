# --coding:utf-8 --**

import os
from pydub import AudioSegment
from pydub.playback import play


song = AudioSegment.from_mp3("C:\\Users\sssss\PycharmProjects\CountdownTimer\\bgm.mp3")
play(song)