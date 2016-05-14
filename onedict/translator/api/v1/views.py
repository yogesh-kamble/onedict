"""Viewset for translator
"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from translator.models import EnglishWordDict
from .serialization import WordTranslatorSerializer


class TranslatorView(ViewSet):
    """ViewSet for Translator
    """

    def list(self, request):
        """Get the word to be translated and return translation
        :param request:
        :return:
        """
        if "word" not in request.GET:
            return Response({"error": "word required to translate"}, status=status.HTTP_400_BAD_REQUEST)

        word = request.GET['word']
        word_definition = EnglishWordDict.objects.is_word_exist(word)
        if word_definition is False:
            word_definitions = EnglishWordDict.objects.translate_word(word)
            EnglishWordDict.objects.add_word_to_db(word, word_definitions)
            # For Now return only one definition
            word_definition = word_definitions[0]

        return_data = {"translated_word": word_definition}
        serializer_data = WordTranslatorSerializer(return_data)
        return Response(serializer_data.data, status=status.HTTP_200_OK)
