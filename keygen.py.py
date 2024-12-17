import tkinter as tk
from tkinter import PhotoImage, Canvas
import winsound

def shift_characters(chars, shift):
    all_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result = ""
    for char in chars:
        if char in all_chars:
            new_index = (all_chars.index(char) + shift) % len(all_chars)
            result += all_chars[new_index]
        else:
            result += char
    return result

def generate_key():
    input_block = input_field.get().upper()
    if len(input_block) != 5 or not input_block.isalnum():
        output_label.config(text="Invalid Input! Enter 5 letters/numbers.")
        return
    
    second_block = shift_characters(input_block, 3)
    third_block = shift_characters(input_block, -5)
    final_key = f"{input_block}-{second_block}-{third_block}"
    
    key_output.delete(0, tk.END)
    key_output.insert(0, final_key)

    generate_button.config(bg="green")
    root.after(200, lambda: generate_button.config(bg="SystemButtonFace"))

# Play background music on loop
def play_music():
    winsound.PlaySound('music.wav', winsound.SND_ASYNC | winsound.SND_LOOP)

root = tk.Tk()
root.title("Keygen Program")
root.geometry("600x400")

# Start playing music when the program starts
play_music()

# Background image loading using PhotoImage (Ensure the file is in the same directory)
background_image = PhotoImage(file="background.png")  # Change to a PNG file
canvas = Canvas(root, width=600, height=400)
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
canvas.pack(fill="both", expand=True)

input_label = tk.Label(root, text="Enter First Block (5 chars):", font=("Arial", 12), bg="#ffffff")
canvas.create_window(300, 120, window=input_label)
input_field = tk.Entry(root, font=("Arial", 14), justify="center")
canvas.create_window(300, 150, window=input_field, width=200)

generate_button = tk.Button(root, text="Generate Key", font=("Arial", 14), command=generate_key)
canvas.create_window(300, 200, window=generate_button, width=150)

key_output = tk.Entry(root, font=("Courier", 16), justify="center")
canvas.create_window(300, 250, window=key_output, width=300)

output_label = tk.Label(root, text="", font=("Arial", 12), bg="#ffffff", fg="red")
canvas.create_window(300, 280, window=output_label)

root.mainloop()
