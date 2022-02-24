clc; clear all; close all;
fprintf('Programa de conteo de cada vocal\n')
a=input("Ingresar una palabra: ",'s');
fprintf('\n')

vocal_a = ['a'];
vocal_e = ['e'];
vocal_i = ['i'];
vocal_o = ['o'];
vocal_u = ['u'];
vocal_A = ['A'];
vocal_E = ['E'];
vocal_I = ['I'];
vocal_O = ['O'];
vocal_U = ['U'];

n = [];
for x_a = 1:1 
    n_a = [n strfind(a,vocal_a(x_a))];
end

for x_e = 1:1
    n_e = [n strfind(a,vocal_e(x_e))];
end

for x_i = 1:1
  n_i = [n strfind(a,vocal_i(x_i))];
end

for x_o = 1:1
  n_o = [n strfind(a,vocal_o(x_o))];
end

for x_u = 1:1
  n_u = [n strfind(a,vocal_u(x_u))];
end

for x_A = 1:1 
    n_A = [n strfind(a,vocal_A(x_A))];
end

for x_E = 1:1
    n_E = [n strfind(a,vocal_E(x_E))];
end

for x_I = 1:1
  n_I = [n strfind(a,vocal_I(x_I))];
end

for x_O = 1:1
  n_O = [n strfind(a,vocal_O(x_O))];
end

for x_U = 1:1
  n_U = [n strfind(a,vocal_U(x_U))];
end

cantidad_a = length(n_a);
cantidad_A = length(n_A);
cantidad_e = length(n_e);
cantidad_E = length(n_E);
cantidad_i = length(n_i);
cantidad_I = length(n_I);
cantidad_o = length(n_o);
cantidad_O = length(n_O);
cantidad_u = length(n_u);
cantidad_U = length(n_U);


respuesta_a = cantidad_A+cantidad_a;
respuesta_e = cantidad_E+cantidad_e;
respuesta_i = cantidad_I+cantidad_i;
respuesta_o = cantidad_O+cantidad_o; 
respuesta_u = cantidad_U+cantidad_u;

fprintf('Resultado: \n');
fprintf('a: %d \n',respuesta_a);
fprintf('e: %d \n',respuesta_e);
fprintf('i: %d \n',respuesta_i);
fprintf('o: %d \n',respuesta_o);
fprintf('u: %d \n',respuesta_u);