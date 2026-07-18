import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# =====================================================================
# CONSTANTES DE EMISIÓN
# =====================================================================
EMISION_GASOLINA_POR_KM = 120  # gramos de CO2
EMISION_ELECTRICA_POR_KM = 0   # gramos de CO2
CO2_KG_A_TOKEN_FACTOR = 1.0    # 1 kg evitado = 1 Token

# =====================================================================
# SIMULACIÓN DE LA BLOCKCHAIN
# =====================================================================
class BlockchainSimulada:
    def __init__(self):
        self.ledger = {}

    def registrarViaje(self, id_viaje, conductor, distrito, kilometros, co2_evitado_g, tokens):
        if id_viaje in self.ledger:
            print(f"\n⚠️ ERROR BLOCKCHAIN: El ID de viaje '{id_viaje}' ya fue registrado.")
            return False
        
        self.ledger[id_viaje] = {
            "ID": id_viaje,
            "Conductor": conductor,
            "Distrito": distrito,
            "Kilómetros": kilometros,
            "CO2_Evitado_g": co2_evitado_g,
            "Tokens": tokens,
            "FechaRegistro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"\n⛓️ [Blockchain] ¡Éxito! Viaje #{id_viaje} grabado de forma inmutable.")
        print(f"   Generados: {tokens:.2f} MotoCarbon Tokens (MCT).")
        return True

    def obtenerViaje(self, id_viaje):
        return self.ledger.get(id_viaje, None)

    def obtenerTodosLosViajes(self):
        # Convierte el ledger en una lista apta para Pandas
        lista_viajes = []
        for v in self.ledger.values():
            lista_viajes.append({
                "ID": v["ID"],
                "Conductor": v["Conductor"],
                "Distrito": v["Distrito"],
                "Kilómetros": v["Kilómetros"],
                "CO2_Evitado_kg": v["CO2_Evitado_g"] / 1000.0,
                "Tokens": v["Tokens"],
                "Fecha": v["FechaRegistro"]
            })
        return lista_viajes


# =====================================================================
# FUNCIONES DE LA APLICACIÓN INTERACTIVA
# =====================================================================
def mostrar_menu():
    print("\n" + "="*40)
    print("      SISTEMA MOTOCARBON TOKEN (MCT)     ")
    print("="*40)
    print("1. Registrar un nuevo viaje")
    print("2. Consultar un viaje por ID (Blockchain)")
    print("3. Ver reportes actuales (Pandas)")
    print("4. Generar gráficos de impacto (Matplotlib)")
    print("5. Salir")
    print("="*40)

def solicitar_viaje(blockchain):
    print("\n--- REGISTRAR NUEVO VIAJE ---")
    try:
        id_viaje = int(input("Ingrese el ID único del viaje (ej. 101): "))
        if blockchain.obtenerViaje(id_viaje) is not None:
            print("⚠️ Este ID ya existe en la Blockchain. Intente con otro.")
            return

        conductor = input("Nombre del conductor: ").strip().title()
        if not conductor:
            print("⚠️ El nombre no puede estar vacío.")
            return

        distrito = input("Distrito del viaje: ").strip().title()
        if not distrito:
            print("⚠️ El distrito no puede estar vacío.")
            return

        km = float(input("Kilómetros recorridos: "))
        if km <= 0:
            print("⚠️ Los kilómetros deben ser mayores a 0.")
            return
        
        # 3. Cálculos de CO2 Evitado
        co2_gasolina = km * EMISION_GASOLINA_POR_KM
        co2_electrica = km * EMISION_ELECTRICA_POR_KM
        co2_evitado_gramos = co2_gasolina - co2_electrica
        co2_evitado_kg = co2_evitado_gramos / 1000.0
        
        # 4. Generar Tokens
        tokens_generados = co2_evitado_kg * CO2_KG_A_TOKEN_FACTOR

        # Enviar a la Blockchain simulada
        blockchain.registrarViaje(id_viaje, conductor, distrito, km, co2_evitado_gramos, tokens_generados)

    except ValueError:
        print("⚠️ Entrada inválida. Asegúrese de ingresar números donde se solicita.")

def consultar_blockchain(blockchain):
    print("\n--- CONSULTAR VIAJE INMUTABLE ---")
    try:
        id_viaje = int(input("Ingrese el ID del viaje a buscar: "))
        viaje = blockchain.obtenerViaje(id_viaje)
        if viaje:
            print("\n✅ Datos recuperados de la Blockchain:")
            print(f"  • ID: {viaje['ID']}")
            print(f"  • Conductor: {viaje['Conductor']}")
            print(f"  • Distrito: {viaje['Distrito']}")
            print(f"  • Distancia: {viaje['Kilómetros']} km")
            print(f"  • CO2 Evitado: {viaje['CO2_Evitado_g']/1000.0:.2f} kg")
            print(f"  • Tokens MCT: {viaje['Tokens']:.2f}")
            print(f"  • Timestamp Blockchain: {viaje['FechaRegistro']}")
        else:
            print("❌ El viaje con ese ID no existe en el registro.")
    except ValueError:
        print("⚠️ ID inválido.")

def generar_reportes(blockchain):
    viajes = blockchain.obtenerTodosLosViajes()
    if not viajes:
        print("\n📭 No hay datos registrados para generar reportes aún.")
        return

    df = pd.DataFrame(viajes)
    print("\n## REPORTE DE PASAJES Y MÉTRICAS (PANDAS) ##")
    
    print("\n[Métrica 1] CO2 Evitado y Tokens por Conductor:")
    rep_conductor = df.groupby("Conductor")[["CO2_Evitado_kg", "Tokens"]].sum()
    print(rep_conductor.to_string())

    print("\n[Métrica 2] CO2 Evitado por Distrito:")
    rep_distrito = df.groupby("Distrito")[["CO2_Evitado_kg", "Tokens"]].sum()
    print(rep_distrito.to_string())

def mostrar_graficos(blockchain):
    viajes = blockchain.obtenerTodosLosViajes()
    if not viajes:
        print("\n📭 No hay datos registrados para graficar. Registre viajes primero.")
        return

    df = pd.DataFrame(viajes)
    rep_conductor = df.groupby("Conductor")["Tokens"].sum()
    rep_distrito = df.groupby("Distrito")["CO2_Evitado_kg"].sum()

    # Crear interfaz de gráficos
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Gráfico Conductor
    rep_conductor.plot(kind="bar", ax=axes[0], color="mediumseagreen", edgecolor="black")
    axes[0].set_title("Tokens MCT por Conductor")
    axes[0].set_ylabel("Tokens")
    axes[0].set_xlabel("Conductor")
    axes[0].grid(axis="y", linestyle="--", alpha=0.5)

    # Gráfico Distrito
    rep_distrito.plot(kind="bar", ax=axes[1], color="skyblue", edgecolor="black")
    axes[1].set_title("CO2 Evitado por Distrito (KG)")
    axes[1].set_ylabel("Kilogramos")
    axes[1].set_xlabel("Distrito")
    axes[1].grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    print("\n📊 Abriendo ventana de gráficos... (Ciérrala para continuar en la terminal)")
    plt.show()

# =====================================================================
# FLUJO PRINCIPAL DEL PROGRAMA
# =====================================================================
def ejecutar_programa():
    # Inicializar la Blockchain vacía
    mi_blockchain = BlockchainSimulada()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            solicitar_viaje(mi_blockchain)
        elif opcion == "2":
            consultar_blockchain(mi_blockchain)
        elif opcion == "3":
            generar_reportes(mi_blockchain)
        elif opcion == "4":
            mostrar_graficos(mi_blockchain)
        elif opcion == "5":
            print("\n🌱 Gracias por usar MotoCarbon Token. ¡Cuidemos el planeta!")
            break
        else:
            print("⚠️ Opción inválida. Intente de nuevo.")

# Ejecutar la aplicación
if __name__ == "__main__":
    ejecutar_programa()
