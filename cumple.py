from datetime import datetime

def calcularCumple(año, mes, dia):
    tiempoActual = datetime.now()

    miCumple = datetime(año,mes,dia)

    tiempoFalta = miCumple-tiempoActual

    resultadoMinutos = tiempoFalta.days * 60*24 + tiempoFalta.seconds//60

    return resultadoMinutos