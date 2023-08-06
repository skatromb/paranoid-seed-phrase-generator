#!/usr/local/bin/python
import os
from mnemonic import Mnemonic

OUTPUT_FOLDER = "output"
if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)
mnemo = Mnemonic("english")
words = mnemo.generate(strength=256)
with open('output/words.txt', 'w') as text_file:
    text_file.write(words)

print(f"""
Seed phrase created under `./{OUTPUT_FOLDER}`.
Now let's make encrypted zip-file.

Enter password for encryption"""
)
