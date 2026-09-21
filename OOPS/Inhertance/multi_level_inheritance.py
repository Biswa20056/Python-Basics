class A():
    v1 = 40
    v2 = 50
class B(A):
    v2 = 60
    v3 = 90
class C(B):
    v3 = 100
    v1 = 10

obj = C()
obj.v1