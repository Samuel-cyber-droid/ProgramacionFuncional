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

#Serie de Fibonacci con Functools
def fibonacci3(n) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n + 1):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        return fib_sequence[n]

#Serie de Fibonacci mas eficiente
def fibonacci4(n) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


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

#potencia de numero con functools
def potencia3(n, p) -> float:
    if p == 0:
        return 1
    elif p > 0:
        return reduce(lambda x, y: x * n, range(p), 1)
    else:
        return 1 / reduce(lambda x, y: x * n, range(abs(p), 1))


#Conteo de digitos
def contar_digitos_iterativo(numero):
    # Convertir a string para manejar números negativos
    numero_str = str(abs(numero))
    contador = 0

    for digito in numero_str:
        if digito.isdigit():
            contador += 1

    return contador

# Conteo de digitos con map y filter *mas rapido*
def contar_digitos_funcional_completo(numero):
    return len(list(filter(str.isdigit, str(abs(numero)))))

# Suma de lista [7, 9, 12, 21]

# Suma de tupla (7, 9, 12, 21)

# Ejecuciones
print('Factoriales')
print(factorial(5))
print(factorial2(5))
print(factorial3(5))

print('Series de Fibonacci')
print(fibonacci(10))
print(fibonacci2(10))
print(fibonacci3(10))
print(fibonacci4(10))

print('Multiplicaciones')
print(resultado)
print(resultado2) #con lambda

print(mult2(2,6))


print('Potencias')
print(potencia(4, 4))
print(potencia2(4,4))
print(potencia3(4, 4))


print('Conteo de Digitos')
print(contar_digitos_iterativo(12345))
print(contar_digitos_funcional_completo(145))

