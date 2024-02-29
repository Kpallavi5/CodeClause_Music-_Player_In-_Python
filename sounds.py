from tkinter import *
from tkinter import filedialog
import pygame
import os


root =Tk()
root.title('Music Player')
root.geometry("500x500")

#Initialze Pygame mixer
pygame.mixer.init()


#Add Song Function
def add_song():
 
    song = filedialog.askopenfilename(initialdir='/Audio', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))


    #Stripe out the Directory info and .mp3 extension from the song name
    song=song.replace("F:/Coldeclause/Music_player/Audio", "")
    song=song.replace(".mp3","")


    #Add song to listbox
    song_box.insert(END ,song)
#Add many Songs to Playlist    
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='/Audio', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))

    #Loop Thru song list and replace Directory info and mp3
    for song in songs:
         song=song.replace("F:/Coldeclause/Music_player/Audio", "")
         song=song.replace(".mp3","")

         #Insert into Playlist
         song_box.insert(END,song)




#Play selected song    
def play():
    # Get the selected song from the listbox
    song_index = song_box.curselection()
    if song_index:
        song = song_box.get(song_index)
        # Construct the full path to the song file
        song_path = f'F:/Coldeclause/Music_player/Audio/{song}.mp3'
        # Load and play the song
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()



  
#Stop selected song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

# Play The Next Song in the Playlist
def next_song():
    #Get the current song tuple number
    next_one = song_box.curselection() 
    # Add  one to the current song number
    next_one = next_one[0]+1
    # Grab song title from playlist
    song = song_box.get(next_one)
    song_path = f'F:/Coldeclause/Music_player/Audio/{song}.mp3'
    # Load and play the song
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    # Clear active bar in Playlist listbox
    song_box.selection_clear(0,END)
    # Activate bar in Playlist listbox
    song_box.activate(next_one)
    
    #Set Active Bar to Next Song
    song_box.selection_set(next_one , last =None)

# Play The Previous  Song in the Playlist
def previous_song():
     #Get the current song tuple number
    next_one = song_box.curselection() 
    # Add  one to the current song number
    next_one = next_one[0]-1
    # Grab song title from playlist
    song = song_box.get(next_one)
    song_path = f'F:/Coldeclause/Music_player/Audio/{song}.mp3'
    # Load and play the song
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    # Clear active bar in Playlist listbox
    song_box.selection_clear(0,END)
    # Activate bar in Playlist listbox
    song_box.activate(next_one)
    
    #Set Active Bar to Next Song
    song_box.selection_set(next_one , last =None)

 



# Create Global Pause Variable
global paused
paused =False    
# Pause and unpause The Current Song
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        #Unpause
        pygame.mixer.music.unpause()
        paused= False
    else:
        #Pause
        pygame.mixer.music.pause() 
        paused = True
     


    
       


   


#Create Playlist Box
song_box=Listbox(root,bg="black",fg="green",width =60,selectbackground="white",selectforeground="black")
song_box.pack(pady=20)

#Define Player Control Button Images
back_btn_img=PhotoImage(file='F:/Coldeclause/Music_player/Images/backward.png')
play_btn_img=PhotoImage(file='F:/Coldeclause/Music_player/Images/play.png')
forward_btn_img=PhotoImage(file='F:/Coldeclause/Music_player/Images/forward.png')
pause_btn_img=PhotoImage(file='F:/Coldeclause/Music_player/Images/pause.png')
stop_btn_img=PhotoImage(file='F:/Coldeclause/Music_player/Images/stop.png')

 # Change the subsample factors as needed
back_btn_img_resized = back_btn_img.subsample(1, 2) 
play_btn_img_resized = play_btn_img.subsample(1, 2)
forward_btn_img_resized = forward_btn_img.subsample(1, 2)
pause_btn_img_resized = pause_btn_img.subsample(1, 2)
stop_btn_img_resized = stop_btn_img.subsample(1, 2)


#Create Player Control Frame
controls_frame=Frame(root)
controls_frame.pack()

#Create Player Control Buttons
back_button=Button(controls_frame, image=back_btn_img,borderwidth=0,command=previous_song)
play_button=Button(controls_frame,image=play_btn_img,borderwidth=0,command=play)
forward_button=Button(controls_frame,image=forward_btn_img,borderwidth=0,command = next_song)
pause_button=Button(controls_frame,image=pause_btn_img,borderwidth=0,command=lambda: pause(paused))
stop_button=Button(controls_frame,image=stop_btn_img,borderwidth=0, command= stop)

back_button.grid(row=0,column=0,padx=10)
play_button.grid(row=0,column=1,padx=10)
forward_button.grid(row=0,column=2,padx=10)
pause_button.grid(row=0,column=3,padx=10)
stop_button.grid(row=0,column=4,padx=10)

#Create Menu
my_menu=Menu(root)
root.config(menu=my_menu)

#Add add Song Menu
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Add songs", menu =add_song_menu)
# add_song_menu.add_command(label="Add One Song To Playlist",command=add_song_menu )
add_song_menu.add_command(label="Add One Song To Playlist",command=add_song)

#Add many song 
add_song_menu.add_command(label="Add Many Song To Playlist",command=add_many_songs)

root.mainloop()


































