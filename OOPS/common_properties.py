class sample:
    location = 'Bangalore'
    course = 'Python'
Biswa = sample()
Raja = sample()
# the above things inside the class is called as common property
'''
Common property means all the states/property of the objects are same
to acess those common property we can use the reference of object or the reference of class as well as
'''
# to access the common property by object reference
print(Biswa.location)
print(Biswa.location,Biswa.course)

# to access the common propert by the reference of class 

print(sample.location)
print(sample.location,sample.course)