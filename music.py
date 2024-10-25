import pygame.mixer
import os
from pynput import keyboard

pygame.mixer.init();

class audioManager:
	def __init__(self):
		self.musics = []
		self.index = 0
		self._pause = False
		self.volume = 1
	def load(self, path):
		for f in os.listdir(path):
			if os.path.isfile(f"{path}/{f}") and f[0] != "_":
				self.musics.append(pygame.mixer.Sound(f"{path}/{f}"))
	def play(self):
		self.musics[self.index].play(-1)
	def pause(self):
		if self._pause:
			pygame.mixer.unpause()
		else:
			pygame.mixer.pause()
		self._pause = not self._pause
	def next(self):
		self.musics[self.index].stop()
		self.index = (self.index+1)%len(self.musics)
		self.musics[self.index].play(-1)
	def previous(self):
		self.musics[self.index].stop()
		self.index = (self.index-1)%len(self.musics)
		self.musics[self.index].play(-1)
	def set_volume(self):
		self.musics[self.index].set_volume(self.volume)
	def volume_up(self):
		self.volume = min(self.volume+0.1, 1)
		self.set_volume()
	def volume_down(self):
		self.volume = min(self.volume-0.1, 1)
		self.set_volume()


audio = audioManager()
audio.load("music")
audio.play()
audio.set_volume()

def release(key):
	if key == keyboard.Key.media_play_pause or key == keyboard.Key.pause:
		audio.pause()
	elif key == keyboard.Key.media_next:
		audio.next()
	elif key == keyboard.Key.media_previous:
		audio.previous()
	elif key == keyboard.Key.f10:
		audio.volume_down()
	elif key == keyboard.Key.f12:
		audio.volume_up()

with keyboard.Listener(on_release = release) as listner:
	listner.join()
