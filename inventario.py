# ============================================================
#  Problema 3 - Auditoría de Inventario
#  Fase 5 - Evaluación Final POA
# ============================================================

# --- Matriz de inventario ---
# Estructura: [Código, Nombre, Stock Actual, Stock Mínimo Requerido]
inventario = [
    [1001, "Papel A4",           30,  50],
    [1002, "Tóner impresora",     5,  10],
    [1003, "Carpetas archivador", 20,  20],
    [1004, "Bolígrafos (caja)",    2,  15],
    [1005, "Grapadora",           8,   5],
]

# --- Módulo / Función ---
def calcular_pedido(stock_actual, stock_minimo):
    """
    Determina la cantidad exacta a pedir para un artículo.
    Retorna la diferencia si hay déficit, o cero si el stock es suficiente.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# --- Lógica principal ---
print("=" * 50)
print("     REPORTE DE REABASTECIMIENTO DE INVENTARIO")
print("=" * 50)

for articulo in inventario:
    codigo       = articulo[0]
    nombre       = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    if cantidad_pedir > 0:
        print(f"Artículo: {nombre:<25} | Cantidad a pedir: {cantidad_pedir} unidades")
    else:
        print(f"Artículo: {nombre:<25} | Sin necesidad de reabastecimiento")

print("=" * 50)
print("Auditoría finalizada.")