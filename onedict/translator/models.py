from __future__ import unicode_literals

from django.db import models
from textblob import Word

# Create your models here.


class EnglishWordDictManager(models.Manager):
    """Manager for English Word Dict
    """
    def add_word_to_db(self, word, definitions):
        """
        :param word:
        :param definitions:
        :return:
        """
        word_obj = self.create(word=word)
        for definition in definitions:
            word_obj.definitions.create(definition=definition)

    def is_word_exist(self, word):
        """
        :param word:
        :return:
        """
        try:
            word_obj = self.get(word=word)
            definition = word_obj.definitions.all()[0]
            return definition.definition
        except EnglishWordDict.DoesNotExist:
            return False

    def translate_word(self, word, to="en"):
        """Translate word to specified language
        :return:
        """
        if to == "en":
            word = Word(word)
            return word.definitions
        else:
            NotImplementedError("Need to implement translator support for %s" % to)


class EnglishWordDict(models.Model):
    """Model for storing English word and their definitions
    """
    objects = EnglishWordDictManager()

    word = models.CharField(max_length=20, unique=True)
    definitions = models.ManyToManyField('WordDefinitions', related_name="word_definitions")
    created_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.word


class WordDefinitions(models.Model):
    """Model for storing english word definitions
    """
    definition = models.CharField(max_length=50)

    def __unicode__(self):
        return self.definition
