class Sample:
    height = 6.5
    weight = 78.0
obj1 = Sample()
obj2 = Sample()
# access-comm-prop by obj ref
print(obj1.height, obj1.weight)
print(obj2.height, obj2.weight)
print('---------')
# access-comm-by-class-ref
print(Sample.height)
print(Sample.weight)