class test:
    def __init__(self,a,b):
        self.val1 = a
        self.val2 = b
    def return_value(self):
        return (self.val1 + self .val2)

t = test(1,2)
val = t.return_value()
print(val)