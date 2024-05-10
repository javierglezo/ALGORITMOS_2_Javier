import functools
"""
"PSEUDOCÓDIGO"
Entrada: Menú, elaborar métodos de los descuentos en una clase y a través de un input introducir el precio base (float) para calcular 
el precio con descuento final.
Final: Precio final
"""
class SimpleOperations:
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""
        return price * (1 - discount)

    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""
        return price * (1 + tax_rate)

# Crear una instancia (OBJETO) de SimpleOperations
operations = SimpleOperations()

# Definir funciones predefinidas con functools.partial
twenty_percent_discount = functools.partial(operations.apply_discount, discount=0.20)
vat_tax = functools.partial(operations.calculate_tax, tax_rate=0.21)

def main():
    print("Bienvenido al programa de cálculo de precios.")
    while True:
        print("\nMenú:")
        print("1. Aplicar descuento del 20%")
        print("2. Aplicar impuesto del 21%")
        print("3. Salir")
        
        choice = input("Ingrese su elección (1/2/3): ")
        
        if choice == "1":
            price = float(input("Ingrese el precio base: "))
            new_price = twenty_percent_discount(price)
            print("Precio con descuento del 20%:", new_price)
        elif choice == "2":
            price = float(input("Ingrese el precio base: "))
            new_price = vat_tax(price)
            print("Precio con impuesto del 21%:", new_price)
        elif choice == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

if __name__ == "__main__":
    main()
