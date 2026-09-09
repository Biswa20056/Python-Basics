s = 'a4@hjcd8#u'
print([ch for ch in s if not ch.isdigit()])


print([ch for ch in s if not '0'<=ch<='9'])