clc; clear all; close all;
fprintf('Programa de lista de inicio a fin\n')
a=input("Ingresar número de inicio: ");
while (a~=fix(a))||(a<0)
    fprintf('El numero no es positivo \n');
    a=input("Ingresar otro valor: ");
end
b=input("Ingresar número de fin: ");
while (b~=fix(b))||(b<0)
    fprintf('El numero no es positivo \n');
    b=input("Ingresar otro valor: ");
end

if (a>b)
  resultado= a:-2:b; 
  fprintf('Resultado: \n');
  disp(resultado)
endif

if (a<b)
  resultado= a:2:b; 
  fprintf('Resultado: \n');
  disp(resultado)
endif

if (a==b)
  resultado= a:2:b; 
  fprintf('El numero de inicio es el mismo que el fin. \n');
  disp(resultado)
endif