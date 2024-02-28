import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

# Set up the music player window
music_player = tkr.Tk()
music_player.title("ScorpionTaj - Music Player")
music_player.geometry("450x350")

# Function to initialize the music directory
def initialize_directory():
    directory = askdirectory()
    os.chdir(directory)
    song_list = os.listdir()
    for item in song_list:
        play_list.insert(tkr.END, item)

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

# Function to play the selected song
def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()

# Function to stop the currently playing song
def stop():
    pygame.mixer.music.stop()

# Function to pause the currently playing song
def pause():
    pygame.mixer.music.pause()

# Function to unpause the paused song
def unpause():
    pygame.mixer.music.unpause()

# Create buttons for control
Button1 = tkr.Button(music_player, text="PLAY", command=play, bg="blue", fg="white")
Button2 = tkr.Button(music_player, text="STOP", command=stop, bg="red", fg="white")
Button3 = tkr.Button(music_player, text="PAUSE", command=pause, bg="purple", fg="white")
Button4 = tkr.Button(music_player, text="UNPAUSE", command=unpause, bg="orange", fg="white")

# Create a label to display the currently playing song
var = tkr.StringVar()
song_title = tkr.Label(music_player, textvariable=var)

# Create a listbox to display the available songs
play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='light ellow', selectmode=tkr.SINGLE)

# Initialize the music directory
initialize_directory()

# Pack the widgets into the window
song_title.pack(pady=10)
Button1.pack(fill="x", pady=5)
Button2.pack(fill="x", pady=5)
Button3.pack(fill="x", pady=5)
Button4.pack(fill="x", pady=5)
play_list.pack(fill="both", expand="yes", padx=20, pady=10)

# Start the music player
music_player.mainloop()
