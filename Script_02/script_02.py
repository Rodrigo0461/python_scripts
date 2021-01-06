# Version of Python 2.7.16
# Function for add 1.0 to list if is minor than 5

def add_note(largo,lista):
    while largo < 5 :
        lista.append(1.0)
        largo += 1
    return lista


# Open file with notes, this file is a .txt and is open read mode "r"
file = open("/Users/rootdrigo/Documents/Tarea/text.txt", "r")

file_result = open("/Users/rootdrigo/Documents/Tarea/result.txt", "w")

# loops for read line by line
for line in file:
    # Separate elements of list by "," 
    valores=line.strip().split(",")
    # trasform to float 
    valoresInt=list(map(float,valores[1:]))
    # calculate lenght of list
    largo=len(valoresInt)
    # check lenght of list, call to function "add_note"
    listaInt = add_note(largo,valoresInt)
    # sum notes
    sumaNotas=sum(listaInt)
    # media
    media=sumaNotas/len(listaInt)
    # validate approved or reprobate
    aprobado="Aprobado" if media>=4 else "Reprobado"
    # Imprime result to file result.txt
    file_result.write("Alumno: {} - Nota media: {} - {} \n".format(valores[0], media, aprobado))

# close both files
file_result.close()
file.close()
