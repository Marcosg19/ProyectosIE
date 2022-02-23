import math

import psycopg2
#Conexión a base de datos
try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "marcos2001",
        dbname = "proyectosIE"  
    )
    print('Conexión exitosa con la base de datos')
except psycopg2.Error as e:
    print('Ocurrió un error en la conexión')
    print('Verifique los parametros')


cursor = conexion.cursor()

#Función para pedir opciones a menú principal
def opciones():
    detenerop = False
    num = 0
    while not detenerop:
        try:
            detenerop = True    
            num = int(input('\nIngrese una opción: '))
        except ValueError:
            print('\nSeleccione una opción valida')
    return num

#Primer Ejercicio
def ejercicio1():
    detenera = True
    detenerb = True
    detenerc = True
    archivo.write('\n')
    while detenera:
        try:
            a=float(input('\nIngrese primer número: '))
            archivo.write('\nPrimer número: ' + str(a))
            detenera = False
        except ValueError:
            print('Caracter invalido...')
            detenera = True
    
    while detenerb:
        try:
            b=float(input('\nIngrese segundo número: '))
            archivo.write('\nSegundo número: ' + str(b))
            detenerb = False
        except ValueError:
            print('Caracter invalido...')
            detenerb= True

    while detenerc:
        try:
            c=float(input('\nIngrese tercer número: '))
            archivo.write('\nTercer número: ' + str(c))
            detenerc = False
        except ValueError:
            print('Caracter invalido...')
            detenerc = True

    if a > b > c:
        print('\nLa suma de los tres números es: ', a+b+c)
        archivo.write('\nLa suma es: ' + str(a+b+c))    

    elif a > c > b:
        print('\nLa suma de los tres números es: ', a+b+c)
        archivo.write('\nLa suma es: ' + str(a+b+c))

    elif b > a > c: 
        print('\nLa multiplicación de los tres números es: ', a*b*c)
        archivo.write('\nLa multiplicación es: ' + str(a*b*c))

    elif b > c > a: 
        print('\nLa multiplicación de los tres números es: ', a*b*c)
        archivo.write('\nLa multiplicación es: ' + str(a*b*c))


    elif c > a > b:
        conc_a = (str(a)+ ',')
        conc_b = (str(b)+ ',')
        conc_c = (str(c)) 
        concatenacion = conc_a + conc_b + conc_c
        print('\nLa concatenación de los números es: ' , concatenacion)
        archivo.write('\nLa multiplicación es: ' + str(a*b*c))

    elif c > b > a:
        conc_a = (str(a)+ ',')
        conc_b = (str(b)+ ',')
        conc_c = (str(c)) 
        concatenacion = conc_a + conc_b + conc_c
        print('\nLa concatenación de los números es: ' , concatenacion)
        archivo.write('\nLa concatenación es: ' + str(concatenacion))

    elif a == b != c: 
        print('\nAl ser iguales el primer y segundo número se muestra el tercero: ', c)
        archivo.write('\nAl ser iguales el primer y segundo número se muestra el tercero: ' + str(c))


    elif a == c != b: 
        print('\nAl ser iguales el primer y tercer número se muestra el segundo: ', b)
        archivo.write('\nAl ser iguales el primer y tercer número se muestra el segundo: ' + str(b))

    elif b == c != a: 
        print('\nAl ser iguales el segundo y tercer número se muestra el primero: ', a)
        archivo.write('\nAl ser iguales el segundo y tercer número se muestra el primero: ' + str(a))

    elif a == b == c: 
        print('\n',(a, b, c))
        print('Todos son iguales\n')
        archivo.write('\nTodos son iguales: ' + str(a)+ ',' + str(b) + ',' + str(c))


#Segundo Ejercicio
def divisores():
    archivo.write('\n')
    detenerd1 = True
    while detenerd1:
        try:
            d= int(input('\nIngrese un numero entero: '))
            archivo.write('\nNúmero entero ingresado: ' + str(d))
            resultado_div = [i for i in range(1, d + 1) if d % i == 0]
            detenerd1 = False
        except ValueError:
            print('\nCaracter invalido...')
            detenerd1 = True

    print('Divisores: ', resultado_div)
    archivo.write('\nDivisores: ' + str(resultado_div))

