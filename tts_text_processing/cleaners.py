""" adapted from https://github.com/keithito/tacotron """

'''
清洁器是在训练和评估时对输入文本运行的转换。

可以通过将以逗号分隔的清洁器名称列表作为"cleaners"超参数来选择清洁器。一些清洁器是特定于英语的。通常情况下，你会想使用：
1. "english_cleaners" 用于英语文本
2. "transliteration_cleaners" 用于非英语文本，可以使用Unidecode库将其转换为ASCII（https://pypi.python.org/pypi/Unidecode）
3. "basic_cleaners" 如果你不想进行转录（在这种情况下，你还应该更新symbols.py中的符号以匹配你的数据）。
'''

import re
from string import punctuation
from functools import reduce
from unidecode import unidecode


# 正则表达式匹配空格：
_whitespace_re = re.compile(r'\s+')

# 用于清洁的正则表达式，用大括号括起来的单词进行分隔
_arpa_re = re.compile(r'{[^}]+}|\S+')


def lowercase(text):
    return text.lower()


def collapse_whitespace(text):
    return re.sub(_whitespace_re, ' ', text)


def separate_acronyms(text):
    text = re.sub(r"([0-9]+)([a-zA-Z]+)", r"\1 \2", text)
    text = re.sub(r"([a-zA-Z]+)([0-9]+)", r"\1 \2", text)
    return text


def convert_to_ascii(text):
    return unidecode(text)


def dehyphenize_compound_words(text):
    text = re.sub(r'(?<=[a-zA-Z0-9])-(?=[a-zA-Z])', ' ', text)
    return text


def remove_space_before_punctuation(text):
    return re.sub(r"\s([{}](?:\s|$))".format(punctuation), r'\1', text)


class Cleaner(object):
    def __init__(self, cleaner_names, phonemedict):
        self.cleaner_names = cleaner_names
        self.phonemedict = phonemedict

    def __call__(self, text):
        for cleaner_name in self.cleaner_names:
            sequence_fns, word_fns = self.get_cleaner_fns(cleaner_name)
            for fn in sequence_fns:
                text = fn(text)

            text = [reduce(lambda x, y: y(x), word_fns, split)
                    if split[0] != '{' else split
                    for split in _arpa_re.findall(text)]
            text = ' '.join(text)
        text = remove_space_before_punctuation(text)
        return text

    def get_cleaner_fns(self, cleaner_name):
        if cleaner_name == 'English_cleaners':
            sequence_fns = [lowercase, collapse_whitespace]
            word_fns = []
        else:
            raise Exception("{} cleaner not supported".format(cleaner_name))

        return sequence_fns, word_fns
