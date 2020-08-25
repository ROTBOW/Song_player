from playsound import playsound
import tkinter as tk

def close():
    main.destroy()

# function that opens the interface for playing songs
def view_songs():
    slist = open('songlist.txt', 'r');song = slist.read();songs = song.split('\n')
    slist.close()
    count = len(songs)
    main.destroy(); listing = tk.Tk(); listing.title('Song List')
    f1 = tk.Frame(master = listing,
                  relief = tk.RAISED,
                  borderwidth = 5
                  );f1.pack()
    for i in range(count):
        l1 = tk.Label(master = f1, width = 20, height = 1, relief = tk.SOLID,
                      text = songs[i], borderwidth = 1)
        l1.grid(row = i, column = 0)
    b1 = tk.Button(master = f1, width = 30, height = 1, text = 'Play')
    b1.grid(row = 0, column = 1)
    
    def play_song1(event):
        playsound('song_1.mp3', False)
    b1.bind('<Button-1>', play_song1)
    
    b2 = tk.Button(master = f1, width = 30, height = 1, text = 'Play')
    b2.grid(row = 1, column = 1)
    
    def play_song2(event):
        playsound('song_2.mp3', False)
    b2.bind('<Button-1>', play_song2)
  
    
# function that opens the menu of the program
def menu():

    main = tk.Tk(); main.title('Bear Music Player')

    f1 = tk.Frame(master = main,
                  relief = tk.RAISED,
                  borderwidth = 5,
                  );f1.pack()

    l1 = tk.Label(master = f1,
                  width = 50,
                  height = 20,
                  text = 'Welcome\nWhat would you like to do?'
                  ); l1.pack(side = 'top', fill = tk.X)

    b1 = tk.Button(master = f1,
                   width = 25,
                   height = 3,
                   text = 'Songs',
                   relief = tk.RAISED,
                   borderwidth = 3,
                   command = view_songs,
                   ); b1.pack(side = 'left', fill = tk.BOTH)

    b2 = tk.Button(master = f1,
                   width = 25,
                   height = 3,
                   text = 'escape',
                   relief = tk.RAISED,
                   borderwidth = 3,
                   command = close,
                   ); b2.pack(side = 'right', fill = tk.BOTH)
    main.mainloop()

if __name__ == "__main__":
    menu()