#Tercer Ejercicio
def conteo_vocales():
    vocales = 'AEIOUaeiou'
    archivo.write('\n')
    detenercv1 = True
    while detenercv1:
        try:
            v= str(input('\nIngrese una palabra: '))
            archivo.write('\nPalabra ingresada: ' + str(v))
            resultado = [c for c in v if c in vocales]
            detenercv1 = False
        except ValueError:
            print('\nCaracter invalido...')
            detenercv1 = True

    print("\nLa palabra "+ str(v) +" tiene" ,str(len(resultado))+ ' vocales '+ str(resultado))
    archivo.write('\nLa palabra '+ str(v) +' tiene ' + str(len(resultado))+ ' vocales')

#Cuarto Ejercicio
def suma_consecutiva():
    archivo.write('\n')
    detenersc1 = True
    while detenersc1:
        try:
            print('\nNOTA: Resultado = 1+2+3+...+n')
            f= int(input('\nIngrese un numero entero: '))
            archivo.write('\nNúmero entero ingresado: ' + str(f))
            s=0 #s inicia en 0
            i=1
            while (i<=f):
                s=s+i
                i=i+1
                detenersc1 = False
        except ValueError:
            print('\nCaracter invalido...')
            detenersc1 = True

    print('\nResultado: ', s)
    archivo.write('\nResultado: ' + str(s))

#Quinto Ejercicio
def inicio_fin():
    detener_if1 = True
    detener_if2 = True
    archivo.write('\n')
    while detener_if1:
        try:
            h=int(input('\nIngrese número de inicio: '))
            archivo.write('\nNúmero de inicio: ' + str(h))
            detener_if1 = False
        except ValueError:
            print('Caracter invalido...')
            detener_if1 = True
    
    while detener_if2:
        try:
            g=int(input('\nIngrese número de fin: '))
            archivo.write('\nNúmero de fin: ' + str(g))
            detener_if2 = False
        except ValueError:
            print('Caracter invalido...')
            detener_if2 = True 

    if h > g:
        resultado_if= [i for i in range(h, g-1, -2) if i%1==0]
        print('\nResultado: ',str(resultado_if))
        archivo.write('\nResultado: ' + str(resultado_if))

    elif h < g:
        resultado_if2= [i for i in range(h, g+1, 2) if i%1==0]
        print('\nResultado: ',str(resultado_if2))
        archivo.write('\nResultado: ' + str(resultado_if2))

    elif h == g:
        resultado_if3= [i for i in range(h, g+1) if i%1==0]
        print('\nResultado: ',str(resultado_if3))
        print('El número de inicio es el mismo que el fin')
        archivo.write('\nEl numero de inicio es el mismo que el fin ' )


#Sexto Ejercicio
def mayor():
    detener_m1 = True
    detener_m2 = True
    archivo.write('\n')
    while detener_m1:
        try:
            m=int(input('\nIngrese primer número: '))
            archivo.write('\nPrimer número: ' + str(m))
            detener_m1 = False
        except ValueError:
            print('Caracter invalido...')
            detener_m1 = True
    
    while detener_m2:
        try:
            n=int(input('\nIngrese segundo número: '))
            archivo.write('\nSegundo número: ' + str(n))
            detener_m2 = False
        except ValueError:
            print('Caracter invalido...')
            detener_m2 = True 

    if m>n:
        resultado_m= [i for i in range(m, n-1, -1) if i%1==0]
        print('\nResultado: ',str(resultado_m))
        archivo.write('\nResultado: ' + str(resultado_m))

    elif m<n:
        resultado_n= [i for i in range(n, m-1, -1) if i%1==0]
        print('\nResultado: ',str(resultado_n))
        archivo.write('\nResultado: ' + str(resultado_n))

    elif m==n:
        print('\nLos números que ingresó son iguales ')
        archivo.write('\nLos números que ingresó son iguales ')
        

