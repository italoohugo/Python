v = int(input('Digite os 4 primeiros dígitos do seu CPF: '))
x = v // 1000
print('x =',x)
y = (v % 1000) // 100
print('y = ',y)
z = ((v % 1000) % 100) // 10
print('z = ',z)
w = ((v % 1000) % 100) % 10
print('w = ',w)
print(x,y,z,w)
r = w*1000 + z*100 + y*10 + x
print(r)