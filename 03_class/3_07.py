import mp3

s1 = mp3.Song('Song1', "Singer1", 5)
s2 = mp3.Song('Song2', "Singer2", 4)
s3 = mp3.Song('Song3', "Singer3", 2)
s4 = mp3.Song('Song4', "Singer4", 3)
s5 = mp3.Song('Song5', "Singer5", 1)
'''
s1.printSongInfo()
s2.printSongInfo()
s3.printSongInfo()
s4.printSongInfo()
s5.printSongInfo()
'''
my = mp3.Player()

my.addSong(s1)
my.addSong(s2)
my.addSong(s3)
my.addSong(s4)
my.addSong(s5)


my.suffle()
my.play()
