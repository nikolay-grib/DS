#  класс А умеет печатать "А"
class A:
    def printA(self):
        print("A")
 
 
#  класс B умеет печатать "B"
class B:
    def printB(self):
        print("B")
 
# класс C наследуется от классов A и B
class C(A, B):        
    pass
 
 

d = C()
d.printA()    
d.printB()