import pygame
import tkinter as tk
from tkinter import filedialog


pygame.mixer.init()


def load_file():
    global filename
    filename = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3*.wav")])
    if filename:
        pygame.mixer.music.load(filename)
        
        


def play_music():
    if filename:
        pygame.mixer.music.play()
        
        
def pause_music():
    pygame.mixer.music.pause()
    
    
def resume_music():
    pygame.mixer.music.unpause()
    

def stop_music():
    pygame.mixer.music.stop()
    
    
root  = tk.Tk()
root_title=("Audio player")
root.geometry("300x200")

btn_load = tk.Button(root, text = "Загрузить", command = load_file)
btn_load.pack(pady=5)

btn_play = tk.Button(root, text="Играть", command=play_music)
btn_play.pack(pady=5)

btn_pause = tk.Button(root, text="Пауза", command=pause_music)
btn_pause.pack(pady=5)

btn_resume = tk.Button(root, text="Продолжить", command=resume_music)
btn_resume.pack(pady=5)

btn_stop = tk.Button(root, text="Остановить", command=stop_music)
btn_stop.pack(pady=5)

# Запуск главного цикла
root.mainloop()