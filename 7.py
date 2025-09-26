# IMC = peso (kg) / altura^2 (m^2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print("Su índice de masa corporal (IMC) es: ", imc)