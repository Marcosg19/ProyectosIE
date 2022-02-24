  clc; clear all; close all;
  fprintf('\n')
  fprintf('Programa Factorial de un numero divible entre 7 \n')
  a=input("Ingresar primer número: ");
  while (a<0)
    fprintf('El número no puede ser negativo\n');
    a=input("Ingresar otro número: ");
  end
  fact=1;
  if mod(a,7)==0
    for i=1:+1:a;
      fact=fact*i;
    end
    fprintf('El factorial de %d es: %d \n',a,fact)
   else 
    fprintf('No es divisible entre 7 \n')
  endif

