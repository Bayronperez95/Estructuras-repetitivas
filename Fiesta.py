import os, msvcrt, sys

asistentes = 0
edad_mas_joven = 0
hombres = 0
mujeres = 0
promedio_hombres = 0
promedio_mujeres = 0
tecla_repetir = b's'
while tecla_repetir==b's' or tecla_repetir==b'S':
    os.system ('cls')
    edad = int (input ('Ingresa el valor de edad: '))
    print ('Selecciona el valor de genero.')
    print ('\t1.- Mujer')
    print ('\t2.- Hombre')
    sys.stdout.write ('\t')
    genero = 0
    while genero<1 or genero>2:
        genero = int (input (': '))
        if genero<1 or genero>2:
            sys.stdout.write ('Valor incorrecto. Ingr\u00E9salo nuevamente.')
    if edad>=18:
        asistentes=asistentes+1
    else:
        print ('No se permiten menores de edad a la fiesta.')
    if genero==1 and edad>=18:
        mujeres=mujeres+1
        promedio_mujeres=promedio_mujeres+edad
    if genero==2 and edad>=18:
        hombres=hombres+1
        promedio_hombres=promedio_hombres+edad
    if edad>=18 and (edad_mas_joven==0 or edad_mas_joven>edad):
        edad_mas_joven=edad
    print ()
    sys.stdout.write ('\u00BFDeseas repetir el proceso? (S/N): ')
    tecla_repetir = b'\0'
    while tecla_repetir!=b's' and tecla_repetir!=b'S' and tecla_repetir!=b'n' and tecla_repetir!=b'N':
        tecla_repetir = msvcrt.getch ()
if hombres == 0:
    promedio_hombres = 0
else:
    promedio_hombres=promedio_hombres/hombres
if mujeres == 0:
    promedio_mujeres = 0
else:
    promedio_mujeres=promedio_mujeres/mujeres
print ('Valor de asistentes: ' + repr (asistentes))
print ('Valor de edad mas joven: ' + repr (edad_mas_joven))
print ('Valor de hombres: ' + repr (hombres))
print ('Valor de mujeres: ' + repr (mujeres))
print ('Valor de promedio hombres: ' + repr (promedio_hombres))
print ('Valor de promedio mujeres: ' + repr (promedio_mujeres))
os.system ('pause')