#  ����� � ����� �������� "�"
class A:
    def printA(self):
        print("A")
 
 
#  ����� B ����� �������� "B"
class B:
    def printB(self):
        print("B")
 
# ����� C ����������� �� ������� A � B
class C(A, B):        
    pass
 
 

d = C()
d.printA()    
d.printB()