def asignar_practica(tupla):
    Grace = []
    Barbara = []
    Alan = []
    for i in range(len(tupla)):
        if tupla[i][3] == "Grace":
            Grace.append(tupla[i])
        elif tupla[i][3] == "Barbara":
            Barbara.append(tupla[i])
        elif tupla[i][3] == "Alan":
            Alan.append(tupla[i])

    return
