# Paso 1: Función que clasifica la alerta

def clasificacion_alerta(hay_exfiltracion, es_cuenta_admin, afecta_a_activo):
    if(hay_exfiltracion): # Regla 1: si se están robando datos
        return "Crítica"
    elif(es_cuenta_admin): # Regla 2: si implica una cuenta de administrador
        return "Alta"
    elif(afecta_a_activo): # Regla 3: si afecta a un activo
        return "Media"
    else:                  # Si nada de lo anterior
        return "Baja"

# Vamos a probar la función con 3 ejemplos
print(clasificacion_alerta(True, False, False)) # Deberia imprimir Crítica
print(clasificacion_alerta(False, False, True)) # Deberia imprimir Media
print(clasificacion_alerta(False, False, False)) # Deberia imprimir Baja
print(clasificacion_alerta(False, True, False)) # Deberia imprimir Alta

# Paso 2: Probar Script con diccionario de valores
import csv   # csv viene incluido en Python, no hay que instalar nada

conteo_severidad = {}   # diccionarios vacío
conteo_tecnica = {}
conteo_host = {}

with open("alertas.csv", encoding="utf-8") as f:
    lector = csv.DictReader(f)        # lee el CSV fila a fila, por nombre de columna
    for fila in lector:              # recorremos cada alerta
        sev = fila["severidad"]      # cogemos su severidad
        tec = fila["tecnica"]        # y su técnica
        hst = fila["host"]           # y su host

        # .get(sev, 0) dice: "dame lo que ya tenía esta clave, y si no existía, 0"
        # luego le sumamos 1
        conteo_severidad[sev] = conteo_severidad.get(sev, 0) + 1
        conteo_tecnica[tec] = conteo_tecnica.get(tec, 0) + 1
        conteo_host[hst] = conteo_host.get(hst,0) + 1

print("\nAlertas por severidad:")
for sev, n in conteo_severidad.items():
    print(f"  {sev}: {n}")

print("\nAlertas por técnica:")
for tec, n in conteo_tecnica.items():
    print(f"  {tec}: {n}")

print ("\nAlertas por host:")
for hst, n in conteo_host.items():
    print(f"  {hst}: {n}")