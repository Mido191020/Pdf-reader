import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import ttk

# Global variable for the pyttsx3 player
player = None

def play_pdf():
    book = askopenfilename()
    pdfreader = PdfReader(book)
    pages = len(pdfreader.pages)

    for num in range(pages):
        page = pdfreader.pages[num]
        text = page.extract_text()

        root = tk.Tk()
        text_widget = tk.Text(root, height=20, width=50)
        text_widget.pack()

        def speak():
            global player  # Access the global player variable
            player = pyttsx3.init()
            player.setProperty('rate', 150)  # Adjust the speech rate (change the value as desired)
            voices = player.getProperty('voices')
            player.setProperty('voice', voices[0].id)  # Select the first available voice (change index as desired)

            player.say(text)
            player.runAndWait()

        def stop():
            global player  # Access the global player variable
            if player is not None:
                player.stop()

        # Add a colored welcome message
        welcome_message = "Welcome to the PDF Audiobook Player!\n\nThis is Mido Tarek."
        text_widget.tag_configure("welcome", foreground="blue")  # Set the color of the tag

        # Display the welcome message
        text_widget.insert(tk.END, welcome_message, "welcome")  # Apply the tag to the welcome message

        btn_speak = ttk.Button(root, text="Speak", command=speak)
        btn_stop = ttk.Button(root, text="Stop", command=stop)

        btn_speak.pack()
        btn_stop.pack()

        root.mainloop()

play_pdf()
