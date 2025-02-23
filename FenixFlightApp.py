#Simulando capacidade de decolagem aérea de foguete através da criação do Algoritmo FenixFlight.
#Henri De Dantas

import math

# Constantes da Terra
G = 6.674e-11  # Constante gravitacional (m³/kg/s²)
M = 5.972e24   # Massa da Terra (kg)
R = 6.371e6    # Raio da Terra (m)
g0 = 9.81      # Gravidade na superfície (m/s²)

def calcular_arrasto(Cd, densidade_ar, area, velocidade):
    """Calcula a força de arrasto aerodinâmico."""
    return 0.5 * Cd * densidade_ar * area * velocidade**2

def calcular_delta_v(Isp, massa_inicial, massa_final):
    """Usa a equação do foguete de Tsiolkovsky para calcular Delta V."""
    return Isp * g0 * math.log(massa_inicial / massa_final)

def escapar(Isp, empuxo, massa_total, massa_combustivel, Cd, area, densidade_ar, velocidade_vento):
    """Verifica se o foguete pode escapar da atmosfera da Terra."""

    # Calcula a velocidade de escape
    v_escape = math.sqrt(2 * G * M / R)
    
    # Massa final após queima de combustível
    massa_final = massa_total - massa_combustivel
    
    # Cálculo do Delta V do foguete
    delta_v = calcular_delta_v(Isp, massa_total, massa_final)
    
    # Cálculo da força de arrasto no início do lançamento
    velocidade_inicial = 0  # O foguete parte do repouso
    forca_arrasto = calcular_arrasto(Cd, densidade_ar, area, velocidade_inicial + velocidade_vento)
    
    # Exibe os resultados
    print(f"Velocidade necessária para escapar: {v_escape:.2f} m/s")
    print(f"Velocidade máxima do foguete: {delta_v:.2f} m/s")
    print(f"Força de arrasto inicial: {forca_arrasto:.2f} N")
    
    if delta_v >= v_escape:
        print("O foguete irá escapar da atmosfera da Terra.")
        return True
    else:
        print("O foguete não possui potência suficiente para escapar da atmosfera da Terra.")
        return False

# Exemplo de teste (valores aproximados para um foguete) ou pode utilizar os valores que desejar para as variáveis
Isp = 300  # Impulso específico (s)
empuxo = 7e6  # Empuxo do motor (N)
massa_total = 500000  # Massa total do foguete (kg)
massa_combustivel = 400000  # Massa de combustível (kg)
Cd = 0.5  # Coeficiente de arrasto (aerodinâmica)
area = 10  # Área frontal do foguete (m²)
densidade_ar = 1.225  # Densidade do ar ao nível do mar (kg/m³)
velocidade_vento = 10  # Velocidade do vento (m/s)

escapar(Isp, empuxo, massa_total, massa_combustivel, Cd, area, densidade_ar, velocidade_vento)
