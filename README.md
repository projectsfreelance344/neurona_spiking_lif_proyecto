> Simulador de Neurona de Impulsos (Spiking Neural Network - SNN) basado en el modelo biofísico Leaky Integrate-and-Fire (LIF), desarrollado en Python puro con NumPy para cómputo neuromórfico de ultra bajo consumo y dinámicas temporales.

## 📌 Propósito del Proyecto

Este proyecto implementa una **Neurona Spiking Biológicamente Inspirada** sin depender de librerías de alto nivel. A diferencia de las neuronas artificiales tradicionales que transmiten valores continuos estáticos, este modelo opera con la dimensión del tiempo ($t$):

- **Integración y Fuga (Leaky):** El potencial de membrana $V(t)$ se carga con la corriente de entrada y decae exponencialmente debido a la resistencia de membrana.
- **Disparo de Acciones (Spikes):** Emisión discretizada de impulsos ($0$ o $1$) cuando el voltaje supera el umbral crítico $V_{th}$.
- **Reinicio Biológico (Reset):** Hiperpolarización instantánea del voltaje al estado de reposo tras cada disparo.

## 💼 Aplicaciones en AGI y Cómputo Neuromórfico

Las arquitecturas Spiking son el pilar de la nueva generación de IA biológicamente eficiente (Hacia AGI y Edge Computing):

- **Procesamiento Neuromórfico de Ultra Bajo Consumo:** Event-driven computing en chips de silicio neuromórfico (ej. Intel Loihi), reduciendo el gasto energético de entrenamiento y transmisión.
- **Filtrado Temporal para Agentes y APIs:** Activación asíncrona de sistemas multi-agente; la neurona actúa como un disparador en tiempo real solo cuando la densidad de eventos supera el umbral.
- **Procesamiento de Señales Continuas:** Análisis en tiempo real de series temporales, sensores biomédicos y telemetría de alta frecuencia.

## 🏗️ Arquitectura del Proyecto

```text
neurona_spiking_lif_proyecto/
├── venv/                      # Entorno virtual aislado de Python
├── .gitignore                 # Archivos excluidos del control de versiones
├── neurona_spiking_lif.py     # Lógica diferencial LIF, simulación biofísica y métricas
└── README.md                  # Documentación ejecutiva de nivel producción