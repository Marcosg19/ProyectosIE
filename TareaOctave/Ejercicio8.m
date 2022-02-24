clc; clear all; close all;
fprintf('Programa de conteo de vocales\n')
fprintf('\n')

cont=1;
for i=1:100
    r=mod(i,2)==0;
    if r==0
      v(cont)=i;
      cont=cont+1;
    endif
endfor
    fprintf('Historial de número impares del 1 al 100: \n');
    disp(v)
    fprintf('Hay %d numeros impares. \n',cont-1);