#Septimo Ejercicio
def veces_vocales():
    vocales2 = 'AEIOUaeiou'
    archivo.write('\n')
    detener_cv = True
    while detener_cv:
        try:
            v= str(input('\nIngrese una palabra: '))
            archivo.write('\nPalabra ingresada: ' + str(v))
            resultado_cv = [c for c in v if c in vocales2]
            detener_cv = False
        except ValueError:
            print('\nCaracter invalido...')
            detener_cv = True

        cantidad_a= v.count('a')
        cantidad_A= v.count('A')
        cantidad_e= v.count('e')
        cantidad_E= v.count('E')
        cantidad_i= v.count('i')
        cantidad_I= v.count('I')
        cantidad_o= v.count('o')
        cantidad_O= v.count('O')
        cantidad_u= v.count('u')
        cantidad_U= v.count('U')

    print("\nLa palabra "+ str(v) +" tiene" ,str(len(resultado_cv))+ ' vocales '+ str(resultado_cv) )
    archivo.write('\nLa palabra '+ str(v) +' tiene ' + str(len(resultado_cv))+ ' vocales')

    print('\na: ',cantidad_a+cantidad_A)
    archivo.write('\na: '+ str(cantidad_a+cantidad_A))
    print('e: ',cantidad_e+cantidad_E)
    archivo.write('\ne: '+ str(cantidad_e+cantidad_E))
    print('i: ',cantidad_i+cantidad_I)
    archivo.write('\ni: '+ str(cantidad_i+cantidad_I))
    print('o: ',cantidad_o+cantidad_O)
    archivo.write('\no: '+ str(cantidad_o+cantidad_O))
    print('u: ',cantidad_u+cantidad_U)
    archivo.write('\nu: '+ str(cantidad_u+cantidad_U))


#Octavo Ejercicio
def impares():
    archivo.write('\n')

    resultado_if= [i for i in range(0, 100+1) if i%2!=0]
    
    print('\nHistorial de número impares del 1 al 100:\n',str(resultado_if))
    print('\nHay',str(len(resultado_if))+ ' números impares')
    archivo.write('\nResultado: ' + str(resultado_if))
    archivo.write('Hay',str(len(resultado_if))+ ' números impares')

#Noveno Ejercicio
def triangulo():
    detener_t1 = True
    detener_t2 = True
    detener_t3 = True
    archivo.write('\n')
    while detener_t1:
        try:
            p=int(input('\nIngrese primer número: '))
            archivo.write('\nPrimer número: ' + str(p))
            detener_t1 = False
            if p < 0:
                print('Ingresar un número positivo... ')
                detener_t1 = True
            if p == 0:
                print('No puede ser 0...')
                detener_t1 = True
        except ValueError:
            print('Caracter invalido...')
            detener_t1 = True
        

    while detener_t2:
        try:
            q=int(input('\nIngrese segundo número: '))
            archivo.write('\nSegundo número: ' + str(q))
            detener_t2 = False
            if q < 0:
                print('Ingresar un número positivo... ')
                detener_t2 = True
            if q == 0:
                print('No puede ser 0...')
                detener_t2 = True
        except ValueError:
            print('Caracter invalido...')
            detener_t2 = True 
        

    while detener_t3:
        try:
            r=int(input('\nIngrese tercer número: '))
            archivo.write('\nTercer número: ' + str(r))
            detener_t3 = False
            if r < 0:
                print('Ingresar un número positivo... ')
                detener_t3 = True
            if r == 0:
                print('No puede ser 0...')
                detener_t3 = True
        except ValueError:
            print('Caracter invalido...')
            detener_t3 = True 

    if p > q > r:
        print('\nTriángulo escaleno ')
        archivo.write('\nTriángulo escaleno')

    elif p > r > q:
        print('\nTriángulo escaleno ')
        archivo.write('\nTriángulo escaleno')

    elif q > p > r:
        print('\nTriángulo escaleno ')
        archivo.write('\nTriángulo escaleno')

    elif q > r > p:
        print('\nTriángulo escaleno ')
        archivo.write('\nTriángulo escaleno')

    elif r > p > q:
        print('\nTriángulo escaleno ')
        archivo.write('\nTriángulo escaleno')

    elif r > q > p:
        print('\nTriángulo escaleno ')
        archivo.write('\nTriángulo escaleno')

    elif q > p > r:
        print('\nTriángulo escaleno ')
        archivo.write('\nTriángulo escaleno')

    elif p == q == r:
        print('\nTriángulo equilátero ')
        archivo.write('\nTriángulo equilátero')

    elif p == q > r:
        print('\nTriángulo isósceles ')
        archivo.write('\nTriángulo isósceles')

    elif p == q < r:
        print('\nTriángulo isósceles ')
        archivo.write('\nTriángulo isósceles')

    elif p == r < q:
        print('\nTriángulo isósceles ')
        archivo.write('\nTriángulo isósceles')

    elif p == r > q:
        print('\nTriángulo isósceles ')
        archivo.write('\nTriángulo isósceles')

    elif q == r > p:
        print('\nTriángulo isósceles ')
        archivo.write('\nTriángulo isósceles')

    elif q == r < p:
        print('\nTriángulo isósceles ')
        archivo.write('\nTriángulo isósceles')


