#! /usr/bin/env python3

import sys
from collections import OrderedDict
import random

word_list = [
        ['あ', 'a'], ['い', 'i'], ['う', 'u'], ['え', 'e'], ['お', 'o'],
        ['か', 'ka'], ['き', 'ki'], ['く', 'ku'], ['け', 'ke'], ['こ', 'ko'],
        ['さ', 'sa'], ['し', 'shi'], ['す', 'su'], ['せ', 'se'], ['そ', 'so'],
        ['た', 'ta'], ['ち', 'chi'], ['つ', 'tsu'], ['て', 'te'], ['と', 'to'],
        ['な', 'na'], ['に', 'ni'], ['ぬ', 'nu'], ['ね', 'ne'], ['の', 'no'],
        ['は', 'ha'], ['ひ', 'hi'], ['ふ', 'fu'], ['へ', 'he'], ['ほ', 'ho'],
        ['ま', 'ma'], ['み', 'mi'], ['む', 'mu'], ['め', 'me'], ['も', 'mo'],
        ['や', 'ya'], ['ゆ', 'yu'], ['よ', 'yo'],
        ['ら', 'ra'], ['り', 'ri'], ['る', 'ru'], ['れ', 're'], ['ろ', 'ro'],
        ['わ', 'wa'], ['を', 'o'], ['ん', 'n']]

if len(sys.argv) >= 2:
    num = int(sys.argv[1], 10)
else:
    num = len(word_list)

print(num)
print(sys.argv)

dct = dict(word_list[:num])
dct_keys = list(dct.keys())

while True:
    question = random.choice(dct_keys)
    print(question)
    response = input(':')
    answer = dct[question]
    if response == answer:
        print("correct")
    else:
        print("wrong, ans is %s" % answer)
