# Funciones a usar en la sección de Machine Learning

# Tramificación de variables

# Year: 52 nuniques
def year_tram(x):
    if 1970 <= x < 1980:
        return '70s'
    elif 1980 <= x < 1990:
        return '80s'
    elif 1990 <= x < 2000:
        return '90s'
    elif 2000 <= x < 2010:
        return '2000s'
    elif 2010 <= x < 2020:
        return '2010s'
    elif 2020 <= x < 2030:
        return '2020s'
    else:
        return 'Unknown'

#Duration_Days: 296 valores únicos
def duration_days_tram(x):
    if x == 0:
        return 'Inmediato'
    elif 1 <= x <= 7:
        return 'Muy corto (1–7d)'
    elif 8 <= x <= 30:
        return 'Corto (8–30d)'
    elif 31 <= x <= 90:
        return 'Medio (31–90d)'
    else:
        return 'Largo (+90d)'