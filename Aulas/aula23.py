# CONSTANTEE = 'VARIAVEIS' que não vão mudar
# Muitas condições no mesmo if (ruim)
#     <-COntagem de complexidade (ruim)

velocidade = 65 #velocidade atual do carro
local_carro = 98 #local em que o carro está na estrada

RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 #velocidade onde o radar 1 está
RADAR_RANGE = 1 # A distancia onde o radar pega

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE) and\
        velocidade > RADAR_1:
    print('carro multado em radar 1')
