class cal():
    def __init__(self, num1 , num2, op):
        self.num1 = num1
        self.num2 = num2
        self.op = op


        sum = 0
        if op == '+':
            sum = num1 + num2
            print('sum of two number is : {}'.format(sum))
        elif op == '-':
            sum = num1 - num2
            print('subtraction of two number is : {}'.format(sum))
        elif op == '*':
            sum = num1 * num2
            print('multiplication of two number is : {}'.format(sum))
        elif op == "/":
            if num2 == 0:
                print('denominator can not be zero')
            else:
                sum = num1 / num2
                print('division of two number is : {}'.format(sum))
        else:
            print('enter valid operand')


    def abc(self):
        print("this is my next level shit")


n1 = int(input('enter the number1:'))
n2 = int(input('enter the number2:'))
opd = input('enter the operand[+,-,*,\]:')

if __name__ == '__main__':
    a = cal(n1, n2, opd)
    # a.abc()
