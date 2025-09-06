from functools import reduce

# ---

### 1. Número Factorial

# PROGRAMACIÓN NORMAL (ITERATIVA)
'''
Esta función calcula el factorial de un número de forma iterativa usando un bucle 'for'.
Inicializa un resultado en 1 y lo multiplica por cada número desde 1 hasta n.
'''


def factorial_normal(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0:
        return 1

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# RECURSIVIDAD
'''
Esta función calcula el factorial de forma recursiva.
La definición se basa en que el factorial de n es n * factorial(n-1).
El caso base es cuando n es 0, donde el factorial es 1.
'''


def factorial_recursivo(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)


# PROGRAMACIÓN FUNCIONAL
'''
Esta función calcula el factorial de forma funcional usando `reduce` del módulo `functools`.
La función `reduce` aplica una operación (en este caso, la multiplicación) de manera acumulativa
a una secuencia de elementos para reducirla a un solo valor.
'''


def factorial_funcional(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))


# ---

### 2. Serie de Fibonacci

# PROGRAMACIÓN NORMAL (ITERATIVA)
'''
Esta función calcula el n-ésimo término de la serie de Fibonacci de forma iterativa.
Utiliza un bucle para sumar los dos términos anteriores hasta alcanzar el término deseado.
Es más eficiente que la versión recursiva para números grandes.
'''


