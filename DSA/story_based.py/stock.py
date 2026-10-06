stock = [7,1,5,3,6,4]
max_profit = 0
for i in range(len(stock)-1):
    current_profit = 0
    for j in range(i+1,len(stock)):
        current_profit = stock[j]-stock[i]
        if current_profit>max_profit:
            max_profit = current_profit
print(max_profit)
