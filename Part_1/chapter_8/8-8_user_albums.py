def make_album(artist_name, album_title, tracks=''):
	if tracks:
		album = {'artist': artist_name.title(), 'title' : album_title.title(), 'tracks' : tracks}
	else:
		album = {'artist': artist_name.title(), 'title' : album_title.title()}
	return album

while True:
	print("\nPlease enter your favorite album name and its artist name")
	print("(enter 'q' at any time to quit)")
	
	artist = input("Artist name: ")
	if artist == 'q':
		break
	
	album = input("Album name: ")
	if album == 'q':
		break
	
	favorite_music = make_album(artist, album)
	print(favorite_music)
		
	
