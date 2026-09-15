class Sample:
    height = 6.5
    weight = 70.0
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
obj1 = Sample('Biswajit',21,'Bhubaneswar')
obj2 = Sample('Satya',22,'Keonjhar')
obj3 = Sample('Raja',23,'Anugul')

print(Sample.height)# accessing common-prop by class ref

print(obj1.height)# accessing comm-prop by object ref


print(obj2.address)# accessing uncommon-prop by object ref

obj3.age = 35# uncommon-prop changed for only one object
print(obj1.age)
print(obj2.age)
print(obj3.age)