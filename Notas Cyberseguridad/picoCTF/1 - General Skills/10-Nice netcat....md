# Nice netcat
# Descripción del reto: 
### There is a nice program that you can talk to by using this command in a shell: Additional details will be available after launching your challenge instance.
There is a nice program that you can talk to by using this command in a shell: $ nc wily-courier.picoctf.net 61594, but it doesn't speak English...
# Solucion
nc wily-courier.picoctf.net 61594

'112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
102 
55 
97 
54 
101 
125'

nc wily-courier.picoctf.net 61594 | python3 -c "import sys; print(''.join([chr(int(x)) for x in sys.stdin.read().split()]))"

'picoCTF{g00d_k1tty!_n1c3_k1tty!_f7a6e}'
# Notas adicionales

# Referencias