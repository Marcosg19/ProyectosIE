from calendar import c
import math

import psycopg2
#Conexión a base de datos
try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "marcos2001",
        dbname = "Tarea1_proyectosIE"  
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
        resultado = a+b+c
        print('\nLa suma de los tres números es: ', resultado)
        archivo.write('\nLa suma es: ' + str(a+b+c))
        cursor.execute("INSERT INTO ejercicio1(primernumero, segundonumero, tercernumero, operacion, resultado) VALUES(%s,%s,%s,'Suma',%s);",(a,b,c,resultado))
        conexion.commit()    

    elif a > c > b:
        resultado = a+b+c
        print('\nLa suma de los tres números es: ', resultado)
        archivo.write('\nLa suma es: ' + str(a+b+c))
        cursor.execute("INSERT INTO ejercicio1(primernumero, segundonumero, tercernumero, operacion, resultado) VALUES(%s,%s,%s,'Suma',%s);",(a,b,c,resultado))
        conexion.commit()

    elif b > a > c: 
        resultado = a*b*c
        print('\nLa multiplicación de los tres números es: ', resultado)
        archivo.write('\nLa multiplicación es: ' + str(a*b*c))
        cursor.execute("INSERT INTO ejercicio1(primernumero, segundonumero, tercernumero, operacion, resultado) VALUES(%s,%s,%s,'Multiplicación',%s);",(a,b,c,resultado))
        conexion.commit()

    elif b > c > a: 
        resultado = a*b*c
        print('\nLa multiplicación de los tres números es: ', resultado)
        archivo.write('\nLa multiplicación es: ' + str(a*b*c))
        cursor.execute("INSERT INTO ejercicio1(primernumero, segundonumero, tercernumero, operacion, resultado) VALUES(%s,%s,%s,'Multiplicación',%s);",(a,b,c,resultado))
        conexion.commit()


    elif c > a > b:
        conc_a = (str(a)+ ',')
        conc_b = (str(b)+ ',')
        conc_c = (str(c)) 
        resultado = conc_a + conc_b + conc_c
        print('\nLa concatenación de los números es: ' , resultado)
        archivo.write('\nLa concatenación es: ' + str(resultado))
        cursor.execute("INSERT INTO ejercicio1(primernumero, segundonumero, tercernumero, operacion, resultado) VALUES(%s,%s,%s,'Concatenación',%s);",(a,b,c,resultado))
        conexion.commit()

    elif c > b > a:
        conc_a = (str(a)+ ',')
        conc_b = (str(b)+ ',')
        conc_c = (str(c)) 
        resultado = conc_a + conc_b + conc_c
        print('\nLa concatenación de los números es: ' , resultado)
        archivo.write('\nLa concatenación es: ' + str(resultado))
        cursor.execute("INSERT INTO ejercicio1(primernumero, segundonumero, tercernumero, operacion, resultado) VALUES(%s,%s,%s,'Concatenación',%s);",(a,b,c,resultado))
        conexion.commit()

    elif a == b != c: 
        resultado = c
        print('\nAl ser iguales el primer y segundo número se muestra el tercero: ', resultado)
        archivo.write('\nAl ser iguales el primer y segundo número se muestra el tercero: ' + str(resultado))
        cursor.execute("INSERT INTO ejercicio1(primernumero, segundonumero, tercernumero, operacion, resultado) VALUES(%s,%s,%s,'Se muestra el tercer número',%s);",(a,b,c,resultado))
        conexion.commit()


    elif a == c != b: 
        resultado = b
        print('\nAl ser iguales el primer y tercer número se muestra el segundo: ', resultado)
        archivo.write('\nAl ser iguales el primer y tercer número se muestra el segundo: ' + str(resultado))
        cursor.execute("INSERT INTO ejercicio1(primernumero, segundonumero, tercernumero, operacion, resultado) VALUES(%s,%s,%s,'Se muestra el segundo número',%s);",(a,b,c,resultado))
        conexion.commit()

    elif b == c != a: 
        resultado = a
        print('\nAl ser iguales el segundo y tercer número se muestra el primero: ', resultado)
        archivo.write('\nAl ser iguales el segundo y tercer número se muestra el primero: ' + str(resultado))
        cursor.execute("INSERT INTO ejercicio1(primernumero, segundonumero, tercernumero, operacion, resultado) VALUES(%s,%s,%s,'Se muestra el primer número',%s);",(a,b,c,resultado))
        conexion.commit()

    elif a == b == c: 
        print('\n',(a, b, c))
        print('Todos son iguales\n')
        archivo.write('\nTodos son iguales: ' + str(a)+ ',' + str(b) + ',' + str(c))
        cursor.execute("INSERT INTO ejercicio1(primernumero, segundonumero, tercernumero, operacion, resultado) VALUES(%s,%s,%s,'Se muestra un mensaje','Todos son iguales');",(a,b,c))
        conexion.commit()

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
    cursor.execute("INSERT INTO divisores(primernumero, resultado) VALUES(%s,%s);",(d,resultado_div))
    conexion.commit()

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
    archivo.write('\nLa palabra '+ str(v) +' tiene ' + str(len(resultado))+ ' vocales '+ str(resultado))
    cursor.execute("INSERT INTO conteo_vocales(palabra, vocales, conteo) VALUES(%s,%s,%s);",(v,resultado,len(resultado)))
    conexion.commit()

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
    cursor.execute("INSERT INTO suma_consecutiva(numero, resultado) VALUES(%s,%s);",(f,s))
    conexion.commit()

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
        cursor.execute("INSERT INTO inicio_fin(numeroinicio, numerofin, resultado) VALUES(%s,%s,%s);",(h,g,resultado_if))
        conexion.commit()

    elif h < g:
        resultado_if2= [i for i in range(h, g+1, 2) if i%1==0]
        print('\nResultado: ',str(resultado_if2))
        archivo.write('\nResultado: ' + str(resultado_if2))
        cursor.execute("INSERT INTO inicio_fin(numeroinicio, numerofin, resultado) VALUES(%s,%s,%s);",(h,g,resultado_if2))
        conexion.commit()

    elif h == g:
        resultado_if3= [i for i in range(h, g+1) if i%1==0]
        print('\nResultado: ',str(resultado_if3))
        print('El número de inicio es el mismo que el fin')
        archivo.write('\nEl numero de inicio es el mismo que el fin ' )
        cursor.execute("INSERT INTO inicio_fin(numeroinicio, numerofin, resultado) VALUES(%s,%s,'El número de inicio y fin es el mismo');",(h,g))
        conexion.commit()


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
        cursor.execute("INSERT INTO mayor(primernumero, segundonumero, resultado) VALUES(%s,%s,%s);",(m,n,resultado_m))
        conexion.commit()

    elif m<n:
        resultado_n= [i for i in range(n, m-1, -1) if i%1==0]
        print('\nResultado: ',str(resultado_n))
        archivo.write('\nResultado: ' + str(resultado_n))
        cursor.execute("INSERT INTO mayor(primernumero, segundonumero, resultado) VALUES(%s,%s,%s);",(m,n,resultado_n))
        conexion.commit()

    elif m==n:
        print('\nLos números que ingresó son iguales ')
        archivo.write('\nLos números que ingresó son iguales ')
        cursor.execute("INSERT INTO mayor(primernumero, segundonumero, resultado) VALUES(%s,%s,'Los números que ingresó son iguales');",(m,n))
        conexion.commit()

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

    vocal_a = cantidad_a + cantidad_A
    print('\na: ',vocal_a)
    archivo.write('\na: '+ str(cantidad_a+cantidad_A))

    vocal_e = cantidad_e + cantidad_E
    print('e: ',vocal_e)
    archivo.write('\ne: '+ str(cantidad_e+cantidad_E))

    vocal_i = cantidad_i + cantidad_I
    print('i: ',vocal_i)
    archivo.write('\ni: '+ str(cantidad_i+cantidad_I))

    vocal_o = cantidad_o + cantidad_O
    print('o: ',vocal_o)
    archivo.write('\no: '+ str(cantidad_o+cantidad_O))

    vocal_u = cantidad_u + cantidad_U
    print('u: ',vocal_u)
    archivo.write('\nu: '+ str(cantidad_u+cantidad_U))

    cursor.execute("INSERT INTO veces_vocales(palabra, vocal_a, vocal_e, vocal_i, vocal_o, vocal_u) VALUES(%s,%s,%s,%s,%s,%s);",(v,vocal_a,vocal_e,vocal_i,vocal_o,vocal_u))
    conexion.commit()

