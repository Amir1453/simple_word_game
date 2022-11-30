import subprocess

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

english_words = load_words()

identity = list(input())
words = dict()

for word in english_words:
    if all(letter in word for letter in identity):
        words.update({len(word):word})

length = max(words.keys())
print(words[length])
copy2clip(words[length])