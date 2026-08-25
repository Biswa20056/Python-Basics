def factor(num: int) -> int:
    fact = 1
    for val in range(1, num + 1):
        fact *= val
    return fact

def digits(num: int) -> int:
    total = 0
    while num > 0:
        total += factor(num%10)
        num //= 10
    return total

def is_strong(num: int) -> str:
    if num == digits(num):
        return "Strong Number"

    return "Not Strong Number"

num = 40585
print(is_strong(num))
