# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (2 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1: Tena
        [
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 29}
        ],
        [
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 23}
        ],
        # ... Resto de las semanas ...
    ],
    [   # Ciudad 2: Loreto
        [
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 29}
        ],
        [
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 41}
        ],
        # ... Resto de las semanas ...
    ],
    [   # Ciudad 3: Sacha
        [
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 42},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 41},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 42}
        ],
        [
            {"day": "Lunes", "temp": 39},
            {"day": "Martes", "temp": 41},
            {"day": "Miércoles", "temp": 43},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 41}
        ],
        # ... Resto de las semanas ...
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(["Tena", "Loreto", "Sacha"], 1):
    for j, semana in enumerate(temperaturas[i-1], 1):
        suma_temperaturas = sum(dia['temp'] for dia in semana)
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas para {ciudad}, Semana {j}: {promedio}")
temperaturas = [
    [   # Ciudad 1: Tena
        [
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 29}
        ],
        [
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 23}
        ],
        # ... Resto de las semanas ...
    ],
    [   # Ciudad 2: Loreto
        [
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 29}
        ],
        [
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 41}
        ],
        # ... Resto de las semanas ...
    ],
    [   # Ciudad 3: Sacha
        [
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 42},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 41},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 42}
        ],
        [
            {"day": "Lunes", "temp": 39},
            {"day": "Martes", "temp": 41},
            {"day": "Miércoles", "temp": 43},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 41}
        ],
        # ... Resto de las semanas ...
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(["Tena", "Loreto", "Sacha"], 1):
    for j, semana in enumerate(temperaturas[i-1], 1):
        suma_temperaturas = sum(dia['temp'] for dia in semana)
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas para {ciudad}, Semana {j}: {promedio}")