import random
palabras=("canotaje","deporte","ejercicio","futbolista","pelota","judo","balón")
palabra_aleatoria=random.choice(palabras)

nombre=input("Bienvenido.Cómo te llamas?: ")
intentos=0
max_intentos=12
print(f"Hola {nombre},tienes hasta {max_intentos} para adivinar una palabra")
suposiciones=["_"]*len(palabra_aleatoria)
while intentos<max_intentos:
    suposición=input("Ingrese una letra: ")
    suposición=suposición.lower()
    if len(suposición)!=1:
        print("Por favor ingrese sólo una letra")
    else:
        if suposición in palabra_aleatoria:
           for i in range(len(palabra_aleatoria)):
               if palabra_aleatoria[i]==suposición:
                  suposiciones[i]=palabra_aleatoria[i]
           print("".join(suposiciones))
           if "".join(suposiciones)==palabra_aleatoria:
                print("Felicidades.Adivinaste la palabra.")
                break
        else:
            print("Incorrecto.Adivina otra letra.")
            intentos+=1
if intentos==max_intentos:
   print(f'Has alcanzado el máximo de intentos.La palabra era"{palabra_aleatoria}"')
    
    




               