#Decimo ejercicio
def factorial():
    detener_f1 = True
    archivo.write('\n')
    while detener_f1:
        try:
            x=int(input('\nIngrese un número: '))
            archivo.write('\nNúmero ingresado: ' + str(x))
            detener_f1 = False
            if x %7 != 0:
                print('ERROR: El número ingresado no es divible entre 7. Ingresé nuevamente un número... ')
                detener_f1 = True
        except ValueError:
            print('Caracter invalido...')
            detener_f1 = True
        

    if x%7 == 0:
        fact=1
        if x>=0:
            for i in range(1, x+1):
                fact=fact*i
        print(f"Factorial de {x} es:",fact)
        archivo.write(f"\nFactorial de {x} es:"+str(fact))


#Ejercicio 11
def area_circulo():
    detener_ac = True
    archivo.write('\n')
    while detener_ac:
        try:
            r=float(input('\nIngrese el valor de radio: '))
            archivo.write('\nPrimer número: ' + str(r))
            detener_ac = False
        except ValueError:
            print('Caracter invalido...')
            detener_ac = True

    print('El área es: ',math.pi*r**2)
    archivo.write("\nEl área es: "+str(math.pi*r**2))

def area_triangulo():
    detener_at1 = True
    detener_at2 = True
    archivo.write('\n')
    while detener_at1:
        try:
            b=float(input('\nIngrese el valor de base: '))
            archivo.write('\nPrimer número: ' + str(b))
            detener_at1 = False
        except ValueError:
            print('Caracter invalido...')
            detener_at1 = True

    while detener_at2:
        try:
            h=float(input('\nIngrese el valor de altura: '))
            archivo.write('\nPrimer número: ' + str(h))
            detener_at2 = False
        except ValueError:
            print('Caracter invalido...')
            detener_at2 = True

    print('El área es: ',(b*h)/2)
    archivo.write("\nEl área es: "+str((b*h)/2))
    
def area_cuadrado():
    detener_ac1 = True
    archivo.write('\n')
    while detener_ac1:
        try:
            l=float(input('\nIngrese el valor de L: '))
            archivo.write('\nPrimer número: ' + str(l))
            detener_ac1 = False
        except ValueError:
            print('Caracter invalido...')
            detener_ac1 = True

    print('El área es: ',l**2)
    archivo.write("\nEl área es: "+str(l**2))

def area_rectangulo():
    detener_ar1 = True
    detener_ar2 = True
    archivo.write('\n')
    while detener_ar1:
        try:
            b=float(input('\nIngrese el valor de base: '))
            archivo.write('\nPrimer número: ' + str(b))
            detener_ar1 = False
        except ValueError:
            print('Caracter invalido...')
            detener_ar1 = True

    while detener_ar2:
        try:
            h=float(input('\nIngrese el valor de altura: '))
            archivo.write('\nPrimer número: ' + str(h))
            detener_ar2 = False
        except ValueError:
            print('Caracter invalido...')
            detener_ar2 = True

    print('El área es: ',b*h)
    archivo.write("\nEl área es: "+str(b*h))

def calculadora_areas():
        print('\nENTRAR A CALCULADORA DE AREAS')
        input()
        detener_w = True
        while detener_w:
            print('\n      CALCULADORA DE AREAS')
            print('-------------------------------')
            print('Opciones para calcular área')
            print('\n1. Circulo ')
            print('2. Triángulo')
            print('3. Cuadrado')
            print('4. Rectángulo')
            print('5. Ver historial')
            print('6. Salir')
                        

            opcion_ca = opciones()

            if opcion_ca == 1:
                    area_circulo()

            elif opcion_ca == 2:
                    area_triangulo()

            elif opcion_ca == 3:
                    area_cuadrado()

            elif opcion_ca == 4:
                    area_rectangulo()

            elif opcion_ca == 5:
                    print()

            elif opcion_ca == 6:
                    print('\n>>>CERRANDO PROGRAMA<<<\n')
                    detener_w = False

            else:
                    print('\nIngrese una opción válida')
                    input()


