def maximum_energy(energy):
    n = len(energy)
    min_price = float('inf')
    max_gain = 0
    for i in range(n-1):
        min_price = min(energy[i], min_price)
        max_gain = max(max_gain, energy[i]-min_price)
    return max_gain
            
energy = [7, 1, 5, 3, 6, 4]
print(maximum_energy(energy))