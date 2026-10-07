def Security_check(IDs):
    n = len(IDs)
    for i in range(n-1):
            if IDs[i+1]<IDs[i]:
                return False
    return True

IDs = [1, 3, 2, 4, 5]
print(Security_check(IDs))