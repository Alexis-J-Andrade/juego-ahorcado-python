# JUEGO DEL AHORCADO 

# IMPORTAMOS LA LIBERIA RANDOM
import random

# LISTA DE PALABRAS
palabras = ["sistema", "codigo", "python", "programacion"]

# ELEGIMOS UNA PALABRA AL AZAR
palabra_secreta = random.choice(palabras)

# GUARDAMOS LAS LETRAS QUE EL USUARIO ADIVINE
letras_adivinadas = []

# NUMERO DE INTENTOS
intentos = 6

print("🎮 Bienvenido al Juego del Ahorcado 🎮")

# EL JUEGO SE EJECUTA MIENTRAS HAYA INTENTOS
while intentos > 0:
    
    # CREAMOS VARIABLE PARA MOSTRAR LA PALABRA
    palabra_mostrada = ""
    
    # RECORREMOS CADA LETRA DE LA PALABRA SECRETA
    for letra in palabra_secreta:
        
        # SI LA LETRA YA FUE ADIVINADA
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        
        # SI NO HA SIDO ADIVINADA
        else:
            palabra_mostrada += "_ "
    
    # MOSTRAMOS LA PALABRA ACTUAL
    print("\nPalabra:", palabra_mostrada)
    
    # SI YA NO HAY GUIONES, EL USUARIO GANÓ
    if "_" not in palabra_mostrada:
        print("¡Felicidades! Ganaste")
        break
    # PEDIMOS UNA LETRA AL USUARIO
    letra_usuario = input("Ingresa una letra: ").lower()

    # SI LA LETRA YA FUE USADA
    if letra_usuario in letras_adivinadas:
        print("Ya usaste esa letra.")
        continue

    # SI LA LETRA ESTÁ EN LA PALABRA
    if letra_usuario in palabra_secreta:
        print("¡Correcto!")
        letras_adivinadas.append(letra_usuario)
    else:
        print(" Incorrecto.")
        intentos -= 1

# SI SE QUEDA SIN INTENTOS
if intentos == 0:
    print("💀 Perdiste.")
    print("La palabra era:", palabra_secreta)
