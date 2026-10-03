
import re

text = "abab ab a"
pat = r"(ab)+"

print(re.findall(pat, text))

## (ab)+ → Capturing group; findall() returns ['ab', 'ab'].

## (?:ab)+ → Non-capturing group; findall() returns ['abab', 'ab'].

## ab+ → Matches a followed by one or more b characters.

