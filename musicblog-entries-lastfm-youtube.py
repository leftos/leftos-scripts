from Tkinter import Tk

stime = raw_input("Time: ")
f = open("list.txt", "w")
while stime != "":
	artist = raw_input("Artist: ")
	title = raw_input("Title: ")
	artist_y = str.replace(artist, "&", "%26")
	title_y = str.replace(title, "&", "%26")
	msg = stime + r' | <a href="http://last.fm/music/' + artist_y + r'">' + artist + r'</a> - <a href="http://www.youtube.com/results?search_query=' + artist_y + " " + title_y + r'&search_type=&aq=f">' + title + '</a><br />'
	f.write(msg + '\n')
	stime = raw_input("\nTime: ")
f.close
	