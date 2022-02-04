#1) Escreva uma função que retorne o maior de dois números. Valores esperados:
# máximo(5,6) == 6
# máximo(2,1) == 2
# máximo(7,7) == 7

def máximo(x, y):
    if x > y:
        return x
    else:
        return y


print("O maior numero entre 5 e 6 é : ", máximo(5,6))
print("O maior numero entre 2 e 1 é : ", máximo(2,1))
print("O maior numero entre 7 e 7 é : ", máximo(7,7))