import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class GoogleTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Google Translator")

        self.source_lang_var = tk.StringVar()
        self.target_lang_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Source language dropdown
        source_label = ttk.Label(self.root, text="Source Language:")
        source_label.grid(row=0, column=0, padx=10, pady=10)

        source_languages = sorted(['Bengali', 'Gujarati', 'Hindi', 'Kannada', 'Malayalam', 'Marathi', 'Nepali', 'Punjabi', 'Sindhi', 'Tamil', 'Telugu', 'Urdu', 'English'])
        self.source_lang_dropdown = ttk.Combobox(self.root, textvariable=self.source_lang_var, values=source_languages)
        self.source_lang_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Target language dropdown
        target_label = ttk.Label(self.root, text="Target Language:")
        target_label.grid(row=1, column=0, padx=10, pady=10)

        target_languages = sorted(['Bengali', 'Gujarati', 'Hindi', 'Kannada', 'Malayalam', 'Marathi', 'Nepali', 'Punjabi', 'Sindhi', 'Tamil', 'Telugu', 'Urdu', 'English'])
        self.target_lang_dropdown = ttk.Combobox(self.root, textvariable=self.target_lang_var, values=target_languages)
        self.target_lang_dropdown.grid(row=1, column=1, padx=10, pady=10)

        # Input text
        input_label = ttk.Label(self.root, text="Input Text:")
        input_label.grid(row=2, column=0, padx=10, pady=10)

        self.input_text = tk.Entry(self.root, width=40)
        self.input_text.grid(row=2, column=1, padx=10, pady=10)

        # Output text
        output_label = ttk.Label(self.root, text="Output Text:")
        output_label.grid(row=3, column=0, padx=10, pady=10)

        self.output_text = tk.Entry(self.root, width=40, state="readonly")
        self.output_text.grid(row=3, column=1, padx=10, pady=10)

        # Translate button
        translate_button = ttk.Button(self.root, text="Translate", command=self.translate_text)
        translate_button.grid(row=4, column=0, columnspan=2, pady=10)

    def translate_text(self):
        translator = Translator()

        source_lang = self.get_lang_code(self.source_lang_var.get())
        target_lang = self.get_lang_code(self.target_lang_var.get())

        input_text = self.input_text.get()

        if input_text and source_lang and target_lang:
            translation = translator.translate(input_text, src=source_lang, dest=target_lang)
            self.output_text.config(state="normal")
            self.output_text.delete(0, tk.END)
            self.output_text.insert(0, translation.text)
            self.output_text.config(state="readonly")

    def get_lang_code(self, lang_name):
        lang_mapping = {'Bengali': 'bn', 'Gujarati': 'gu', 'Hindi': 'hi', 'Kannada': 'kn', 'Malayalam': 'ml',
                        'Marathi': 'mr', 'Nepali': 'ne', 'Punjabi': 'pa', 'Sindhi': 'sd', 'Tamil': 'ta',
                        'Telugu': 'te', 'Urdu': 'ur', 'English': 'en'}
        return lang_mapping.get(lang_name, None)

if __name__ == "__main__":
    root = tk.Tk()
    app = GoogleTranslatorApp(root)
    root.mainloop()
