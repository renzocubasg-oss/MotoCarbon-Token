# MotoCarbon Token

## Proyecto Final - Hackathon Carbon Tokenization

### Universidad Nacional Mayor de San Marcos (UNMSM)

---

## Información General

**Curso:** Microeconomía

**Escuela Profesional:** Ingeniería Industrial

**Docente:** Lillo

---

## Integrantes

- Renzo Yair Cubas Gil
- Jimm
- Michaell

---

## Descripción del Proyecto

MotoCarbon Token es una solución basada en tecnología Blockchain que permite registrar el impacto ambiental positivo generado por mototaxis eléctricas mediante la tokenización del CO₂ evitado.

Cada viaje realizado registra información relevante como el conductor, distrito, kilómetros recorridos, CO₂ evitado y la cantidad de tokens ambientales generados. Esta información queda almacenada en un Smart Contract desarrollado en Solidity, garantizando transparencia, trazabilidad e inmutabilidad de los registros.

Como complemento, se desarrolló una simulación en Python que representa el funcionamiento del sistema y visualiza el impacto ambiental obtenido mediante gráficos.

---

# Objetivo

Diseñar un sistema basado en Blockchain para incentivar la movilidad sostenible mediante la generación de tokens ambientales asociados a la reducción de emisiones de carbono producidas por mototaxis eléctricas.

---

# Tecnologías utilizadas

- Solidity
- Hardhat
- Ethereum (Remix IDE)
- Python
- Pandas
- Matplotlib
- Git
- GitHub

---

# Estructura del Proyecto

```
MotoCarbon-Token/
│
├── contracts/
│   └── MotoCarbonToken.sol
│
├── scripts/
│   └── deploy.js
│
├── python-simulation/
│   ├── MotoCarbonSimulation.py
│   └── token de motocarbono.png
│
├── package.json
├── hardhat.config.js
├── .gitignore
└── README.md
```

---

# Smart Contract

El contrato inteligente desarrollado permite:

- Registrar viajes realizados por mototaxis eléctricas.
- Almacenar información del conductor.
- Registrar el distrito donde se realizó el servicio.
- Calcular el CO₂ evitado.
- Generar tokens ambientales.
- Consultar los viajes registrados.
- Emitir eventos en la blockchain para mantener trazabilidad de cada registro.

---

# Simulación

La simulación fue desarrollada en Python utilizando datos representativos para validar el funcionamiento del sistema.

Los resultados muestran:

- CO₂ evitado por conductor.
- CO₂ evitado por distrito.
- Representación gráfica del impacto ambiental generado.
