  clc; clear all; close all;
  fprintf('\n')
  fprintf('Programa de tipo de triangulos \n')
  a=input("Ingresar primer n�mero: ");
  while (a<0)
    fprintf('El n�mero no puede ser negativo\n');
    a=input("Ingresar otro n�mero: ");
  end
  b=input("Ingresar segundo n�mero: ");
  while (b<0)
    fprintf('El n�mero no puede ser negativo\n');
    b=input("Ingresar otro n�mero: ");
  end
  c=input("Ingresar tercer n�mero: ");
  while (c<0)
    fprintf('El n�mero no puede ser negativo\n');
    c=input("Ingresar otro n�mero: ");
  end  
  fprintf('\n')
  

  if a == b && a == c && c == b 
     fprintf('Triangulo equil�tero \n')
  endif
      
  if a ~= b && a ~= c && b ~= c 
     fprintf('Triangulo escaleno \n');
  endif

  if a == b && a ~= c && b ~= c 
    fprintf('Triangulo isosceles \n')
  endif
  
  if a == c && a ~= b && b ~= c 
    fprintf('Triangulo isosceles \n')
  endif
  
  if b == c && b ~= a && c ~= a 
    fprintf('Triangulo isosceles \n')
  endif