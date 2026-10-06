def missing_ticket(tickets,N):
    total_sum = N*(N+1)//2
    active_sum = 0
    for val in tickets:
        active_sum+=val
    return total_sum - active_sum

tickets = [1, 2, 4, 5]
N = 5
print(missing_ticket(tickets,N))
