clc; clear all; close all;
fprintf('Programa de lista de mayor a menor \n')
a=input("Ingresar primer número: ");
while (a~=fix(a))
    fprintf('El numero tiene que ser entero \n');
    a=input("Ingresar otro valor: ");
end
b=input("Ingresar segundo numero: ");
while (b~=fix(b))
    fprintf('El numero tiene que ser entero \n');
    b=input("Ingresar otro valor: ");
end

if (a>b)
  resultado= a:-1:b; 
  fprintf('Resultado: \n');
  disp(resultado)
endif

if (a<b)
  resultado= b:-1:a; 
  fprintf('Resultado: \n');
  disp(resultado)
endif

if (a==b)
  resultado= a:1:b; 
  fprintf('Los dos numeros son iguales \n');
  disp(resultado)
endif