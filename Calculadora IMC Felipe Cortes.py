#El primer paso es establecer las variables
nombre = input ("Introduce tu nombre: ")
apellido_materno = input ("Introduce tu primer apellido: ")
apellido_paterno= input ("Introduce tu segundo apellido: ")
edad = input ("Introduce tu edad: ")
estatura = float(input("Introduce tu estatura: "))
peso = float(input("Introduce tu peso: "))

#El segundo paso es incluir la función  con la fórmula para calcular el IMC. Gracias al ejemplo de IMC enviado con el ejercicio pude investigar sobre funciones 
#y darme cuenta de que en este caso la función con el parametro automatiza el proceso par calcular el IMC.
def calculo(peso,estatura):
    resultado = peso/(estatura**2)
    return resultado

resultado = calculo(peso,estatura)

def mensaje(resultado): #Como vimos en clase con operadores de comparación podemos establecer un valor que indique cuándo hay un bajo o alto peso
    if resultado < 18.5: 
       resul = print("Bajo peso")
    elif resultado < 24.9:
        resul = print("Normal")
    elif resultado < 29.9:
        resul = print("Sobrepeso")
    else: 0
    return resul


#El tercer paso muestra la información solicitada y así en la terminal se puede poner la información solicitada
print("Nombre: " + nombre)
print("apellido_materno: " + apellido_materno)
print("apellido_paterno: " + apellido_paterno)
print("Tengo: " + str(edad) + "años")  #Casteo con str para poder obtener el número de la edad
print("Peso: " + str(peso))
print(resultado)
resul = mensaje(resultado)
