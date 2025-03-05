import nltk
from nltk.sem.logic import Expression

# Iniciar el analizador
read_expr = Expression.fromstring

# Definir las constantes para fer, ruiz y luz
fer = read_expr('fer')
ruiz = read_expr('ruiz')
luz = read_expr('luz')

# Definir los predicados con las constantes
amigos_fer_ruiz = read_expr('amigos(fer, ruiz)')
no_amigos_fer_luz = read_expr('no_son_amigos(fer, luz)')
mismo_edad_luz_fer = read_expr('tienen_la_misma_edad(luz, fer)')
trabajar_juntos_fer_ruiz = read_expr('trabajan(fer, ruiz)')

# Crear un conjunto de fórmulas
formulas = [
    amigos_fer_ruiz,
    no_amigos_fer_luz,
    mismo_edad_luz_fer,
    trabajar_juntos_fer_ruiz
]

# Imprimir las fórmulas
for formula in formulas:
    print(f"{formula} : {formula}")
