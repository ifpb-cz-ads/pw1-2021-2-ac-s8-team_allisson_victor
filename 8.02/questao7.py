#7) Escreva uma função para validar uma variável string. Essa função recebe como parâmetro a string, 
# o número mínimo e máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver
#  entre os valores de máximo e mínimo, e falso em caso contrário.

def valida_string(s, mín, máx):
    tamanho = len(s)
    return mín <= tamanho <= máx


print(valida_string("", 1, 5))
print(valida_string("ABC", 2, 5))
print(valida_string("ABCEFG", 3, 5))
print(valida_string("ABCEFG", 1, 10))