'''def SingleTon(arg):
    l = []
    def Inner():
        if len(l)==0:
            obj = arg()
            l.append(obj)
    return Inner
@SingleTon
class Sample():
    def __init__(self):
        print('Object Created')
obj1 = Sample()
obj2 = Sample()'''

# by dictionary
def SingleTon(arg):
    l = {}
    def Inner():
        if len(l)==0:
            obj = arg()
            l['a'] = obj
            return l['a']
    return Inner
@SingleTon
class Sample():
    def __init__(self):
        print('Object Created')
obj1 = Sample()
obj2 = Sample()