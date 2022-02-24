clc; clear all; close all;
fprintf('Programa de conteo de vocales\n')
a=input("Ingresar una palabra: ",'s');

vocales = ['a','e','i','o','u','A','E','I','O','U'];
n = [];
for x = 1:10
    n = [n strfind(a,vocales(x))];
end
cantidad = length(n);

respuesta = fprintf('La palabra tiene %d vocales. \n',cantidad);