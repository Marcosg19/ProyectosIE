archivo = open('Tarea1.txt','w')

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

    resultado_if= [i for i in range(h, g+1, 2) if i%1==0]
    
    print('\nResultado: ',str(resultado_if))
    archivo.write('\nResultado: ' + str(resultado_if))

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

#Noveno Ejercicio



#ejercicio1()
#divisores()
#conteo_vocales()
#suma_consecutiva()
#inicio_fin()
#mayor()
#veces_vocales()
#impares()

cursor.close()
conexion.close()
archivo.close()