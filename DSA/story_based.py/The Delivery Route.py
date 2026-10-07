def reverse_package(package):
    n = len(package)
    i = 0
    j = n-1
    while i<j:
        package[i],package[j] = package[j],package[i]
        i+=1
        j-=1
    return package

package = [10, 20, 30, 40, 50]
print(reverse_package(package))