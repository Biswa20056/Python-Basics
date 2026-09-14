class Sample:
    height = 6.0
    weight = 45.5

obj1 = Sample()
obj2 = Sample()
# modifying comm-prop by class ref
Sample.height = 9.0
print(obj1.height)
print(obj2.height)
