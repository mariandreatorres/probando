from datetime import datetime
tiempo_actual = datetime.now()
micumple = datetime(2023,9,27)
tiempofalta = micumple-tiempo_actual
print(tiempofalta.days*60*60*24+tiempofalta.seconds)
