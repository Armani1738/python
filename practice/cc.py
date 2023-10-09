class CreditCard:
    @staticmethod
    def main(args):
        number = 5196081888500645
        print(str(number) + " is " +
              ("valid" if CreditCard.isValid(number) else "invalid"))
    @staticmethod
    def isValid(number):
        return (CreditCard.getSize(number) >= 13 and CreditCard.getSize(number) <= 16) and (CreditCard.prefixMatched(number, 4) or CreditCard.prefixMatched(number,5) or CreditCard.prefixMatched(
                number, 37) or CreditCard.prefixMatched(number, 6)) and ((CreditCard.sumOfDoubleEvenPlace(number) + CreditCard.sumOfOddPlace(number)) % 10 == 0)
    @staticmethod
    def sumOfDoubleEvenPlace(number):
        sum = 0
        num = str(number) + ""
        number = CreditCard.getSize(number) - 2
        while (number >= 0):
            sum += CreditCard.getDigit(int(str(num[number]) + "") * 2)
            number -= 2
        return sum
    @staticmethod
    def getDigit(number):
        if (number < 9):
            return number
        return int(number / 10) + number % 10
    @staticmethod
    def sumOfOddPlace(number):
        sum = 0
        num = str(number) + ""
        count = CreditCard.getSize(number) - 1
        while (count >= 0):
            sum += int(str(num[count]) + "")
            count -= 2
        return sum
    @staticmethod
    def prefixMatched(number, d):
        return CreditCard.getPrefix(number, CreditCard.getSize(d)) == d
    @staticmethod
    def getSize(number):

        num = str(number) + ""
        return len(num)
    @staticmethod
    def getPrefix(number, count):
        if (CreditCard.getSize(number) > count):
            num = str(number) + ""
            return int(num[0:count])
        return number