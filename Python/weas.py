# -*- coding: cp1252 -*-
import random
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
palabras = 'sombra animal django oveja aprender ejercicios caballo perro vaca computadora python abeja diente conejo mantel mesa basura escritorio ubuntu gorro parque amuleto cama cuarto descargar curso diario pythondiario vaso cuadro foto revista esdrujula parlantes radio tutorial banana naranja manzana celular casco ventana silla pileta juegos televisor heladera modulos cocina timbre lavarropas estufa enchufe futbol pelota pizarron cargador factura papel impresora telefono remedio planta vegetal aves luna electricidad copa fernet google lenguaje internet esposa jarra microondas manual sarten cortina musica pato'.split()

def buscarPalabraAleat(listaPalabras):
    # Esta funcion retorna una palabra aleatoria.
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]

def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(AHORCADO[len(letraIncorrecta)])
    print ""
    fin = " "
    print 'Letras incorrectas:', fin
    for letra in letraIncorrecta:
        print (letra, fin)
    print ""
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)): # Remplaza los espacios en blanco por la letra bien escrita
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print (letra, fin)
    print ""

def elijeLetra(algunaLetra):
    # Devuelve la letra que el jugador ingreso. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
    while True:
        print 'Adivina una letra:'
        letra = raw_input()
        letra = letra.lower()
        if len(letra) != 1:
            print 'Introduce una sola letra.' 
        elif letra in algunaLetra:
            print 'Ya has elegido esa letra, elige otra.'
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print 'Elije una letra.' 
        else:
            return letra

def empezar():
    # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    print 'Quieres jugar de nuevo? (Si o No)' 
    return raw_input().lower().startswith('s')

print 'A H O R C A D O' 
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = buscarPalabraAleat(palabras)
finJuego = False
while True:
    displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
    # El usuairo elije una letra.
    letra = elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in palabraSecreta:
        letraCorrecta = letraCorrecta + letra
        # Se fija si el jugador gano
        letrasEncontradas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print ('Si! La palabra secreta es "' + palabraSecreta + '"! Has ganado!')
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
        if len(letraIncorrecta) == len(AHORCADO) - 1:
            displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
            print ('Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
            finJuego = True
    # Pregunta al jugador si quiere jugar de nuevo
    if finJuego:
        if empezar():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            palabraSecreta = buscarPalabraAleat(palabras)
        else:
            break
