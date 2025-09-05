from functools import reduce

# Numero Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Numero Factorial Programacion Funcional
def factorial2(n):
    return 1 if n == 0 else n * factorial(n - 1)

# Numero factorial con Functools
def factorial3(n) -> int:
    if n < 0:
        raise ValueError("No se aceptan numeros negativos")
    elif n == 0:
        return 1
    else:
        return reduce(lambda x,y : x * y, range(1, n + 1))

# Serie de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Serie de Fibonacci Programacion Funcional
def fibonacci2(n):
    return 0 if n == 0 else 1 if n == 1 else fibonacci(n - 1) + fibonacci(n - 2)

#multiplicacion a * b
def mult2(a, b):
    return a * b

#multiplicacion de 2 numero Programcion Funcional
def multi(n1=0, n2=0):
    return n1 * n2
def operacion(funcion, n1=0, n2=0):
    return funcion(n1, n2)
funcion_mult = multi
resultado = operacion(funcion_mult, 4, 5)

#multiplicacion de 2 numeros con lambda
multiplicacion = lambda n1=0, n2=0: n1 * n2
operacion = lambda operacion, n1=0, n2=0 : operacion(n1,n2)
resultado2= operacion(multiplicacion, 30,4)


#elevacion de numero a una potencia
def potencia(n,p):
    return n ** p

# potencia termaria
def potencia2(n, p):
    return 1 if p == 0 else n * potencia(n, p - 1)

#Conteo de digitos
# Iterativa
def contar_digitos_iterativo(numero):
    # Maneja el caso del número 0
    if numero == 0:
        return 1

    # Toma el valor absoluto para manejar números negativos
    numero = abs(numero)

    contador = 0
    while numero > 0:
        numero //= 10  # División entera por 10
        contador += 1
    return contador

# Recursivo
def contar_digitos_recursivo(numero):
    # Toma el valor absoluto para manejar números negativos
    numero = abs(numero)

    if numero < 10:  # Caso base: un solo dígito
        return 1
    else:
        # Paso recursivo: 1 + el conteo de los dígitos restantes
        return 1 + contar_digitos_recursivo(numero // 10)

# Funcional
def contar_digitos_funcional(numero):
    # Convierte el número a string y toma su longitud
    return len(str(abs(numero)))

# Suma de lista [7, 9, 12, 21]
# Iterativa
def suma_normal(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total

lista_numeros = [7, 9, 12, 21]

# Recursividad
def suma_recursiva(lista):
    if not lista:  # Caso base: la lista está vacía
        return 0
    else:  # Paso recursivo: primer elemento + suma del resto de la lista
        return lista[0] + suma_recursiva(lista[1:])

lista_numeros = [7, 9, 12, 21]

# Funcional
def suma_funcional(lista):
    # La función lambda x, y: x + y define la operación de suma
    return reduce(lambda x, y: x + y, lista)

lista_numeros = [7, 9, 12, 21]

# Suma de tupla (7, 9, 12, 21)
# Iterativa
def suma_normal_tupla(tupla):
    total = 0
    for elemento in tupla:
        total += elemento
    return total

mi_tupla = (7, 9, 12, 21)

# Recursiva
def suma_recursiva_tupla(tupla):
    if not tupla:
        return 0
    else:
        return tupla[0] + suma_recursiva_tupla(tupla[1:])

mi_tupla = (7, 9, 12, 21)

# Funcional
def suma_funcional_tupla(tupla):
    return reduce(lambda x, y: x + y, tupla)

mi_tupla = (7, 9, 12, 21)


'''
En las siguientes lines estan colocados 
los print de cada funcion
'''

# Ejecuciones
print(factorial(5))
print(factorial2(6))
print(factorial3(7))


print(fibonacci(10))
print(fibonacci2(10))


print(resultado)
print(resultado2) #con lambda


print(mult2(2,6))


print(potencia(4, 4))
print(potencia2(5,8))


print(f"Número de dígitos (iterativo) en 12345: {contar_digitos_iterativo(12345)}")
print(f"Número de dígitos (iterativo) en -987: {contar_digitos_iterativo(-987)}")
print(f"Número de dígitos (iterativo) en 0: {contar_digitos_iterativo(0)}")
print(f"Número de dígitos (recursivo) en 12345: {contar_digitos_recursivo(12345)}")
print(f"Número de dígitos (recursivo) en -987: {contar_digitos_recursivo(-987)}")
print(f"Número de dígitos (recursivo) en 0: {contar_digitos_recursivo(0)}")
print(f"Número de dígitos (funcional) en 12345: {contar_digitos_funcional(12345)}")
print(f"Número de dígitos (funcional) en -987: {contar_digitos_funcional(-987)}")
print(f"Número de dígitos (funcional) en 0: {contar_digitos_funcional(0)}")


print(f"Suma normal: {suma_normal(lista_numeros)}") # Salida: 49
print(f"Suma recursiva: {suma_recursiva(lista_numeros)}") # Salida: 49
print(f"Suma funcional: {suma_funcional(lista_numeros)}") # Salida: 49


print(f"Suma normal de la tupla: {suma_normal_tupla(mi_tupla)}")
print(f"Suma recursiva de la tupla: {suma_recursiva_tupla(mi_tupla)}")
# O utilizando la función integrada sum() para un enfoque más conciso
print(f"Suma funcional de la tupla (con sum()): {sum(mi_tupla)}")

