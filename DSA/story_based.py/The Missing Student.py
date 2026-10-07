def missing(rollnumber,n):
    actual_sum = n*(n+1)//2
    present_sum = 0
    for val in rollnumber:
        present_sum += val
    return actual_sum - present_sum

n = 5
rollnumber = [3, 0, 1, 4, 2]
print(missing(rollnumber,n))