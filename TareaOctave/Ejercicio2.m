clc; clear all; close all;
fprintf('Programa de divisores\n')
a=input("Ingresar un numero entero positivo: ");
while (a~=fix(a))||(a<1)
    fprintf('El numero no es positivo \n');
    a=input("Ingresar otro valor: ");
end
cont=1;
for i=1:a
    r=mod(a,i);
    if r==0
      v(cont)=i;
      cont=cont+1;
    endif
endfor
fprintf('Los divisores de %d son: \n',a)
disp(v)