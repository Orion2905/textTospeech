#
# import pygame
# pygame.init()
# pygame.display.set_mode((200,100))
# pygame.mixer.music.load("x.MP3")
# pygame.mixer.music.play(0)
#
# clock = pygame.time.Clock()
# clock.tick(10)
# while pygame.mixer.music.get_busy():
#     pygame.event.poll()
#     clock.tick(10)

import pygame
from tkinter import *
import librosa
import time

import soundfile as sf
f = sf.SoundFile('2022-08-24135035496417.wav')
print('samples = {}'.format(f.frames))
print('sample rate = {}'.format(f.samplerate))
print('seconds = {}'.format(f.frames / f.samplerate))

seconds = f.frames / f.samplerate
converted_current_time = time.strftime('%M:%S', time.gmtime(seconds))
print(converted_current_time)
print(round(seconds) / 60)
