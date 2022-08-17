# Fizz Buzz - Write a program that prints the numbers from x to y.
# But for multiples of three print “Fizz” instead of the number and
# for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

class FizzBuzz():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.res = ''

    def exec(self) -> None:
        for i in range(self.start, self.end + 1):
            res = ''
            if i % 3 == 0:
                res += 'FIZZ'
            if i % 5 == 0:
                res += 'BUZZ'
            if len(res) == 0:
                res += str(i)
            self.res += res + '\n'

    def get_result(self) -> str:
        return self.res

def main():
    fizzbuzz = FizzBuzz(1, 100)
    fizzbuzz.exec()
    print(fizzbuzz.get_result())

if __name__ == '__main__':
    main()