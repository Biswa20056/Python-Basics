'''
Infosys Q1 Story Problem 1 — The Treasure Hunt
A group of treasure hunters enters an ancient cave. Inside the cave, they discover N treasure boxes arranged in a straight line.
Each box contains a certain number of gold coins.
The treasure hunters want to find out:
Which box contains the maximum number of gold coins?

You are given the number of boxes and the number of coins in each box. Your task is to determine the maximum number of coins present in any one box.
'''

def treasure(coins):
    n = len(coins)
    if n==1:
        return coins[0]
    else:
        max_coin = coins[0]
        for i in range(n):
            current_coin = coins[i]
            if current_coin>max_coin:
                max_coin = current_coin
        return max_coin

coins = [12, 45, 7, 89, 23, 56, 34]
print(treasure(coins))