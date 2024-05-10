#Recursividad para calcular el factorial de un número.
"""
PSEUDOCÓDIGO:
Algoritmo factorial 
-Hipótesis: 
    Algoritmo para sacar el factorial de un número a través del método de recursividad
-Precondición:
    el numero (n) debe ser positivo
    si es 0, igualarlo por definición a 1
-Entrada: 
    el número (n) para sacar sus factores
-Tratamiento datos:
    si n diferente a 0, multiplicar n por (n-1) hasta llegar a 0 y así el último número 
    que multiplique sea 1 y acabe la recursividad
-Salida:
    Valor del factorial
"""
def factorial(n):
    """Calcula el factorial de un número dado.
    
    Parameters
    ----------
    n : int
        Número entero al que se le calculará el factorial.
        
    Returns
    -------
    int
        El factorial del número dado.
        
    Example
    -------
    factorial(5)
    120
    """
    #Código a realizar.
    if n < 0:
        raise ValueError("El número ingresado debe ser positivo.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print("=================================================================.")
    print("Test Case 1: Check the Factorial of 5.")
    print("=================================================================.")
    print("The factorial of 5 is: ", factorial(5))

if __name__ == "__main__":
    main()
    