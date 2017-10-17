#!/usr/bin/python3

# simple fibonacci series
# the series of two elements defines the next set
class FIbonacci:
    def __init__(self, a, b): # initializer
        self.a = a
        self.b = b
    
    def series(self):
        while(True): 
            yield(self.b) # generator
            self.a, self.b = self.b, self.a + self.b

f = FIbonacci(0, 1) # Create an object called f
for r in f.series():
    if r > 100 : break
    print(r, end=' ')
print()