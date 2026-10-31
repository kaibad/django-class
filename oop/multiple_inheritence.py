# multiple ingeritance
class A:
    #variable
    a = 10

    #method
    def method_a(self):
        print("Method A from class A") 


class B:
    def method_b(self):
        print("Method B from class B") 


class C(A, B):
    def method_c(self):
        print("Method C from class C") 

C = C()
# accesing vaiables
print(C.a)  # Output: 10

C.method_a()  # Output: Method A from class A
C.method_b()  # Output: Method B from class B
C.method_c()  # Output: Method C from class C