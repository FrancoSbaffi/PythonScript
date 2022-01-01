# import os
# from random import randint 

# for i in range(1, 365):
    
#     for j in range(0, randint(1, 10)):
#         d = str(i) + ' days ago'
#         with open('file.txt', 'a') as file:
#             file.write(d)
#         os.system('git add .')
#         os.system('git commit --date="' + d + '" -m "commit"')      
        
# os.system('git push origin master')        

import os
from random import randint
from datetime import datetime, timedelta

# Define la fecha de inicio y fin para la generación de commits (por ejemplo, un año).
fecha_inicio = datetime(2022, 1, 1)
fecha_fin = datetime(2022, 12, 30)

# Itera para generar commits en fechas aleatorias dentro del rango definido.
while fecha_inicio <= fecha_fin:
    # Genera un número aleatorio de commits para el día actual.
    num_commits = randint(1, 10)

    # Crea la fecha y hora del commit dentro del rango deseado.
    fecha_commit = fecha_inicio + timedelta(hours=randint(0, 23), minutes=randint(0, 59), seconds=randint(0, 59))

    for _ in range(num_commits):
        # Formatea la fecha para el commit.
        fecha_str = fecha_commit.strftime('%Y-%m-%d %H:%M:%S')

        # Escribe un mensaje de commit ficticio.
        mensaje_commit = f"Commit en {fecha_str}"

        # Ejecuta los comandos de Git para agregar y confirmar los cambios.
        with open('file.txt', 'a') as file:
            file.write(mensaje_commit + '\n')
        os.system('git add .')
        os.system(f'git commit --date="{fecha_str}" -m "{mensaje_commit}"')

    # Incrementa la fecha en un número aleatorio de días para el siguiente ciclo.
    fecha_inicio += timedelta(days=randint(1, 30))

# Finalmente, empuja los cambios al repositorio remoto.
os.system('git push origin master')
