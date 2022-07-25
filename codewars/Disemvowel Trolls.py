https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

# 내 풀이: 문자열의 각 문자를 리스트 안의 값과 비교하고 제거한다.  
def disemvowel(string_):
    a=['a','e','i','o','u','A','E','I','O','U']
    for i in range(len(a)):
        string_= string_.replace(a[i],'')
    return string_

# 다른 풀이 1
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

# 다른 풀이 2
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s       # 이 풀이 좋다..!

# 다른 풀이 3
import re
def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)

# 다른 풀이 4
def disemvowel(string):
    return string.translate(None, 'aeiouAEIOU')

# 다른 풀이 5
def disemvowel(str2handle):
    vowel_character = ["a", "A", "e", "E", "o", "O", "i", "I", "u", "U"]
    str2return = ""
    i = 0
    n = len(str2handle)
    while i < n:
        if not str2handle[i] in vowel_character:
            str2return += str2handle[i]
        i += 1
    return str2return

# 다른 풀이 6
def disemvowel(string):
    result = ""
    for i in range(0, len(string)):
        c = string[i]
        if c == 'A':
            continue
        if c == 'E':
            continue
        if c == 'I':
            continue
        if c == 'O':
            continue
        if c == 'U':
            continue
        if c == 'a':
            continue
        if c == 'e':
            continue
        if c == 'i':
            continue
        if c == 'o':
            continue
        if c == 'u':
            continue
        result += c
    return result

# 다른 풀이 7
import re

def disemvowel(string):
    return re.sub(r"[aeiouAEIOU]", "", string)

# 다른 풀이 8
def disemvowel(string):
        
    s = ""
    for c in string:
        if c.lower() not in "aeiou":
            s += c
    return s
