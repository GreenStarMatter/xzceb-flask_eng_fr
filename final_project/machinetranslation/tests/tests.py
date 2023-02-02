import unittest
from machinetranslation import translator
#from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):

    def test_frenchToEnglish_bounjour(self):
        french_word = 'Bonjour'
        expected_english_word = 'Hello'
        translated_english_word = translator.french_to_english(french_word)
        assert(translated_english_word == expected_english_word)

    def test_frenchToEnglish_merci(self):
        french_word = 'Merci'
        expected_english_word = 'Thank you'
        translated_english_word = translator.french_to_english(french_word)
        assert(translated_english_word == expected_english_word)

    def test_frenchToEnglish_empty(self):
        french_word = ''
        expected_english_word = ''
        translated_english_word = translator.french_to_english(french_word)
        assert(translated_english_word == expected_english_word)

    def test_englishToFrench_hello(self):
        english_word = 'Hello'
        expected_french_word = 'Bonjour'
        translated_french_word = translator.english_to_french(english_word)
        assert(translated_french_word == expected_french_word)

    def test_englishToFrench_thankyou(self):
        english_word = 'Thank you'
        expected_french_word = 'Je vous remercie'
        translated_french_word = translator.english_to_french(english_word)
        assert(translated_french_word == expected_french_word)

    def test_englishToFrench_empty(self):
        english_word = ''
        expected_french_word = ''
        translated_french_word = translator.english_to_french(english_word)
        assert(translated_french_word == expected_french_word)

if __name__ == "__main__":
    unittest.main()