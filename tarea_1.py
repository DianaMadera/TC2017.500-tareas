# Recibes una string conteniendo solo () y []
# Crea un algoritmos para validar que la sintaxis de los corchetes es correcta:
# Ejemplos validos:
# '()'
# '()()()()()()()()()'
# '([])[]()'
# Ejemplos no validos:
# ')'
# '()['
# '(([))]'
# '(((((((((((((((((((((((((((((((((('

open_par = ["(","["]
close_par = [")","]"]
stack = []

#funcion para checar la sintaxis de los corchetes
def check(word):
    for i in word:
        if i in open_par:
            stack.append(i)
        elif i in close_par:
            pos = close_par.index(i)
            if ((len(stack) > 0) and
                (open_par[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Invalid"
    if len(stack) == 0:
        return "Valid"
    else:
        return "Invalid"

#Comprobando una cadena correcta y una incorrecta
input = "()()()()()()()()()"
print(check(input))
input = "(([))]"
print(check(input))