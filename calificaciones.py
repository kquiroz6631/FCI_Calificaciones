from functools import reduce

# 1. Datos iniciales (Inmutabilidad: usamos tuplas de diccionarios)
estudiantes = (
    {"nombre": "Kevin", "nota": 85},
    {"nombre": "Maria", "nota": 92},
    {"nombre": "Jose", "nota": 58},
    {"nombre": "Ana", "nota": 74},
    {"nombre": "Luis", "nota": 62},
)

# 2. Funciones Puras (Sin efectos secundarios, solo dependen de sus argumentos)
es_aprobado = lambda estudiante: estudiante["nota"] >= 70
obtener_nota = lambda estudiante: estudiante["nota"]
obtener_nombre = lambda estudiante: estudiante["nombre"]
sumar_notas = lambda acumulado, nota: acumulado + nota

# --- PROCESAMIENTO DECLARATIVO ---

# A. FILTER: Estudiantes que aprobaron
aprobados = tuple(filter(es_aprobado, estudiantes))

# B. MAP: Lista de solo nombres de los aprobados
nombres_aprobados = tuple(map(obtener_nombre, aprobados))

# C. REDUCE: Cálculo del promedio de notas (Total / Cantidad)
total_puntos = reduce(sumar_notas, map(obtener_nota, estudiantes), 0)
promedio_general = total_puntos / len(estudiantes)

# D. REDUCE: Encontrar la nota más alta (Funciones de orden superior)
mejor_estudiante = reduce(lambda a, b: a if a["nota"] > b["nota"] else b, estudiantes)

# E. ZIP: Combinar nombres con un mensaje de estado
estados = ("Excelente" if n >= 90 else "Regular" for n in map(obtener_nota, estudiantes))
resumen_final = tuple(zip(map(obtener_nombre, estudiantes), estados))

# --- RESULTADOS ---
print(f"Estudiantes Aprobados: {nombres_aprobados}")
print(f"Promedio General de la Facultad: {promedio_general:.2f}")
print(f"Estudiante con mayor puntaje: {mejor_estudiante['nombre']} ({mejor_estudiante['nota']})")
print(f"Resumen de desempeño: {resumen_final}")