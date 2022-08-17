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
        for ch in self.text:
            try:
                self.counter[ch] += 1
            except (KeyError):
                continue

    def get_total(self) -> int:
        total = 0
        for val in self.counter.values():
            total += val
        return total

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