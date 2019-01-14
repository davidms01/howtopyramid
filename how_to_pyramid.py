def ejercicio2():
    j = 2
    number_of_tries = int (input ())
    # Numero de intentos
    numeros = []
    for i in range (number_of_tries):
        numeros.append (int (input()))
        # Guardo cada intento
    for i in range (len(numeros)):
        # Para cada intento:
        # Mantengo dos contadores: latas y latas previas.
        # Cuando sobrepase el número de latas apilables,
        # Resto al resultado la cantidad de latas anterior
        result = numeros[i]
        latas_pre = 1
        latas = 1
        incremento = 2
        while latas <= result:
            latas_pre = latas
            latas += incremento
            incremento += 1
        resto = result - latas_pre
        print (resto)

ejercicio2()