#Octavo Ejercicio
def impares():
    archivo.write('\n')

    resultado_if= [i for i in range(0, 100+1) if i%2!=0]
    
    print('\nHistorial de número impares del 1 al 100:\n',str(resultado_if))
    print('\nHay',str(len(resultado_if))+ ' números impares')
    archivo.write('\nResultado: ' + str(resultado_if))
    archivo.write(f'\nHay {(len(resultado_if))} números impares')
    '''
    cursor.execute("INSERT INTO impares(historial, cantidad) VALUES(%s,%s);",(resultado_if,len(resultado_if)))
    conexion.commit()
    '''

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


    if p == r != q:
        print('\nTriángulo isósceles ')
        archivo.write('\nTriángulo isósceles')
        cursor.execute("INSERT INTO triangulo(lado_a, lado_b, lado_c, resultado) VALUES(%s,%s,%s,'Triángulo isósceles');",(p,q,r))
        conexion.commit()    

    elif p != q != r:
        print('\nTriángulo escaleno ')
        archivo.write('\nTriángulo escaleno')
        cursor.execute("INSERT INTO triangulo(lado_a, lado_b, lado_c, resultado) VALUES(%s,%s,%s,'Triángulo escaleno');",(p,q,r))
        conexion.commit()

    elif p == q == r:
        print('\nTriángulo equilátero ')
        archivo.write('\nTriángulo equilátero')
        cursor.execute("INSERT INTO triangulo(lado_a, lado_b, lado_c, resultado) VALUES(%s,%s,%s,'Triángulo equilatero');",(p,q,r))
        conexion.commit()

    elif p == q != r:
        print('\nTriángulo isósceles ')
        archivo.write('\nTriángulo isósceles')
        cursor.execute("INSERT INTO triangulo(lado_a, lado_b, lado_c, resultado) VALUES(%s,%s,%s,'Triángulo isósceles');",(p,q,r))
        conexion.commit()

    elif q == r != p:
        print('\nTriángulo isósceles ')
        archivo.write('\nTriángulo isósceles')
        cursor.execute("INSERT INTO triangulo(lado_a, lado_b, lado_c, resultado) VALUES(%s,%s,%s,'Triángulo isósceles');",(p,q,r))
        conexion.commit()


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

    cursor.execute("INSERT INTO factorial(numero, resultado) VALUES(%s,%s);",(x,fact))
    conexion.commit()


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
    cursor.execute("INSERT INTO calculadora_areas(figura, base, altura, radio, area) VALUES('Círculo',0,0,%s,%s);",(r,math.pi*r**2))
    conexion.commit()
    input()

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
    cursor.execute("INSERT INTO calculadora_areas(figura, base, altura, radio, area) VALUES('Triángulo',%s,%s,0,%s);",(b,h,(b*h)/2))
    conexion.commit()
    input()
    
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
    cursor.execute("INSERT INTO calculadora_areas(figura, base, altura, radio, area) VALUES('Cuadrado',%s,%s,0,%s);",(l,l,l**2))
    conexion.commit()
    input()

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
    cursor.execute("INSERT INTO calculadora_areas(figura, base, altura, radio, area) VALUES('Rectangulo',%s,%s,0,%s);",(b,h,b*h))
    conexion.commit()
    input()

