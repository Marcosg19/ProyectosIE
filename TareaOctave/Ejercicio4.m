clc; clear all; close all;
fprintf('Programa de suma consecutiva hasta un numero n\n')
a=input("Ingresar un numero entero positivo: ");
while (a~=fix(a))||(a<1)
    fprintf('El numero no es positivo \n');
    a=input("Ingresar otro valor: ");
end
s=0;
i=1;
while (i<=a)
    s=s+i;
    i=i+1;
end

fprintf('Resultado: %d \n',s);