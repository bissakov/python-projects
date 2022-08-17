# Count Vowels
# Enter a string and the program counts the number of vowels in the text.
# For added complexity have it report a sum of each vowel found.

class Count_Vowels():
    def __init__(self, text):
        self.text = text
        self.counter = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'total': 0 }
        self.__count()
        self.counter['total'] = self.get_total()
    
    def __count(self) -> None:
        vowels = list(self.counter.keys())[:-1]
        for ch in self.text:
            if ch not in vowels:
                continue
            self.counter[ch] += 1

    def get_total(self) -> int:
        return sum(self.counter.values())

    def print_vowel_count(self) -> None:
        for key, val in self.counter.items():
            print(f'{key}:\t{val}')

def main():
    text = '''
        The Quick Response system became popular outside the automotive industry due
        to its fast readability and greater storage capacity compared to standard UPC barcodes.
        Applications include product tracking, item identification, time tracking, document management,
        and general marketing.
    '''
    cnt = Count_Vowels(text)
    cnt.print_vowel_count()

if __name__ == '__main__':
    main()