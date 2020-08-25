from playsound import playsound
from functools import partial
import tkinter as tk
import os, sys

local_file = os.path.join(sys.path[0])
song_local = local_file + '/songs/'
song_list = os.listdir(local_file + '/songs/')

# function that opens the interface for playing songs
def view_songs():
    count = len(song_list)
    listing = tk.Tk(); listing.title('Song List')
    f1 = tk.Frame(master = listing,
                  relief = tk.RAISED,
                  borderwidth = 5
                  );f1.pack()
    def play(x):
            song_name = button[x].cget('text')
            playsound(song_local + song_name, False)

    button = list()
    for i, song in zip(range(count), song_list):
        buttom_name = 'b'+str(i)
        
        button.append(tk.Button(master = f1,
                                 width = 30,
                                 height = 1,
                                 text = song_list[i],
                                 command = partial(play,i)))
        button[-1].grid(row = i, column = 1)
  
    
# function that opens the menu of the program
def menu():

    def close():
        main.destroy()

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