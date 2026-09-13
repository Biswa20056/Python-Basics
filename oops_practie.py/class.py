class Sample:
    height = 4.0
    weight = 70.5

obj1 = Sample()
obj2 = Sample()
print(obj1.height)
# changing common-prop by object ref
obj1.height = 5.0
print(obj1.height)
print(obj2.height)
