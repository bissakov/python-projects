#Reverse a String
#Enter a string and the program will reverse it and print it out.

class ReverseString():
    def __init__(self, text_string):
        self.text_string = text_string

    def get_reversed_pythonic(self) -> str:
        return self.text_string[::-1]

    def get_reversed_long(self) -> str:
        reversed = ''
        for i in range(len(self.text_string) - 1, -1, -1):
            reversed += self.text_string[i]
        return reversed

    def get_reversed_list_comprehension(self) -> str:
        return ''.join([self.text_string[i] for i in range(len(self.text_string) - 1, -1, -1)])

def main():
    rev = ReverseString('fklasjflkasd')
    print(rev.get_reversed_pythonic() + '\tPythonic way')
    print(rev.get_reversed_long() + '\tReverse loop')
    print(rev.get_reversed_list_comprehension() + '\tList comprehension')

if __name__ == '__main__':
    main()