FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    words = []
    if 100 <= number < 1000:
        words.append(FIRST_TEN[(number//100)-1])
        words.append(HUNDRED)
        number = number%100
    if 20 <= number <= 99:
        words.append(OTHER_TENS[(number//10)-2])
        number = number%10
    elif 10 <= number <= 19:
        words.append(SECOND_TEN[number-10])
        number = 0
    if 0 < number <= 9:
        words.append(FIRST_TEN[number-1])
        
    return ' '.join(words)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
