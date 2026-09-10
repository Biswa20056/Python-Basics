class sample:
    location = 'Bangalore'
    course = 'Python'

Biswa = sample()
Raja = sample()

'''
To change the common property of the objects we can take the help of object reference and as well as class reference
if we will take the object reference then it will not affect the remaining object property
if we will take the class reference then it will affect all the object property
'''

# change location for raja by object reference
Biswa.location = 'Delhi'
print(Biswa.location)
print(Raja.location)

# change location by class reference

class sample_1:
    location = 'Bangalore'
    course = 'Python'

Biswa = sample_1()
Raja = sample_1()
sample_1.location = 'Chennai'
print(Biswa.location)
print(Raja.location)