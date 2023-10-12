class CreditCard:
    def main(self, number):
        number = 5196081888500645
        print(str(number) + " is " +
              ("valid" if CreditCard.isValid(number) else "invalid"))

    def isValid(number):
        return (CreditCard.getSize(number) >= 13 and CreditCard.getSize(number) <= 16) and (
                CreditCard.prefixMatched(number, 4) or CreditCard.prefixMatched(number,
                                                                                5) or CreditCard.prefixMatched(
            number, 37) or CreditCard.prefixMatched(number, 6)) and (
                (CreditCard.sumOfDoubleEvenPlace(number) + CreditCard.sumOfOddPlace(number)) % 10 == 0)

    def sumOfDoubleEvenPlace(self, number):
        sum = 0
        num = str(number) + ""
        number = CreditCard.getSize(number) - 2
        while (number >= 0):
            sum += CreditCard.getDigit(int(str(num[number]) + "") * 2)
            number -= 2
        return sum

    def getDigit(self, number):
        if (number < 9):
            return number
        return int(number / 10) + number % 10

    def sumOfOddPlace(number):
        sum = 0
        num = str(number) + ""
        count = CreditCard.getSize(number) - 1
        while (count >= 0):
            sum += int(str(num[count]) + "")
            count -= 2
        return sum

    def prefixMatched(number, d):
        return CreditCard.getPrefix(number, CreditCard.getSize(d)) == d

    def getSize(number):
        num = str(number) + ""
        return len(num)

    def getPrefix(number, count):
        if (CreditCard.getSize(number) > count):
            num = str(number) + ""
            return int(num[0:count])
        return number
