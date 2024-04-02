import os

ls_bodega_1 = []
ls_bodega_2 = []
sw = True
def fnt_registrar():
    año = input('Ingrese el año del vehiculo: ')
    fabricante = input('1. Chevrolet\n2. Ford\n3. Renault\n4. Dodge\n5. Hyundai\n6. Fiat\n-> ')
    modelo = input('Ingrese el modelo del vehiculo\n-> ')
    motor = input('Ingrese el numero del motor\n-> ')
    if año == '2024' and (fabricante =='1'or fabricante =='2' or fabricante == '3'):
        ls_bodega_1.append([año, modelo, motor, fabricante])
        enter = input('Vehiculo registrado con exito >>>ENTER<<<')

while sw == True:
    os.system('cls')
    opcion = input('\n1. Registrar\n2. Mostrar\n->')
    if opcion == '1':
        fnt_registrar()