#Ejercicio 12
def notas():
    detenera = True
    detenerb = True
    detenerc = True
    archivo.write('\n')
    while detenera:
        try:
            a=int(input('\nIngrese primer número: '))
            archivo.write('\nPrimer número: ' + str(a))
            detenera = False
            if a < 0:
                print('Calificación invalida...')
                detenera = True
            elif a > 100:
                print('Calificación invalida...')
                detenera = True 
        except ValueError:
            print('Caracter invalido...')
            detenera = True

    
    while detenerb:
        try:
            b=int(input('\nIngrese segundo número: '))
            archivo.write('\nSegundo número: ' + str(b))
            detenerb = False
            if b < 0:
                print('Calificación invalida...')
                detenerb = True
            elif b > 100:
                print('Calificación invalida...')
                detenerb = True 
        except ValueError:
            print('Caracter invalido...')
            detenerb= True


    while detenerc:
        try:
            c=int(input('\nIngrese tercer número: '))
            archivo.write('\nTercer número: ' + str(c))
            detenerc = False
            if c < 0:
                print('Calificación invalida...')
                detenerc = True
            elif c > 100:
                print('Calificación invalida...')
                detenerc = True             
        except ValueError:
            print('Caracter invalido...')
            detenerc = True

    resultado_promedio = (a+b+c)/3

    if resultado_promedio >= 60:
        print('\nPromedio: ',resultado_promedio)
        archivo.write('\nPromedio: ' + str(resultado_promedio))
        print('\nAprobado')
        archivo.write('\nAprobado')
    else:
        print('\nPromedio: ',resultado_promedio)
        archivo.write('\nPromedio: ' + str(resultado_promedio))
        print('\nReprobado')
        archivo.write('\nReprobado')

#Ejercicio 13
def año_bisiesto():
    detener_ab1 = True
    archivo.write('\n')
    while detener_ab1:
        try:
            k=int(input('\nIngrese año de nacimiento: '))
            archivo.write('\nAño: ' + str(k))
            detener_ab1 = False
            if k < 0:
                print('Ingrese otro año...')
                detener_ab1 = True
        except ValueError:
            print('Caracter invalido...')
            detener_ab1 = True
    if k % 400 == 0:
        archivo.write('\nEl año si fue bisiesto ')
        return print(f'\nEl año {k} si fue bisiesto')

    elif k % 100 == 0:
        archivo.write('\nEl año no fue bisiesto ')
        return print(f'\nEl año {k} no fue bisiesto')

    elif k % 4 == 0:
        archivo.write('\nEl año si fue bisiesto ')
        return print(f'\nEl año {k} si fue bisiesto')

    else:
        archivo.write('\n:El año no fue bisiesto ')
        return print(f'\nEl año {k} no fue bisiesto')


#Ejercicio 14
def grupo_taxis():
    detener_gt1 = True
    detener_gt2 = True
    archivo.write('\n')
    while detener_gt1:
        try:
            mod=int(input('\nIngrese modelo del taxi (Año): '))
            archivo.write('\nModelo: ' + str(mod))
            detener_gt1 = False
            if mod < 1970:
                print('Modelo muy antiguo...')
                detener_gt1 = True
            elif mod > 2022:
                print('Modelo no existente...')
                detener_gt1 = True 
        except ValueError:
            print('Caracter invalido...')
            detener_gt1 = True

    
    while detener_gt2:
        try:
            km=int(input('\nIngrese kilometraje del taxi: '))
            archivo.write('\nKilometraje: ' + str(km))
            detener_gt2 = False
            if km < 0:
                print('Kilometraje invalido...')
                detener_gt2 = True
        except ValueError:
            print('Caracter invalido...')
            detener_gt2= True

    if mod < 2007:
        if km > 20000:
            print('\nDebe renovarse')
        else:
            print('\nMécanico')
            

    if 2007 <= mod <= 2013:
        if km >= 20000:
            print('\nRecibir mantenimiento')
        else:
            print('\nMécanico')

    if mod > 2013:
        if km < 10000:
            print('\nÓptimas condiciones')
        else:
            print('\nMécanico')


#MENÚ PRINCIPAL

