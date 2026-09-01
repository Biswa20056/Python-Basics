def reverse(num,rev):
    if num==0:
        return rev
    return reverse(num//10,rev*10 + num%10)


num = 345
rev = 0
print(reverse(num,rev))