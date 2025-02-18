def Fact(num):
    if num==1 or num==0:
        return 1
    else:
        return num*Fact(num-1)

def Fabonacci(num):
    if num==1 or num==0:
        return 1
    else:
        return Fabonacci(num-1)+Fabonacci(num-2)


def SumOfDigits(num):
    if num==0:
        return 0
    else:
        return num%10+SumOfDigits(num//10)  


print(SumOfDigits(1234))