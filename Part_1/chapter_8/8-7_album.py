def make_album(artist_name, album_title, tracks=''):
	if tracks:
		album = {'artist': artist_name.title(), 'title' : album_title.title(), 'tracks' : tracks}
	else:
		album = {'artist': artist_name.title(), 'title' : album_title.title()}
	return album
	
album1 = make_album('michael jackson', 'thriller')
album2 = make_album('ac/dc', 'back in black')
album3 = make_album('pink floyd', 'the dark side of the moon', '10')
print(album1)
print(album2)
print(album3)
