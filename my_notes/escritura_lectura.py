# Escritura de Archivo de Texto
with open('my_notes.txt', 'w') as file:
    file.write("Nota 1: Hoy es buen dia para aprender cosas nuevas.\n")
    file.write("Nota 2: No dejes para mañana las cosas que puedes hacer hoy.\n")
    file.write("Nota 3: Disfruta hoy talvez mañana no llegues a compartir.\n")

# Lectura de Archivo de Texto
with open('my_notes.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Cierre de Archivo
file.close()