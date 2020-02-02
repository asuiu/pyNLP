#!/usr/bin/env python
# coding:utf-8
# Author: ASU --<andrei.suiu@gmail.com>
# Purpose: 
# Created: 4/19/2016
import re
from abc import ABCMeta, abstractmethod

from pyxtension.streams import slist

__author__ = 'ASU'

creReplaceNLs = re.compile(r'[\n\r\t\s]+')


class TextTokenizer(object, metaclass=ABCMeta):
    @abstractmethod
    def tokenizeText(self, text):
        pass


class DefaultTextTokenizer(TextTokenizer):
    def __init__(self):
        # Initializing TreeBank tokenizer from NLTK
        from nltk.tokenize import TreebankWordTokenizer
        self._tb_tokenizer = TreebankWordTokenizer().tokenize
        # Initializing Punkt Sentence Tokenizer from NLTK
        from nltk import data
        self._sent_detector = data.load('tokenizers/punkt/english.pickle')

    def tokenizeText(self, text):
        """
        Uses a sentence tokenizer, and tokenize obtained sentences with a TreeBank tokenizer.
        Replace unnormal quotes.
        :param text:
        :type text: str | unicode
        :rtype: slist
        """
        sentences = self.__tokenizeToSentences(text)
        tokens = slist()
        for sent in sentences:
            sent = creReplaceNLs.sub(r' ', sent)
            tokens.extend(self._tb_tokenizer(
                    sent))  # Tokenize sentences using TreeBank tokenizer initialized upper in the __init__ function
        return tokens

    def __tokenizeToSentences(self, text):
        text = re.sub(r'[`\x92\x91]', r"'", text)
        text = re.sub(r'[\x93\x94\x95\x96\x85\xE9]', r'"', text)
        text = re.sub(r'[\x80-\xFF]', r' ', text)
        text = re.sub(r"([:\s])\'(.+?)\'([\s\.])", r'\1"\2"\3', text)

        sentences = self._sent_detector.tokenize(text.strip())
        return sentences
