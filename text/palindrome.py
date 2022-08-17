#Check if Palindrome
#Checks if the string entered by the user is a palindrome.
#That is that it reads the same forwards as backwards like “racecar”

class Palindrome():
    def __init__(self, *words):
        self.words = []
        for w in words:
            if isinstance(w, list):
                self.words.extend(w)
                continue
            self.words.append(w)

    def is_palindrome(self, word) -> bool:
        return word == word[::-1]

    def print(self) -> None:
        for word in self.words:
            print(f'"{word}" {"is" if self.is_palindrome(word) else "is not"} a palindrome')

def main():
    word1 = 'racecar'
    word2 = 'lkfjsdlk'
    word3 = 'aba'
    words = ['utotu', 'ewrqo', 'abracadabra']
    pal = Palindrome(word1, word2, word3, words)
    pal.print()

if __name__ == '__main__':
    main()