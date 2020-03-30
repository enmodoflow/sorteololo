from datetime import date, datetime

def transformarHora(fecha):
    año = fecha.year
    mes = fecha.month
    dia = fecha.day
    hora = fecha.hour
    minutos = fecha.minute
    segundos = fecha.second
    fecha_hoy = datetime.now()
    dia_hoy = fecha_hoy.day
    fecha_x = datetime(año, mes, dia, hora, minutos, segundos)
    resultado = fecha_hoy - fecha_x
    separar = str(resultado).split()
    lista = []
    for i in separar:
        try:
            int(i)
            lista.append(int(i))
        except:
            pass
        if i == 'days,':
            tiempo = 'dias'
        elif i == 'day,':
            tiempo = 'dia'
    minutos = str(minutos)
    if len(minutos) == 1:
        minutos = (f'0{minutos}')
    try:
        if tiempo == 'dias':
            return (f'aace {lista[0]} días')
        elif tiempo == 'dia':
            return (f'ayer a las {hora}:{minutos}')
    except:
        if dia_hoy == dia:
            return (f'hoy a las {hora}:{minutos}')
        else:
            return (f'ayer a las {hora}:{minutos}')

def calcular30dias(fecha):
    año = fecha.year
    mes = fecha.month
    dia = fecha.day
    hora = fecha.hour
    minutos = fecha.minute
    segundos = fecha.second
    fecha_hoy = datetime.now()
    dia_hoy = fecha_hoy.day
    fecha_x = datetime(año, mes, dia, hora, minutos, segundos)
    resultado = fecha_hoy - fecha_x
    separar = str(resultado).split()
    lista = []
    for i in separar:
        try:
            int(i)
            lista.append(int(i))
        except:
            pass
        if i == 'days,':
            tiempo = 'dias'
        elif i == 'day,':
            tiempo = 'dia'
    minutos = str(minutos)
    if len(minutos) == 1:
        minutos = (f'0{minutos}')
    try:
        if tiempo == 'dias':
            if lista[0] > 29:
                return True
            else:
                return False
        else:
            return False
    except:
        return False