class P1:
    def m1 (self):
        print ("P1 Method")

class P2:
    def m1 (self):
        print("P2 method")

class C(P2,P1):
        def m1(self):
            print ("C Method")
        
c = C()
c.m1()