def historial():
    print('\nHISTORIAL DE BASE DE DATOS')
    print('\nEjemplo \n[(Figura, Base, Altura, Radio, Área)]') 
    SQL = 'SELECT*FROM calculadora_areas;'
    cursor.execute(SQL)
    valores = cursor.fetchall()
    print()
    print(valores)
    print()
    input()  

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
                    historial()

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
            a=int(input('\nIngrese primera calificación: '))
            archivo.write('\nPrimera nota: ' + str(a))
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
            b=int(input('\nIngrese segunda calificación: '))
            archivo.write('\nSegunda nota: ' + str(b))
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
            c=int(input('\nIngrese tercera calificación: '))
            archivo.write('\nTercera nota: ' + str(c))
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
        cursor.execute("INSERT INTO notas(nota1, nota2, nota3, promedio, mensaje) VALUES(%s,%s,%s,%s,'Aprobado');",(a,b,c,resultado_promedio))
        conexion.commit()

    else:
        print('\nPromedio: ',resultado_promedio)
        archivo.write('\nPromedio: ' + str(resultado_promedio))
        print('\nReprobado')
        archivo.write('\nReprobado')
        cursor.execute("INSERT INTO notas(nota1, nota2, nota3, promedio, mensaje) VALUES(%s,%s,%s,%s,'Reprobado');",(a,b,c,resultado_promedio))
        conexion.commit()

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
    
    if k < 2022:    
        if k % 400 == 0:
            archivo.write('\nEl año si fue bisiesto ')
            cursor.execute("INSERT INTO bisiesto(nacimiento, mensaje) VALUES(%s,'Si fue año bisiesto');",(k,))
            conexion.commit()
            return print(f'\nEl año {k} si fue bisiesto')

        elif k % 100 == 0:
            archivo.write('\nEl año no fue bisiesto ')
            cursor.execute("INSERT INTO bisiesto(nacimiento, mensaje) VALUES(%s,'No fue año bisiesto');",(k,))
            conexion.commit()
            return print(f'\nEl año {k} no fue bisiesto')

        elif k % 4 == 0:
            archivo.write('\nEl año si fue bisiesto ')
            cursor.execute("INSERT INTO bisiesto(nacimiento, mensaje) VALUES(%s,'Si fue año bisiesto');",(k,))
            conexion.commit()
            return print(f'\nEl año {k} si fue bisiesto')

        else:
            archivo.write('\n:El año no fue bisiesto ')
            cursor.execute("INSERT INTO bisiesto(nacimiento, mensaje) VALUES(%s,'No fue año bisiesto');",(k,))
            conexion.commit()
            return print(f'\nEl año {k} no fue bisiesto')

    if k >= 2022:
        if k % 400 == 0:
            archivo.write('\nEl año si será bisiesto ')
            cursor.execute("INSERT INTO bisiesto(nacimiento, mensaje) VALUES(%s,'Si será año bisiesto');",(k,))
            conexion.commit()
            return print(f'\nEl año {k} si será bisiesto')

        elif k % 100 == 0:
            archivo.write('\nEl año no será bisiesto ')
            cursor.execute("INSERT INTO bisiesto(nacimiento, mensaje) VALUES(%s,'No será año bisiesto');",(k,))
            conexion.commit()
            return print(f'\nEl año {k} no será bisiesto')

        elif k % 4 == 0:
            archivo.write('\nEl año si será bisiesto ')
            cursor.execute("INSERT INTO bisiesto(nacimiento, mensaje) VALUES(%s,'Si será año bisiesto');",(k,))
            conexion.commit()
            return print(f'\nEl año {k} si será bisiesto')

        else:
            archivo.write('\n:El año no será bisiesto ')
            cursor.execute("INSERT INTO bisiesto(nacimiento, mensaje) VALUES(%s,'No será año bisiesto');",(k,))
            conexion.commit()
            return print(f'\nEl año {k} no será bisiesto')

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
            archivo.write('\nDebe renovarse')
            cursor.execute("INSERT INTO grupo_taxis(modelo, kilometraje, mensaje) VALUES(%s,%s,'Debe renovarse');",(mod,km))
            conexion.commit()
        else:
            print('\nMécanico')
            archivo.write('\nMécanico')
            cursor.execute("INSERT INTO grupo_taxis(modelo, kilometraje, mensaje) VALUES(%s,%s,'Mécanico');",(mod,km))
            conexion.commit()
            

    if 2007 <= mod <= 2013:
        if km >= 20000:
            print('\nRecibir mantenimiento')
            archivo.write('\nRecibir mantenimiento')
            cursor.execute("INSERT INTO grupo_taxis(modelo, kilometraje, mensaje) VALUES(%s,%s,'Recibir mantenimiento');",(mod,km))
            conexion.commit()
        else:
            print('\nMécanico')
            archivo.write('\nMécanico')
            cursor.execute("INSERT INTO grupo_taxis(modelo, kilometraje, mensaje) VALUES(%s,%s,'Mécanico');",(mod,km))
            conexion.commit()

    if mod > 2013:
        if km < 10000:
            print('\nÓptimas condiciones')
            archivo.write('\nÓptimas condiciones')
            cursor.execute("INSERT INTO grupo_taxis(modelo, kilometraje, mensaje) VALUES(%s,%s,'Óptimas condiciones');",(mod,km))
            conexion.commit()
        else:
            print('\nMécanico')
            archivo.write('\nMécanico')
            cursor.execute("INSERT INTO grupo_taxis(modelo, kilometraje, mensaje) VALUES(%s,%s,'Mécanico');",(mod,km))
            conexion.commit()