def fibonacci_normal(n):
    if n < 0:
        raise ValueError("El número de término no puede ser negativo.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# RECURSIVIDAD
'''
Esta función calcula el n-ésimo término de la serie de Fibonacci de forma recursiva.
Se basa en la definición de que F(n) = F(n-1) + F(n-2).
Los casos base son n=0 y n=1.
'''


def fibonacci_recursivo(n):
    if n < 0:
        raise ValueError("El número de término no puede ser negativo.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# PROGRAMACIÓN FUNCIONAL (CON FUNCIÓN INTERNA)
'''
Esta función usa un enfoque funcional y recursivo para calcular Fibonacci.
Aunque es un enfoque funcional, la recursividad no es la forma más eficiente para este problema
debido a la cantidad de llamadas repetidas.
'''


def fibonacci_funcional(n):
    if n < 0:
        raise ValueError("El número de término no puede ser negativo.")

    def fib_recursivo(num):
        return 0 if num == 0 else 1 if num == 1 else fib_recursivo(num - 1) + fib_recursivo(num - 2)

    return fib_recursivo(n)


# ---

### 3. Multiplicación de dos números

# PROGRAMACIÓN NORMAL
'''
Esta es una función simple que multiplica dos números. Es la forma más básica
y directa de realizar esta operación.
'''


def multiplicacion_normal(a, b):
    return a * b


# RECURSIVIDAD
'''
Esta función realiza la multiplicación de forma recursiva, sin usar el operador '*'.
Se basa en el principio de que a * b es igual a 'a' sumado 'b' veces.
El caso base es cuando b es 0, donde el resultado es 0.
'''


def multiplicacion_recursiva(a, b):
    if b == 0:
        return 0
    if b > 0:
        return a + multiplicacion_recursiva(a, b - 1)
    else:
        return -multiplicacion_recursiva(a, -b)


# PROGRAMACIÓN FUNCIONAL
'''
Esta función utiliza un enfoque funcional con una función de orden superior para
realizar la multiplicación. La función `operacion` toma otra función (`multi`) como
parámetro, lo que es una característica clave de la programación funcional.
'''


def multi(n1, n2):
    return n1 * n2


def operacion_funcional(funcion, n1, n2):
    return funcion(n1, n2)


# PROGRAMACIÓN FUNCIONAL CON LAMBDA
'''
Este código demuestra la multiplicación de dos números usando funciones lambda,
que son funciones anónimas y de una sola línea.
'''
multiplicacion_lambda = lambda n1, n2: n1 * n2
operacion_lambda = lambda op, n1, n2: op(n1, n2)

# ---

### 4. Elevación a una Potencia

# PROGRAMACIÓN NORMAL (ITERATIVA)
'''
Esta función calcula la potencia de un número de forma iterativa, sin usar el operador '**'.
Multiplica el número base por sí mismo 'p' veces.
'''


def potencia_normal(n, p):
    if p < 0:
        raise ValueError("El exponente no puede ser negativo en esta implementación.")
    if p == 0:
        return 1

    resultado = 1
    for _ in range(p):
        resultado *= n
    return resultado


# RECURSIVIDAD
'''
Esta función calcula la potencia de forma recursiva. Se basa en que n^p es igual a
n * n^(p-1). El caso base es cuando p es 0, donde el resultado es 1.
'''


def potencia_recursiva(n, p):
    if p < 0:
        raise ValueError("El exponente no puede ser negativo en esta implementación.")
    if p == 0:
        return 1
    else:
        return n * potencia_recursiva(n, p - 1)


# PROGRAMACIÓN FUNCIONAL (CON EXPRESIÓN LAMBDA)
'''
Esta función utiliza un enfoque funcional y conciso con una expresión lambda.
Es la forma más compacta de representar una operación simple.
'''
potencia_funcional = lambda n, p: n ** p

# ---

### 5. Conteo de Dígitos

# PROGRAMACIÓN NORMAL (ITERATIVA)
'''
Esta función cuenta la cantidad de dígitos en un número entero de forma iterativa.
Convierte el número a una cadena de texto para iterar sobre sus caracteres y contar
los que son dígitos. Maneja números negativos tomando el valor absoluto.
'''


def contar_digitos_normal(numero):
    if numero == 0:
        return 1

    numero_str = str(abs(numero))
    contador = 0
    for digito in numero_str:
        if digito.isdigit():
            contador += 1
    return contador


# RECURSIVIDAD
'''
Esta función cuenta los dígitos de un número de forma recursiva.
Se basa en el principio de que el número de dígitos es 1 + el número de dígitos del
número dividido por 10 (división entera), hasta que el número es menor que 10.
'''


def contar_digitos_recursivo(numero):
    if abs(numero) < 10:
        return 1
    else:
        return 1 + contar_digitos_recursivo(numero // 10)


# PROGRAMACIÓN FUNCIONAL
'''
Esta función cuenta los dígitos de un número usando un enfoque funcional.
Convierte el número a una cadena de texto, y luego utiliza la función `len()`
para obtener la longitud de esa cadena. Es una solución concisa y eficaz.
'''


def contar_digitos_funcional(numero):
    return len(str(abs(numero)))


# ---

### 6. Suma de Listas y Tuplas

# PROGRAMACIÓN NORMAL (ITERATIVA)
'''
Esta función suma todos los elementos de un iterable (lista o tupla) de forma iterativa,
usando un bucle 'for' y acumulando el resultado.
'''


def suma_normal(iterable):
    total = 0
    for elemento in iterable:
        total += elemento
    return total


# RECURSIVIDAD
'''
Esta función suma los elementos de un iterable (lista o tupla) de forma recursiva.
La suma es el primer elemento más la suma del resto. El caso base es un iterable vacío.
'''


def suma_recursiva(iterable):
    if not iterable:
        return 0
    else:
        return iterable[0] + suma_recursiva(iterable[1:])


# PROGRAMACIÓN FUNCIONAL
'''
Esta función suma los elementos de un iterable (lista o tupla) utilizando la función `reduce`
del módulo `functools`. `reduce` aplica una función de suma de forma acumulativa.
'''


def suma_funcional(iterable):
    return reduce(lambda x, y: x + y, iterable)


# ---

### **Ejecuciones**

# Factorial
print(f"Factorial normal de 5: {factorial_normal(5)}")  # Resultado: 120
print(f"Factorial recursivo de 6: {factorial_recursivo(6)}")  # Resultado: 720
print(f"Factorial funcional de 7: {factorial_funcional(7)}")  # Resultado: 5040

# Fibonacci
print(f"Fibonacci recursivo de 10: {fibonacci_recursivo(10)}")  # Resultado: 55
print(f"Fibonacci funcional de 10: {fibonacci_funcional(10)}")  # Resultado: 55

# Multiplicación
print(f"Multiplicación con función de orden superior: {operacion_funcional(multi, 4, 5)}")  # Resultado: 20
print(f"Multiplicación con lambda: {operacion_lambda(multiplicacion_lambda, 30, 4)}")  # Resultado: 120
print(f"Multiplicación normal de 2 y 6: {multiplicacion_normal(2, 6)}")  # Resultado: 12

# Potencia
print(f"Potencia recursiva de 4 elevado a 4: {potencia_recursiva(4, 4)}")  # Resultado: 256
print(f"Potencia recursiva de 5 elevado a 8: {potencia_recursiva(5, 8)}")  # Resultado: 390625

# Conteo de dígitos
print(f"Conteo de dígitos normal de 12345: {contar_digitos_normal(12345)}")  # Resultado: 5
print(f"Conteo de dígitos funcional de 145: {contar_digitos_funcional(145)}")  # Resultado: 3

# Suma de listas y tuplas
print(f"Suma normal de lista: {suma_normal([7, 9, 12, 21])}")  # Resultado: 49
print(f"Suma normal de tupla: {suma_normal((7, 9, 12, 21))}")  # Resultado: 49