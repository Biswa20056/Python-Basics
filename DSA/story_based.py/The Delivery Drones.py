def missing_drone(deliveries):
    max_delivery = 0
    current_delivery = 0
    n = len(deliveries)
    for i in range(n):
        if deliveries[i]==1:
            current_delivery +=1
            if current_delivery > max_delivery:
                max_delivery = current_delivery
        else:
            current_delivery = 0
    return max_delivery

Deliveries = [1, 1, 0, 1, 1, 1, 0]
print(missing_drone(Deliveries))