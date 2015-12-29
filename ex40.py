class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics 
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	
happy_bday = Song(["Happy birthday to you", 
					"I don,t wnat to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family", 
						"With pockets full of shells"])
						
lyrics = ["Hello", "Is it Me?", "SING!!"]

bulls_on_parade.sing_me_a_song()
hack = "print a song"

adele = Song(lyrics)
adele.sing_me_a_song()

hacker = Song(hack)
hacker.sing_me_a_song()