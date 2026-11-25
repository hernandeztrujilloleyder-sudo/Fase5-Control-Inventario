# Fase 5 - Evaluacion Final POA
# Problema 3 - Control de inventario
# Autor: Leyder Hernandez Trujillo

inventario = [
    ["A001", "Teclado", 5, 15],
    ["A002", "Mouse", 20, 10],
    ["A003", "Monitor", 3, 8],
    ["A004", "Memoria USB", 15, 15],
    ["A005", "Disco SSD", 2, 10]
]

# Funcion para calcular el reabastecimiento
def calcular_reabastecimiento(actual, minimo):
    if actual < minimo:
        return minimo - actual
    else:
        return 0

# Mostrar resultados del inventario
print("CONTROL DE INVENTARIO")
print("-" * 40)

total = 0

for articulo in inventario:
    codigo, nombre, actual, minimo = articulo
    cantidad = calcular_reabastecimiento(actual, minimo)

    print("Codigo:", codigo)
    print("Articulo:", nombre)
    print("Stock actual:", actual)
    print("Stock minimo:", minimo)
    print("Cantidad a solicitar:", cantidad)
    print("-" * 40)

    total += cantidad

print("Total de unidades a solicitar:", total)