def menu_triangulo():
    detenertr= True
    while detenertr:
        print('\n\tTipo de triángulo')
        print('\nOpciones')
        print('1. Abrir programa ')
        print('2. Historial')
        print('3. Regresar')

        opciontr = opciones()

        if opciontr == 1:
            print('Tipo de triángulo')
            print('\nINSTRUCCIONES: Ingrese tres números.\nSi el primero es el más grande obtiene la suma de los tres.\nSi el segundo es el más grande obtiene la multiplicación de los tres.\nSi el tercero es el más grande se concatenan los tres.\nSi hay dos iguales se muestra el único que no es igual.\nSi los tres son iguales obtiene el mensaje: Todos son iguales.')
            triangulo()
            input()

        elif opciontr == 2:
            cursor.execute('SELECT*FROM triangulo;')
            valorestr = cursor.fetchall()
            print()
            print(valorestr)
            input()

        elif opciontr == 3:
            print('\nRegresando...')
            detenertr = False

        else:
            print('\nIngrese una opción válida')
            input()


def menu_factorial():
    detenertr= True
    while detenertr:
        print('\n\tFactorial de un número divisible entre 7')
        print('\nOpciones')
        print('1. Abrir programa ')
        print('2. Historial')
        print('3. Regresar')

        opciontr = opciones()

        if opciontr == 1:
            print('Factorial de un número divisible entre 7')
            print('\nINSTRUCCIONES: Factorial de un número si y solo sí este es divible entre 7.')
            factorial()
            input()

        elif opciontr == 2:
            cursor.execute('SELECT*FROM factorial;')
            valorestr = cursor.fetchall()
            print()
            print(valorestr)
            input()

        elif opciontr == 3:
            print('\nRegresando...')
            detenertr = False

        else:
            print('\nIngrese una opción válida')
            input()


