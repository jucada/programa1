from datetime import datetime


tiempoActual = datetime.now()

miCumple = datetime(año,mes,dia)

tiempoFalta = miCumple-tiempoActual

resultado = tiempoFalta.days *60*60*24 + tiempoFalta.seconds

print(resultado)