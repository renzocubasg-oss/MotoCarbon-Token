# ==============================================================================
# PROYECTO: MotoCarbon Token - Simulación de Impacto Ambiental (Python)
# EQUIPO: Carbon Mobility Team - UNMSM
# COMPONENTE: /python-simulation
# ==============================================================================

import pandas as pd
import matplotlib.pyplot as plt

# 1. DEFINICIÓN DE FACTORES DE EMISIÓN (Metodología Basada en GSA/MINAM)
# Factor promedio estimado de emisión para una mototaxi convencional a gasolina:
# Se calcula en gramos de CO2 por kilómetro recorrido (g CO2 / km)
FACTOR_GASOLINA_G_KM = 120.0  # Ejemplo: 120g de CO2 por km recorrido
FACTOR_ELECTRICO_G_KM = 0.0    # Moto eléctrica (cero emisiones directas en ruta)

# Relación de Tokenización: Cantidad de CO2 evitado necesaria para generar 1 MotoCarbon Token
# Ejemplo: 1 Token por cada 1000 gramos (1 kg) de CO2 evitado
CO2_GRAMOS_POR_TOKEN = 1000.0

# 2. BASE DE DATOS SIMULADA (Viajes realizados por mototaxis eléctricas)
datos_viajes = {
    'id_viaje': [101, 102, 103, 104, 105, 106],
    'conductor': ['Michaell Santiago', 'Juan Perez', 'Michaell Santiago', 'Ana Gomez', 'Juan Perez', 'Ana Gomez'],
    'distrito': ['Villa El Salvador', 'San Juan de Miraflores', 'Villa El Salvador', 'Villa María del Triunfo', 'San Juan de Miraflores', 'Villa María del Triunfo'],
    'km_recorridos': [15.5, 22.0, 12.3, 30.5, 18.2, 25.0]
}

# Crear el DataFrame principal con Pandas
df_viajes = pd.DataFrame(datos_viajes)

# 3. LÓGICA DE CÁLCULO AMBIENTAL
# Cálculo del CO2 que habría emitido una mototaxi a gasolina en esa misma distancia
df_viajes['co2_gasolina_g'] = df_viajes['km_recorridos'] * FACTOR_GASOLINA_G_KM

# Cálculo del CO2 de la mototaxi eléctrica
df_viajes['co2_electrico_g'] = df_viajes['km_recorridos'] * FACTOR_ELECTRICO_G_KM

# CO2 Evitado = CO2 Gasolina - CO2 Eléctrico (en gramos y convertido a kilogramos)
df_viajes['co2_evitado_g'] = df_viajes['co2_gasolina_g'] - df_viajes['co2_electrico_g']
df_viajes['co2_evitado_kg'] = df_viajes['co2_evitado_g'] / 1000.0

# Cálculo de MotoCarbon Tokens generados (Proporcional al CO2 evitado)
df_viajes['tokens_generados'] = df_viajes['co2_evitado_g'] / CO2_GRAMOS_POR_TOKEN

print("--- REGISTRO DE TRAZABILIDAD DE VIAJES PROCESADO ---")
print(df_viajes[['id_viaje', 'conductor', 'distrito', 'km_recorridos', 'co2_evitado_kg', 'tokens_generados']])
print("-" * 60)

# 4. AGRUPACIÓN Y REPORTES ACUMULADOS (Pandas)
# Impacto total acumulado por cada conductor
reporte_conductores = df_viajes.groupby('conductor')[['km_recorridos', 'co2_evitado_kg', 'tokens_generados']].sum().reset_index()

# Impacto total acumulado por distrito de Lima Sur
reporte_distritos = df_viajes.groupby('distrito')[['co2_evitado_kg']].sum().reset_index()

print("\n--- RESUMEN DE IMPACTO POR CONDUCTOR ---")
print(reporte_conductores)

# 5. VISUALIZACIÓN GRÁFICA (Matplotlib)
plt.style.use('seaborn-v0_8-whitegrid') # Estilo limpio para la presentación
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico 1: CO2 Evitado por Conductor (en KG)
ax1.bar(reporte_conductores['conductor'], reporte_conductores['co2_evitado_kg'], color='#2ecc71', edgecolor='black')
ax1.set_title('Impacto Ambiental: CO₂ Evitado por Conductor', fontsize=12, fontweight='bold')
ax1.set_xlabel('Conductor')
ax1.set_ylabel('CO₂ Evitado (Kilogramos)')
for i, v in enumerate(reporte_conductores['co2_evitado_kg']):
    ax1.text(i, v + 0.1, f"{v:.2f} kg", ha='center', fontweight='bold')

# Gráfico 2: CO2 Evitado por Distrito de Lima Sur
ax2.bar(reporte_distritos['distrito'], reporte_distritos['co2_evitado_kg'], color='#3498db', edgecolor='black')
ax2.set_title('Descarbonización Urbana: CO₂ Evitado por Distrito', fontsize=12, fontweight='bold')
ax2.set_xlabel('Distrito')
ax2.set_ylabel('CO₂ Evitado (Kilogramos)')
plt.xticks(rotation=15)
for i, v in enumerate(reporte_distritos['co2_evitado_kg']):
    ax2.text(i, v + 0.1, f"{v:.2f} kg", ha='center', fontweight='bold')

plt.tight_layout()
plt.suptitle('MotoCarbon Token - Simulación de Resultados Funcionales', fontsize=14, fontweight='bold', y=1.02)

# Guardar gráfico para usarlo en la documentación o diapositivas
plt.savefig('impacto_ambiental_motocarbon.png', dpi=300, bbox_inches='tight')
plt.show()
