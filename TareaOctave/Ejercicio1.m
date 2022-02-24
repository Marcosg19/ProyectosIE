  fprintf('\n')
  fprintf('Programa Ejercicio 1 \n')
  a=input("Ingresar primer número: ");
  b=input("Ingresar segundo número: ");
  c=input("Ingresar tercer número: ");
  fprintf('\n')
  if a>b && a>c && b~=c
     y=a+b+c;
     fprintf('La suma es: %d \n',y)
  endif

  if b>a && b>c && a~=c
    y1=a*b*c;
    fprintf('La multiplicación es: %d \n',y1)
  endif

  if c>a && c>b && a~=b

    fprintf('La concatenación es: %d%d%d \n',a,b,c)

  endif

  if a==b && a~=c
    fprintf('Al ser iguales el primer y segundo número se muestra el tercero: %d \n',c)
  endif

  if a==c && a~=b
    fprintf('Al ser iguales el primer y tercer número se muestra el segundo: %d \n',b)
  endif

  if b==c && b~=a
    fprintf('Al ser iguales el segundo y tercer número se muestra el primero: %d \n',a)
  endif

  if a==b && a==c
    fprintf('TODOS SON IGUALES \n')
  endif