detenerprogramas= True
while detenerprogramas:
    archivo = open('Tarea1.txt','w')
    print('\n\tPROGRAMAS DE TAREA PREPARATORIA 1')
    print('\nMENÚ')
    print('\n1. Número más grande')
    print('2. Divisores de un número')
    print('3. Cuantas vocales tiene una palabra')
    print('4. Suma de los números desde 0 hasta ese número')
    print('5. Número de inicio y fin')   
    print('6. Cúal es el mayor y lista de mayor a menor ')
    print('7. Cuantas veces aparece cada vocal ')
    print('8. Números impares hasta 100')
    print('9. Tipo de triángulo')
    print('10. Factorial de un número divisible entre 7')
    print('11. Calculadora de áreas de figuras geométricas')
    print('12. Promedio')
    print('13. Verificar año bisiesto')
    print('14. Grupo de taxis')
    print('15. Salir')  

    opcionb = opciones()

    if opcionb == 1:
        print('\nINSTRUCCIONES: Ingrese tres números.\nSi el primero es el más grande obtiene la suma de los tres.\nSi el segundo es el más grande obtiene la multiplicación de los tres.\nSi el tercero es el más grande se concatenan los tres.\nSi hay dos iguales se muestra el único que no es igual.\nSi los tres son iguales obtiene el mensaje: Todos son iguales.')
        ejercicio1()
        input()

    elif opcionb == 2:
        print('\nINSTRUCCIONES: Ingrese un número para mostrar sus divisores.')
        divisores()
        input()

    elif opcionb == 3:
        print('\nINSTRUCCIONES: Ingrese una palabra para mostrar cuantas vocales tiene.')
        conteo_vocales()
        input()

    elif opcionb == 4:
        print('\nINSTRUCCIONES: Ingrese un número y obtenga la suma de los número desde 0 hasta ese número.')
        suma_consecutiva()
        input()

    elif opcionb == 5:
        print('\nINSTRUCCIONES: Ingrese dos número y obtenga los números de 2 en 2 desde el número de inicio hasta el número de fin.')
        inicio_fin()
        input()

    elif opcionb == 6:
        print('\nINSTRUCCIONES: Ingrese dos número, y se verifica cual es el mayor y se muestra una lista de mayor a menor.')
        mayor()
        input()

    elif opcionb == 7:
        print('\nINSTRUCCIONES: Ingrese una palabra y obtenga el conteo de cada vocal')
        veces_vocales()
        input()

    elif opcionb == 8:
        print('\nINSTRUCCIONES: Números impares desde el 1 hasta el 100')
        impares()
        input()

    elif opcionb == 9:
        print('\nINSTRUCCIONES: Ingrese tres números. Los tres números corresponden a los lados de un triángulo.\nObtenga que tipo de triángulo es respecto al tamaño de sus lados.\nCuando: A=B=C - Triángulo equilatero\n\tA=B!=C - Triángulo isósceles\n\tA!=B!=C - Triángulo escaleno')
        triangulo()
        input()

    elif opcionb == 10:
        print('\nINSTRUCCIONES: Factorial de un número si y solo sí este es divible entre 7.')
        factorial()
        input()

    elif opcionb == 11:
        calculadora_areas()
        input()

    elif opcionb == 12:
        print('\nINSTRUCCIONES: Ingrese tres números enteros positivos, obtenga el promedio y un mensaje si esta aprobado(Mayor o igual a 60) o reprobado.')
        notas()
        input()

    elif opcionb == 13:
        print('\nINSTRUCCIONES: Ingrese su año de nacimiento y obtenga si fue año bisiesto')
        año_bisiesto()
        input()

    elif opcionb == 14:
        print('\nGRUPO DE TAXIS')
        grupo_taxis()
        input()

    elif opcionb == 15:
        print('\n>>>>>>CERRANDO PROGRAMAS DE TAREA PREPARATORIA 1<<<<<<\n')
        detenerprogramas = False

    else:
        print('\nIngrese una opción válida')
        input()


#ejercicio1()
#divisores()
#conteo_vocales()
#suma_consecutiva()
#inicio_fin()
#mayor()
#veces_vocales()
#impares()
#triangulo()
#factorial()
#calculadora_areas()
#notas()
#año_bisiesto()
#grupo_taxis()

cursor.close()
conexion.close()
archivo.close()