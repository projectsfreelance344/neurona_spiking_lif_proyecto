import numpy as np

print("--- INICIALIZANDO SIMULADOR DE NEURONA SPIKING (LIF) ---")

# 1. Parámetros Biofísicos de la Membrana
V_rest = -70.0     # Voltaje de reposo (mV)
V_th = -55.0       # Umbral crítico de disparo / Threshold (mV)
V_reset = -70.0    # Voltaje de reinicio tras emisión de spike (mV)
tau = 10.0         # Constante de tiempo de fuga de la membrana (ms)
R = 1.0            # Resistencia de membrana
dt = 1.0           # Intervalo de tiempo de integración (ms)
tiempo_total = 100 # Duración de la simulación (ms)

pasos_tiempo = int(tiempo_total / dt)

# 2. Vector de corriente inyectada I(t)
# Se aplica un pulso de corriente sostenida entre t=10ms y t=80ms
I = np.zeros(pasos_tiempo)
I[10:80] = 18.0  # Intensidad suficiente para vencer la fuga y superar V_th

# 3. Inicialización de estado y registros
V = V_rest
historial_V = []
spikes = []

print("Simulando acumulación de carga y potencial de acción a través del tiempo...")

# 4. Simulación paso a paso (Integración discreta de Euler)
for t in range(pasos_tiempo):
    # Ecuación diferencial discreta: dV = (-(V - V_rest) + R * I[t]) / tau * dt
    dV = (-(V - V_rest) + R * I[t]) / tau * dt
    V += dV
    
    # Mecanismo de disparo (Spike Generator) y reinicio
    if V >= V_th:
        spikes.append(1)
        V = V_reset  # Colapso/reinicio biológico
    else:
        spikes.append(0)
        
    historial_V.append(V)

# 5. Cálculo de métricas biofísicas
total_spikes = sum(spikes)
tasa_disparo_hz = (total_spikes / tiempo_total) * 1000.0  # Hz (Spikes por segundo)

print("\n--- SIMULACIÓN BIOLÓGICA FINALIZADA ---")
print(f"Tiempo total simulado: {tiempo_total} ms")
print(f"Total de impulsos (Spikes) emitidos: {total_spikes}")
print(f"Frecuencia de disparo calculada: {tasa_disparo_hz:.2f} Hz")