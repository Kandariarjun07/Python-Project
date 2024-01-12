from googletrans import Translator

class GoogleTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate_text(self, input_text, source_lang, target_lang):
        source_lang_code = self.get_lang_code(source_lang)
        target_lang_code = self.get_lang_code(target_lang)

        if source_lang_code and target_lang_code:
            translation = self.translator.translate(input_text, src=source_lang_code, dest=target_lang_code)
            return translation.text
        else:
            return "Invalid language selection."

    def get_lang_code(self, lang_name):
        lang_mapping = {'Bengali': 'bn', 'Gujarati': 'gu', 'Hindi': 'hi', 'Kannada': 'kn', 'Malayalam': 'ml',
                        'Marathi': 'mr', 'Nepali': 'ne', 'Punjabi': 'pa', 'Sindhi': 'sd', 'Tamil': 'ta',
                        'Telugu': 'te', 'Urdu': 'ur', 'English': 'en'}
        return lang_mapping.get(lang_name, None)

if __name__ == "__main__":
    translator = GoogleTranslator()

    # Take input, source language, and target language from the user
    input_text = input("Enter the text to translate: ")
    source_language = input("Enter the source language: ")
    target_language = input("Enter the target language: ")

    translated_text = translator.translate_text(input_text, source_language, target_language)
    print(f"Translated text: {translated_text}")
