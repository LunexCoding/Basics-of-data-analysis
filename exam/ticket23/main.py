class DataAnalysis:
    '''
    Найти все простые натуральные числа, не превосходящие n, двоичная запись которых представляет собой палиндром,
    т. е. читается одинаково слева направо и справа налево.
    '''

    def __init__(self, array=None):
        self._array = array

    def checkPalindrome(self):
        for num in self._array:
            copyNum = num
            result = 0

            while num != 0:
                digit = num % 10
                result = result * 10 + digit
                num = int(num / 10)

            if result == copyNum:
               print(copyNum)
            

task = DataAnalysis([123321, 3345, 121, 5643, 45654])
task.checkPalindrome()

    