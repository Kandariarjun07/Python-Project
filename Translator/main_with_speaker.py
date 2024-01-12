from tkinter import *
from tkinter import ttk
from googletrans import Translator
from gtts import gTTS
import os
from PIL import Imagae, ImageTk

class MyTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Arjun's Translator")

        self.source_lang_var = StringVar()
        self.target_lang_var = StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Source language section
        source_label = Label(self.root, text="Source Language:")
        source_label.grid(row=0, column=0, padx=10, pady=10)

        source_languages = sorted(['Bengali', 'Gujarati', 'Hindi', 'Kannada', 'Malayalam', 'Marathi', 'Nepali', 'Punjabi', 'Sindhi', 'Tamil', 'Telugu', 'Urdu', 'English'])
        self.source_lang_dropdown = ttk.Combobox(self.root, textvariable=self.source_lang_var, values=source_languages)
        self.source_lang_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Input text with speaker icon
        input_label = Label(self.root, text="Input Text:")
        input_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.input_text = Entry(self.root, width=40)
        self.input_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        speaker_icon = ImageTk.PhotoImage(Image.open("speaker.png"))  
        self.source_speaker_button = Button(self.root, image=speaker_icon, command=self.speak_source_text)
        self.source_speaker_button.image = speaker_icon
        self.source_speaker_button.grid(row=2, column=2, padx=10, pady=10, sticky="e")

        # Image section
        divide_image = ImageTk.PhotoImage(Image.open("divider_image.png"))
        divide_label = Label(self.root, image=divide_image)
        divide_label.image = divide_image
        divide_label.grid(row=0, rowspan=3, column=3, padx=10, pady=10, sticky="ns")

        # Output text with speaker icon
        output_label = Label(self.root, text="Output Text:")
        output_label.grid(row=1, column=4, columnspan=2, padx=10, pady=10, sticky="w")

        self.output_text = Entry(self.root, width=40, state="readonly")
        self.output_text.grid(row=2, column=4, columnspan=2, padx=10, pady=10, sticky="w")

        self.target_speaker_button = Button(self.root, image=speaker_icon, command=self.speak_target_text)
        self.target_speaker_button.image = speaker_icon
        self.target_speaker_button.grid(row=2, column=6, padx=10, pady=10, sticky="e")

        # Target language section
        target_label = Label(self.root, text="Target Language:")
        target_label.grid(row=0, column=4, padx=10, pady=10)

        target_languages = sorted(['Bengali', 'Gujarati', 'Hindi', 'Kannada', 'Malayalam', 'Marathi', 'Nepali', 'Punjabi', 'Sindhi', 'Tamil', 'Telugu', 'Urdu', 'English'])
        self.target_lang_dropdown = ttk.Combobox(self.root, textvariable=self.target_lang_var, values=target_languages)
        self.target_lang_dropdown.grid(row=0, column=5, padx=10, pady=10)

        # Translate button
        translate_button = Button(self.root, text="Translate", command=self.translate_text)
        translate_button.grid(row=3, column=0, columnspan=7, pady=10)

    def translate_text(self):
        translator = Translator()

        source_lang = self.get_lang_code(self.source_lang_var.get())
        target_lang = self.get_lang_code(self.target_lang_var.get())

        input_text = self.input_text.get()

        if input_text and source_lang and target_lang:
            translation = translator.translate(input_text, src=source_lang, dest=target_lang)
            self.output_text.config(state="normal")
            self.output_text.delete(0, END)
            self.output_text.insert(0, translation.text)
            self.output_text.config(state="readonly")

    def speak_source_text(self):
        text_to_speak = self.input_text.get()
        lang_code = self.get_lang_code(self.source_lang_var.get())
        self.speak_text(text_to_speak, lang_code)

    def speak_target_text(self):
        text_to_speak = self.output_text.get()
        lang_code = self.get_lang_code(self.target_lang_var.get())
        self.speak_text(text_to_speak, lang_code)

    def speak_text(self, text, lang_code):
        try:
            tts = gTTS(text, lang=lang_code, slow=False)
            audio_file = 'output.mp3'
            tts.save(audio_file)
            os.system(f'start {audio_file}')
        except ValueError:
            print('Invalid input. Please enter text.')

    def get_lang_code(self, lang_name):
        lang_mapping = {'Bengali': 'bn', 'Gujarati': 'gu', 'Hindi': 'hi', 'Kannada': 'kn', 'Malayalam': 'ml',
                        'Marathi': 'mr', 'Nepali': 'ne', 'Punjabi': 'pa', 'Sindhi': 'sd', 'Tamil': 'ta',
                        'Telugu': 'te', 'Urdu': 'ur', 'English': 'en'}
        return lang_mapping.get(lang_name, None)

if __name__ == "__main__":
    root = Tk()
    app = MyTranslatorApp(root)
    root.mainloop()
