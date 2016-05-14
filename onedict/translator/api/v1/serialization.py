"""Serialization for translator views
"""
from rest_framework import serializers


class WordTranslatorSerializer(serializers.Serializer):
    """Serializer for WordTranslator
    """
    translated_word = serializers.CharField(required=True)
