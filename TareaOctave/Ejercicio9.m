  clc; clear all; close all;
  fprintf('\n')
  fprintf('Programa de tipo de triangulos \n')
  a=input("Ingresar primer número: ");
  while (a<0)
    fprintf('El número no puede ser negativo\n');
    a=input("Ingresar otro número: ");
  end
  b=input("Ingresar segundo número: ");
  while (b<0)
    fprintf('El número no puede ser negativo\n');
    b=input("Ingresar otro número: ");
  end
  c=input("Ingresar tercer número: ");
  while (c<0)
    fprintf('El número no puede ser negativo\n');
    c=input("Ingresar otro número: ");
  end  
  fprintf('\n')
  

  if a == b && a == c && c == b 
     fprintf('Triangulo equilátero \n')
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