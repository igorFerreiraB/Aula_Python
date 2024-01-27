# Method resolusion order
# MRO

class A:
    def say_hello(self):
        print("Hello from class A")

class B(A):
    def say_hello(self):
        print("Hello from class B")

class C(A):
    def say_hello(self):
        print("Hello from class C")

class D(B, C):
    pass

# A MRO para a classe D
print(D.mro())