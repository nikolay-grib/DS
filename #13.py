#  класс ј умеет печатать "ј"
class A:
    def printA(self):
        print("A")
 
 
#  класс B умеет печатать "B"
class B:
    def printB(self):
        print("B")
 
# класс C наследуетс€ от классов A и B
class C(A, B):        
    pass
 
 

d = C()
d.printA()    
d.printB()