


## Custom Iterator:-

#% Static
##---------------------------------
class Series:
    def __init__(self):
        self.i=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i<=10:
            dummy=self.i
            self.i+=1
            return dummy
        raise StopIteration
s=Series()
print(s)
for i in s:
    print(i)





#% Dynamically
##--------------------------------------

class Series:
    def __init__(self,sv,ev,up=1):
        self.sv=sv
        self.ev=ev
        self.up=up
    def __iter__(self):
        self.i=self.sv
        return self
    def __next__(self):
        if self.i<self.ev:
            dummy=self.i
            self.i+=self.up
            return dummy
        raise StopIteration
s=Series(1,11)
for i in s:
    print(i)








## Write a custom iterator cube of series of numbers??

class Series:
    def __init__(self,sv,ev,up=1):
        self.sv=sv
        self.ev=ev
        self.up=up
    def __iter__(self):
        self.i=self.sv
        return self
    def __next__(self):
        if self.i<self.ev:
            dummy=self.i**3
            self.i+=self.up
            return dummy
        raise StopIteration
s=Series(1,11)
for i in s:
    print(i)






## WAP to print fibo series by using custom iterator??

class FiboSeries:
    def __init__(self,fe,se,n):
        self.fe=fe
        self.se=se
        self.n=n
    def __iter__(self):
        self.i=1
        return self
    def __next__(self):
        if self.i<=self.n:
            dummy=self.fe
            self.fe=self.se
            self.se=dummy+self.se
            self.i+=1
            return dummy
        raise StopIteration
fs=FiboSeries(2,3,10)
for i in fs:
    print(i)

