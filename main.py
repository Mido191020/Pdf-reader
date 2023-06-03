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

    root = tk.Tk()
    text_widget = tk.Text(root, height=20, width=70)
    text_widget.pack()

    def speak():
        global player  # Access the global player variable
        player = pyttsx3.init()
        player.setProperty('rate', 150)  # Adjust the speech rate (change the value as desired)
        voices = player.getProperty('voices')
        player.setProperty('voice', voices[0].id)  # Select the first available voice (change index as desired)

        for num in range(pages):
            page = pdfreader.pages[num]
            text = page.extract_text()
            player.say(text)
            player.runAndWait()

    def stop():
        global player  # Access the global player variable
        if player is not None:
            player.stop()
        root.quit()  # Quit the Tkinter application

    # Add a colored welcome message
    welcome_message = "Welcome to the PDF Audiobook Player!\n\nThis application allows you to turn PDF files into audio books.\n\nSit back, relax, and enjoy listening to your favorite books.\n\nDeveloped by Mido Tarek."

    # Customizing the font settings
    font_family = "Arial"
    font_size = 16
    font_weight = "bold"
    font_style = "italic"

    # Applying the formatted text and font settings
    text_widget.tag_configure("welcome", foreground="blue", font=(font_family, font_size, font_weight, font_style))
    text_widget.insert(tk.END, welcome_message, "welcome")

    btn_speak = ttk.Button(root, text="Speak", command=speak)
    btn_stop = ttk.Button(root, text="Exit", command=stop)

    btn_speak.pack()
    btn_stop.pack()

    root.protocol("WM_DELETE_WINDOW", stop)  # Handle window close event
    root.mainloop()

play_pdf()
