### check update.md for info
# jps
**A  simple Python Program that translate EN spelling into JP**
the project comes with three different types of running it
 1. as a pkg aka module
 ~~2. Source code~~
 ~~3. The already built file which is jps .exe~~
 # 1. as a pkg aka module (default)
 - you can download in the main branch
 # examples

```py
import jpspkg
print(jpspkg.hiragana("ko n ni chi wa"))
```
if you wanna use both
## or
```py
from jpspkg import hiragana
print(hiragana("ko n ni chi wa"))
```
if you want to use hiragana only
```py
from jpspkg import katakana
print(katakana("ko n ni chi wa"))
```
if you want to use katakana only
#
# 2. using the reverse method to translate from jp 2 en

# examples
```py
import reversepkg
print(reversepkg.hiragana("こんにちは"))
```
if you wanna use both
## or
```py
from reversepkg import hiragana
print(hiragana("こんにちは"))
```
if you want to use hiragana only
```py
from reversepkg import katakana
print(katakana("コンニチワ"))
```

if you like this repo Dont forget to give it a star
[![Star](https://img.shields.io/github/stars/username/repo.svg?style=social&label=Star)](https://github.com/catlomao/jps)
