TEMPERATURA = [
    [# LORETO
        [# SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 37},
            {"DIA": "MARTES", "TEMPERATURA": 36},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 32},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 26},
            {"DIA": "DOMINGO", "TEMPERATURA": 28}
        ],
        [# SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 38},
            {"DIA": "MIERCOLES", "TEMPERATURA": 32},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 31},
            {"DIA": "SABADO", "TEMPERATURA": 22},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
        [# SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 39},
            {"DIA": "MARTES", "TEMPERATURA": 38},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 32},
            {"DIA": "VIERNES", "TEMPERATURA": 35},
            {"DIA": "SABADO", "TEMPERATURA": 33},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 31},
            {"DIA": "MARTES", "TEMPERATURA": 32},
            {"DIA": "MIERCOLES", "TEMPERATURA": 33},
            {"DIA": "JUEVES", "TEMPERATURA": 34},
            {"DIA": "VIERNES", "TEMPERATURA": 35},
            {"DIA": "SABADO", "TEMPERATURA": 36},
            {"DIA": "DOMINGO", "TEMPERATURA": 37}
        ],
    ],
    [# SACHA
        [# SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 38},
            {"DIA": "MARTES", "TEMPERATURA": 38},
            {"DIA": "MIERCOLES", "TEMPERATURA": 40},
            {"DIA": "JUEVES", "TEMPERATURA": 39},
            {"DIA": "VIERNES", "TEMPERATURA": 38},
            {"DIA": "SABADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 41}
        ],
        [# SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 40},
            {"DIA": "MARTES", "TEMPERATURA": 39},
            {"DIA": "MIERCOLES", "TEMPERATURA": 39},
            {"DIA": "JUEVES", "TEMPERATURA": 39},
            {"DIA": "VIERNES", "TEMPERATURA": 38},
            {"DIA": "SABADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 40}
        ],
        [# SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 38},
            {"DIA": "MARTES", "TEMPERATURA": 39},
            {"DIA": "MIERCOLES", "TEMPERATURA": 40},
            {"DIA": "JUEVES", "TEMPERATURA": 41},
            {"DIA": "VIERNES", "TEMPERATURA": 40},
            {"DIA": "SABADO", "TEMPERATURA": 41},
            {"DIA": "DOMINGO", "TEMPERATURA": 39}
        ],
        [# SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 39},
            {"DIA": "MARTES", "TEMPERATURA": 38},
            {"DIA": "MIERCOLES", "TEMPERATURA": 38},
            {"DIA": "JUEVES", "TEMPERATURA": 39},
            {"DIA": "VIERNES", "TEMPERATURA": 40},
            {"DIA": "SABADO", "TEMPERATURA": 40},
            {"DIA": "DOMINGO", "TEMPERATURA": 39}
        ],
    ],
    [# LAGO
        [# SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 40},
            {"DIA": "MARTES", "TEMPERATURA": 38},
            {"DIA": "MIERCOLES", "TEMPERATURA": 40},
            {"DIA": "JUEVES", "TEMPERATURA": 41},
            {"DIA": "VIERNES", "TEMPERATURA": 40},
            {"DIA": "SABADO", "TEMPERATURA": 40},
            {"DIA": "DOMINGO", "TEMPERATURA": 39}
        ],
        [# SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 39},
            {"DIA": "MARTES", "TEMPERATURA": 38},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 39},
            {"DIA": "VIERNES", "TEMPERATURA": 38},
            {"DIA": "SABADO", "TEMPERATURA": 37},
            {"DIA": "DOMINGO", "TEMPERATURA": 36}
        ],
        [# SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 40},
            {"DIA": "MARTES", "TEMPERATURA": 40},
            {"DIA": "MIERCOLES", "TEMPERATURA": 39},
            {"DIA": "JUEVES", "TEMPERATURA": 40},
            {"DIA": "VIERNES", "TEMPERATURA": 38},
            {"DIA": "SABADO", "TEMPERATURA": 37},
            {"DIA": "DOMINGO", "TEMPERATURA": 36}
        ],
        [# SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 41},
            {"DIA": "MARTES", "TEMPERATURA": 40},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 40},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SABADO", "TEMPERATURA": 38},
            {"DIA": "DOMINGO", "TEMPERATURA": 39}
        ],
    ],
]
suma_temperatura = float()
peomedio_semanal = float()
c = int()
x = int()
for ciudad in TEMPERATURA:
    x += 1
    if x == 1:
        print("=========================================================")
        print("PROMEDIO SEMANAL DE TEMPERATURAS DE LA CIUDAD DE LORETO")
        print("=========================================================")
    if x == 2:
        print("=========================================================")
        print("PROMEDIO SEMANAL DE TEMPERATURAS DE LA CIUDAD SACHA")
        print("=========================================================")
    if x == 3:
        print("=========================================================")
        print("PROMEDIO SEMANAL DE TEMPERATURAS DE LA CIUDAD LAGO")
        print("=========================================================")
    for semana  in ciudad:
        c +=1
        for dia in semana:
            suma_temperatura += dia["TEMPERATURA"]
        promedio_semanal = suma_temperatura / 7
        print(f"La semana {c}, tuvo un promedio de temperatura {promedio_semanal}")
        print()
        suma_temperatura = 0
    c=0