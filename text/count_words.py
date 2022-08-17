#Count Words in a String
#Counts the number of individual words in a string.
#For added complexity read these strings in from a text file and generate a summary.

import re

class File_Reader():
    def __init__(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            self.text = f.read()

    def get_text(self) -> str:
        return self.text

class Word_Count():
    def __init__(self, text):
        self.words = self.split_text(text)

    def split_text(self, text) -> list:
        return re.findall(r'\w+', text)

    def get_word_count(self) -> int:
        return len(self.words)

    def get_unique_word_count(self) -> int:
        return len(dict.fromkeys(self.words))

    def print(self) -> None:
        print(f'Total word count: {self.get_word_count()}\nUnique word count: {self.get_unique_word_count()}')

def main():
    f_reader = File_Reader('misc_input/text.txt')
    
    cnt = Word_Count(f_reader.get_text())

    cnt.print()

if __name__ == '__main__':
    main()