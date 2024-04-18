""" adapted from https://github.com/keithito/tacotron """

'''
定义了模型输入中使用的符号集。
默认情况下是一组ASCII字符，适用于英语或经过Unidecode处理的文本。对于其他数据，你可以修改_characters。
'''

def get_symbols(symbol_set):
    if symbol_set == 'ukrainian':
        _punctuation = '\'.,?! '
        _special = '-'
        _letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        symbols = list(_letters + _special + _punctuation)
    else:
        raise Exception("{} symbol set does not exist".format(symbol_set))

    return symbols
