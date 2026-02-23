# JUEGO DEL AHORCADO 

# IMPORTAMOS LA LIBRERÍA RANDOM
import random

# LISTA DE PALABRAS
palabras = ["sistema", "codigo", "python", "programacion"]

# ELEGIMOS UNA PALABRA AL AZAR
palabra_secreta = random.choice(palabras)

# GUARDAMOS TODAS LAS LETRAS QUE EL USUARIO INGRESE
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
    
    # MOSTRAMOS LA PALABRA ACTUAL Y LOS INTENTOS
    print("\nPalabra:", palabra_mostrada)
    print(f"Tienes {intentos} intentos restantes.")
    
    # SI YA NO HAY GUIONES, EL USUARIO GANÓ
    if "_" not in palabra_mostrada:
        print("\n🏆 ¡Felicidades! Ganaste 🏆")
        break
        
    # PEDIMOS UNA LETRA AL USUARIO
    letra_usuario = input("Ingresa una letra: ").lower()

    # NUEVO FUNCIONALIDADES DE VALIDACIÓN
    
    # 1. Verificamos que sea solo UNA letra
    if len(letra_usuario) != 1:
        print("⚠️ Error: Solo puedes ingresar UNA letra a la vez.")
        continue # El 'continue' hace que el bucle vuelva a empezar sin restar intentos
        
    # 2. Verificamos que sea realmente una letra (y no números ni espacios)
    if not letra_usuario.isalpha():
        print("⚠️ Error: Debes ingresar letras, no se permiten números ni símbolos.")
        continue

    # 3. SI LA LETRA YA FUE USADA (Correcta o incorrecta)
    if letra_usuario in letras_adivinadas:
        print("⚠️ Ya usaste esa letra. Intenta con otra.")
        continue

    # AGREGAMOS LA LETRA A LA LISTA DE USADAS
    letras_adivinadas.append(letra_usuario)

    # SI LA LETRA ESTÁ EN LA PALABRA
    if letra_usuario in palabra_secreta:
        print("✅ ¡Correcto!")
    # SI LA LETRA NO ESTÁ EN LA PALABRA
    else:
        print("❌ Incorrecto.")
        intentos -= 1

# SI SE QUEDA SIN INTENTOS (FUERA DEL BUCLE WHILE)
if intentos == 0:
    print("\n💀 Perdiste.")
    print("La palabra era:", palabra_secreta)
