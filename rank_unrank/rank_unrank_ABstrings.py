# -*- coding: utf-8 -*-
# Template di soluzione per il problema rank_unrank_ABstrings

import sys

# INIZIO area entro la quale ti richiediamo/consigliamo di operare.

def ABstring2rank(s):
    count = 0
    exp = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'B':
            count = count + (2**exp)
        exp += 1
    return count

def ABstring_of_len_and_rank(length, r):
    if length == 0:
        return 'A'
    result = ""
    while r != 0:
        if r % 2 == 1:
            result = 'B' + result
            r = (r - 1)/2
        else:
            result = 'A' + result
            r = r/2
    diff = length - len(result)
    while diff > 0:
        result = 'A' + result
        diff = length - len(result)
    return result

# FINE area entro la quale ti richiediamo/consigliamo di operare.

input_string = input()

if input_string[0] == 'A' or input_string[0] == 'B':
   print(ABstring2rank(input_string))
else:
   length, r = input_string.split()
   print(ABstring_of_len_and_rank(int(length), int(r)))

