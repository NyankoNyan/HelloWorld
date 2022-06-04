#Императивная
a = 5
a = a * 10
print(a)

#Деларативные

#Функцинальная

def mult2(a,b):
    return a*b

c = mult2(5,2)

#Класс

class Test:
    a = 5
    def mult(self, b):
        return self.a*b

test = Test()
print(test.mult(2))


l = [3,2,1]
#l.sort()
#print(l)

print( sorted( l ) )

print(l)