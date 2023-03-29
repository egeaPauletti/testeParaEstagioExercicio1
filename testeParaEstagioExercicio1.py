x1 = 0
x2 = 1
x3 = 0
x4 = 0


print('_'*30)
print('Sequência de Fibonacci')
print('_'*30)
input = int(input('Insira um numero: '))
print('~'*30)

while True:
    if x3 <= input:
        x3 = x1 + x2
        x1 = x2
        x4 = x2
        x2 = x3
    else:
        break

if x4 == input:
 print('este numero FAZ parte da Sequência de Fibonacci')

else:
   print('este numero NÃO faz parte Sequência de Fibonacci')
