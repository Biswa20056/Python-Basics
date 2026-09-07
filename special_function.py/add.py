def Add(num1,num2):
    return num1 + num2
print(list(map(Add,range(1,6),range(11,16))))


def add(num1, num2, num3):
    return num1 + num2 + num3
print(list(map(add, range(1,6), range(11,16), range(20,26))))