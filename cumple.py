from datetime import datetime

def calcular_cumple(anio,mes,dia):
    tiempo_actual = datetime.now()
    micumple = datetime(anio,mes,dia)
    tiempofalta = micumple-tiempo_actual
    resultado = tiempofalta.days*60*24+tiempofalta.seconds//60
    return resultado