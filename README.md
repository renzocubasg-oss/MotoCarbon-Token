# MotoCarbon Token

## Proyecto Final - Hackathon Carbon Tokenization

### Universidad Nacional Mayor de San Marcos (UNMSM)

---

# Información General

**Curso:** Microeconomía

**Escuela Profesional:** Ingeniería Industrial

**Docente:** Lillo

---

# Integrantes

- Cubas Gil, Renzo Yair
- Mendez Mosquera, Jimmy
- Santiago Leon, Michaell Pool

---

# Descripción del Proyecto

MotoCarbon Token es una solución basada en tecnología Blockchain que permite registrar el impacto ambiental positivo generado por mototaxis eléctricas mediante la tokenización del CO₂ evitado.

Cada viaje realizado registra información relevante como el conductor, distrito, kilómetros recorridos, CO₂ evitado y la cantidad de tokens ambientales generados. Esta información queda asociada a un Smart Contract desarrollado en Solidity, garantizando transparencia, trazabilidad e integridad de los registros.

Como complemento, se desarrolló una aplicación web interactiva que simula el funcionamiento del sistema. La plataforma permite conectar una billetera simulada, registrar viajes eléctricos, calcular automáticamente el CO₂ evitado, generar MotoCarbon Tokens (MCT) y visualizar el historial de registros en una blockchain simulada.

---

# Objetivo

Diseñar un sistema basado en Blockchain para incentivar la movilidad sostenible mediante la generación de tokens ambientales asociados a la reducción de emisiones de carbono producidas por mototaxis eléctricas.

---

# Tecnologías utilizadas

- Solidity
- Hardhat
- Ethereum (Remix IDE)
- HTML5
- CSS3
- JavaScript
- Git
- GitHub

---

# Estructura del Proyecto

```text
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
│   └── motocarbon token.png
│
├── web-app/
│   └── index.html
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
- Generar MotoCarbon Tokens.
- Consultar los viajes registrados.
- Emitir eventos en la blockchain para mantener la trazabilidad de cada registro.

---

# Aplicación Web

La aplicación web fue desarrollada utilizando HTML5, CSS3 y JavaScript como una demostración funcional del proyecto MotoCarbon Token.

Sus principales funcionalidades son:

- Conexión de una billetera simulada.
- Registro de viajes realizados por mototaxis eléctricas.
- Cálculo automático del CO₂ evitado.
- Generación de MotoCarbon Tokens (MCT).
- Visualización del historial de registros en una blockchain simulada.
- Dashboard con métricas del impacto ambiental generado.

---

# Funcionamiento del Sistema

1. El usuario conecta una billetera simulada.
2. Registra un viaje indicando la distancia recorrida y la ruta.
3. El sistema calcula el CO₂ evitado con respecto a una mototaxi convencional.
4. Se generan MotoCarbon Tokens equivalentes al impacto ambiental obtenido.
5. El viaje queda registrado en un historial que representa una blockchain simulada.

---

# Arquitectura del Proyecto

```
Mototaxi Eléctrica
        │
        ▼
Registro del Viaje
        │
        ▼
Cálculo de CO₂ Evitado
        │
        ▼
Generación de MotoCarbon Tokens
        │
        ▼
Registro en Blockchain Simulada
```

---

# Futuras Mejoras

- Integración con MetaMask.
- Despliegue del Smart Contract en una red EVM.
- Integración con LACChain.
- Almacenamiento de evidencias mediante IPFS.
- Desarrollo de una aplicación móvil.
- Panel administrativo para asociaciones y municipalidades.

---

# Repositorio

Este repositorio contiene el Smart Contract desarrollado en Solidity junto con una aplicación web que demuestra el funcionamiento del sistema de tokenización ambiental MotoCarbon Token mediante una interfaz interactiva.

---

# Autores

**Carbon Mobility Team**

Universidad Nacional Mayor de San Marcos (UNMSM)