def menu_notas():
    detenernt= True
    while detenernt:
        print('\n\tPromedio')
        print('\nOpciones')
        print('1. Abrir programa ')
        print('2. Historial')
        print('3. Regresar')

        opcionnt = opciones()

        if opcionnt == 1:
            print('Promedio')
            print('\nINSTRUCCIONES: Ingrese tres números enteros positivos, obtenga el promedio y un mensaje si esta aprobado(Mayor o igual a 60) o reprobado.')
            notas()
            input()

        elif opcionnt == 2:
            cursor.execute('SELECT*FROM notas;')
            valoresnt = cursor.fetchall()
            print()
            print(valoresnt)
            input()

        elif opcionnt == 3:
            print('\nRegresando...')
            detenernt = False

        else:
            print('\nIngrese una opción válida')
            input()


def menu_bisiesto():
    detenerbs= True
    while detenerbs:
        print('\n\tVerificar año bisiesto')
        print('\nOpciones')
        print('1. Abrir programa ')
        print('2. Historial')
        print('3. Regresar')

        opcionbs = opciones()

        if opcionbs == 1:
            print('Verificar año bisiesto')
            print('\nINSTRUCCIONES: Ingrese su año de nacimiento y obtenga si fue año bisiesto')
            año_bisiesto()
            input()

        elif opcionbs == 2:
            cursor.execute('SELECT*FROM bisiesto;')
            valoresbs = cursor.fetchall()
            print()
            print(valoresbs)
            input()

        elif opcionbs == 3:
            print('\nRegresando...')
            detenerbs = False

        else:
            print('\nIngrese una opción válida')
            input()

def menu_taxis():
    detenertx= True
    while detenertx:
        print('\n\tGrupo de taxis')
        print('\nOpciones')
        print('1. Abrir programa ')
        print('2. Historial')
        print('3. Regresar')

        opciontx = opciones()

        if opciontx == 1:
            print('Información - Grupo de taxis')
            grupo_taxis()
            input()

        elif opciontx == 2:
            cursor.execute('SELECT*FROM grupo_taxis;')
            valorestx = cursor.fetchall()
            print()
            print(valorestx)
            input()

        elif opciontx == 3:
            print('\nRegresando...')
            detenertx = False

        else:
            print('\nIngrese una opción válida')
            input()


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
        menu_triangulo()

    elif opcionb == 10:
        menu_factorial()

    elif opcionb == 11:
        calculadora_areas()
        input()

    elif opcionb == 12:
        menu_notas()

    elif opcionb == 13:
        menu_bisiesto()

    elif opcionb == 14:
        menu_taxis()

    elif opcionb == 15:
        print('\n>>>>>>CERRANDO PROGRAMAS DE TAREA PREPARATORIA 1<<<<<<\n')
        detenerprogramas = False

    else:
        print('\nIngrese una opción válida')
        input()

cursor.close()
conexion.close()
archivo.close()