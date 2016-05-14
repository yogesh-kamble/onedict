from textblob import TextBlob, Word
from nltk.corpus import stopwords
import re

ENGLISH_STOPWORDS = set(stopwords.words('english'))
EXTRA_KEYWORD_REGEX = r"\"|\'|\.|\,"


class Text(object):
    """Class for Handling Text related tasks
    """
    def __init__(self, text):
        # JUST remove punctuation from text
        # TODO find out best way to do this using TextBlob only
        text = re.sub(EXTRA_KEYWORD_REGEX, "", text)
        self.text = TextBlob(text)

    @staticmethod
    def remove_stop_words(word_list):
        """Helper method to remove stop words from word list
        :param word_list: word list
        :type word_list: []
        :return: list with removed word
        :rtype: []
        """
        return set(word_list) - ENGLISH_STOPWORDS

    def process_text(self):
        """This will do end to end processing on text such as removing stop words etc
        :return:
        """
        pass

    def get_words_from_text(self):
        """This will remove stop words from text and remaining words return as list
        :return: Word List from Text
        :rtype: []
        """
        word_list = self.text.words
        clean_word_list = self.remove_stop_words(word_list.lower())
        return clean_word_list


class TextWordTranslator(object):
    """Class for handling translator related tasks
    """
    def __init__(self, word_list=None):
        self.word_list = word_list

    def translate_word(self, word, to="en"):
        """Translate word to specified language
        :return:
        """
        if to == "en":
            word = Word(word)
            return word.definitions()
        else:
            NotImplementedError("Need to implement translator support for %s"%to)

    def translate_word_list(self, to="en"):
        """Translate all word from list to specified language and return list
        :param to: Language
        :type to: str
        :return: list of translated words
        :rtype: []
        """
        translated_word_list = []
        for word in self.word_list:
            translated_word = self.translate_word(word)
            translated_word_list.append(translated_word)
        return translated_word
