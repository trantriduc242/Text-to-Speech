import tkinter as tk
from gtts import gTTS
import os
from googletrans import Translator

def convert_to_speech_vietnamese():
    # Get the user input from the text box
    vietnamese_text = text_input.get()

    # Create a gTTS object for Vietnamese
    tts_vietnamese = gTTS(text=vietnamese_text, lang='vi')
    tts_vietnamese.save("vietnamese_speech.mp3")

    # Play the Vietnamese audio file (requires an external player)
    os.system("start vietnamese_speech.mp3")

def translate_to_english_and_speak():
    # Get the user input from the text box
    vietnamese_text = text_input.get()

    # Create a Translator object
    translator = Translator()

    # Translate Vietnamese text to English
    translated_text = translator.translate(vietnamese_text, src='vi', dest='en').text

    # Create a gTTS object for English
    tts_english = gTTS(text=translated_text, lang='en')
    tts_english.save("english_speech.mp3")

    # Play the English audio file (requires an external player)
    os.system("start english_speech.mp3")

# Create the main window
root = tk.Tk()
root.title("Vietnamese Text-to-Speech App")

# Create a label
label = tk.Label(root, text="Nhập thoại bằng Tiếng Việt vào ô bên dưới:")
label.pack()

# Create a text input box
text_input = tk.Entry(root, width=50)  # Set the desired width (in characters)
text_input.pack()

# Create a button to convert text to speech (Vietnamese)
convert_button_vietnamese = tk.Button(root, text="Tiếng Việt", command=convert_to_speech_vietnamese)
convert_button_vietnamese.pack()

# Create a button to translate Vietnamese text to English and speak
translate_button = tk.Button(root, text="Tiếng Anh", command=translate_to_english_and_speak)
translate_button.pack()

# Create a label to display status
status_label = tk.Label(root, text="")
status_label.pack()

# Run the GUI event loop
root.mainloop()
