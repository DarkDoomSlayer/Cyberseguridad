# Descripción
Everything seems secure; strong numbers, familiar parameters but something small might ruin it all. Can you recover the message?
Download the [message](https://challenge-files.picoctf.net/c_plain_mesa/1079be04e10c8603dfdacdb45b780bc467aff1eba21cdf0ff9cccc40e2de5c55/message.txt). And source [code](https://challenge-files.picoctf.net/c_plain_mesa/1079be04e10c8603dfdacdb45b780bc467aff1eba21cdf0ff9cccc40e2de5c55/encryption.py)
# Solución
Al analizar el código, vemos esto:
```
from random import randint
from sage.all import *

N = 48
p = 3
q = 509

R = PolynomialRing(ZZ, 'x')
x = R.gen()
R_modq = PolynomialRing(Integers(q), 'x').quotient(x**N - 1, 'xbar')
R_modp = PolynomialRing(Integers(p), 'x').quotient(x**N - 1, 'xbar')

def gen_poly():
    return R([randint(-1,1) for _ in range(N)])

def gen_msg(text):
    binary_str = ''.join(format(ord(char), '08b') for char in text)
    
    padding_length = (N - (len(binary_str) % N)) % N
    binary_str += '0' * padding_length
    
    chunks = [binary_str[i:i+N] for i in range(0, len(binary_str), N)]
    
    polynomials = [
        R([int(bit) for bit in chunk])
        for chunk in chunks
    ]
    
    return polynomials

def encrypt(h, m): 
    r = gen_poly()
    return R_modq(p*(h*r) + m)

def generate_keys():
    while True:
        # Random ternary polynomials f and g
        f = gen_poly()
        g = gen_poly()
        
        # Check if f is invertible modulo p and q
        try:
            f_p_inv = R_modp(f)**-1
            f_q_inv = R_modq(f)**-1
            break
        except:
            continue

    h = R_modq(p*(f_q_inv*g))
    
    private_key = (f, g, f_p_inv, f_q_inv)
    public_key = h
    return public_key, private_key

with open("flag.txt", "r") as f:
    flag = f.read().strip()

public_key, private_key = generate_keys()
print(f"h = {public_key.list()}")

ciphertext = []
encoded = gen_msg(flag)
for part in encoded:
    ciphertext.append(encrypt(public_key, part))
ct = [c.list() for c in ciphertext]
print(f"ct = {ct}")

with open("public.txt", "w") as f:
    f.write(f"N = {N}\n")
    f.write(f"p = {p}\n")
    f.write(f"q = {q}\n")
    f.write(f"h = {public_key.list()}\n")
    f.write(f"ct = {ct}\n")
```

El problema aquí es que el parámetro *N = 48* es extremadamente pequeño para los estándares de seguridad modernos. Esto permite realizar un ataque de reducción de base de red (LLL/BKZ) para encontrar la clave privada *(f, g* a partir de la clave pública *h*

Para este tipo de problemas, podemos usar la herramienta ***sagemath***.

Para no tener que instalarla, usamos una versión online (https://sagecell.sagemath.org/) a la que le pasaremos el siguiente código
```
from sage.all import *

# Datos del reto
N = 48
p = 3
q = 509
h_coeffs = [171, 218, 364, 196, 397, 127, 385, 467, 30, 314, 298, 455, 307, 40, 97, 200, 347, 301, 219, 258, 432, 469, 155, 311, 431, 184, 276, 170, 125, 403, 49, 326, 125, 416, 409, 506, 226, 441, 245, 373, 426, 503, 420, 298, 449, 453, 243, 206]
ct_blocks = [[461, 481, 501, 448, 105, 391, 58, 322, 90, 349, 410, 60, 502, 116, 410, 262, 416, 479, 291, 90, 410, 226, 253, 25, 233, 286, 474, 255, 165, 274, 491, 285, 14, 485, 7, 400, 53, 23, 155, 98, 322, 35, 16, 90, 103, 472, 204, 62], [291, 437, 68, 214, 302, 166, 368, 455, 132, 49, 396, 265, 452, 488, 377, 334, 139, 232, 283, 277, 258, 14, 14, 161, 388, 176, 288, 339, 291, 315, 484, 49, 51, 421, 350, 492, 389, 97, 229, 431, 426, 285, 292, 412, 255, 1, 130, 39], [179, 159, 95, 353, 267, 160, 349, 483, 413, 480, 482, 103, 331, 499, 417, 255, 136, 352, 384, 235, 387, 371, 132, 108, 498, 84, 29, 267, 157, 424, 453, 74, 219, 151, 470, 104, 89, 348, 166, 96, 304, 424, 447, 124, 413, 273, 401, 333], [6, 387, 353, 98, 2, 486, 96, 387, 316, 317, 472, 289, 330, 169, 308, 427, 465, 344, 457, 249, 383, 380, 2, 407, 265, 48, 391, 142, 157, 340, 3, 0, 469, 245, 346, 172, 47, 175, 188, 145, 238, 436, 210, 369, 259, 135, 350, 167], [150, 202, 32, 135, 325, 152, 498, 59, 67, 81, 6, 14, 158, 328, 289, 292, 463, 255, 217, 295, 258, 418, 151, 56, 472, 19, 266, 184, 176, 259, 411, 470, 96, 319, 303, 459, 46, 159, 464, 287, 306, 215, 349, 23, 384, 322, 313, 262], [367, 133, 319, 404, 341, 202, 195, 406, 496, 232, 281, 17, 18, 91, 257, 460, 263, 445, 203, 329, 27, 199, 499, 454, 467, 345, 52, 464, 93, 410, 35, 15, 226, 263, 198, 166, 441, 59, 193, 96, 49, 486, 297, 72, 304, 150, 40, 140]]

R = PolynomialRing(ZZ, 'x')
x = R.gen()
Quotient = R.quotient(x**N - 1, 'xbar')

# 1. Construir la matriz de la red
# [ I   H ]
# [ 0  qI ]
M = Matrix(ZZ, 2*N, 2*N)
for i in range(N):
    M[i, i] = 1
    for j in range(N):
        # Matriz circulante para h
        M[i, N + j] = h_coeffs[(j - i) % N]
    M[N + i, N + i] = q

# 2. Reducción LLL
print("Reduciendo la red...")
L = M.LLL()

# 3. Extraer la clave privada f
# La primera fila suele contener (f, pg)
f_vec = L[0][:N]
f_poly = Quotient(list(f_vec))

# 4. Decodificar
# Preparar anillos para el descifrado
R_modq = PolynomialRing(Integers(q), 'x').quotient(x**N - 1, 'xbar')
R_modp = PolynomialRing(Integers(p), 'x').quotient(x**N - 1, 'xbar')

f_q = R_modq(list(f_vec))
f_p_inv = R_modp(list(f_vec))**-1

binary_str = ""
for ct in ct_blocks:
    c = R_modq(ct)
    # a = f * c (mod q)
    a = f_q * c
    # Centrar coeficientes de a entre -q/2 y q/2
    a_coeffs = [(int(coeff) + q//2) % q - q//2 for coeff in a.list()]
    # m = f_p_inv * a (mod p)
    m = R_modp(f_p_inv) * R_modp(a_coeffs)
    # Asegurar que tenemos N bits por bloque
    bits = m.list()
    bits += [0] * (N - len(bits))
    binary_str += "".join(str(b) for b in bits)

# Convertir de binario a texto
flag = ""
for i in range(0, len(binary_str), 8):
    byte = binary_str[i:i+8]
    if len(byte) == 8:
        flag += chr(int(byte, 2))

print(f"Resultado: {flag}")
```

Para resolver este reto, se aplica el algoritmo LLL sobre una red construida con la clave pública *h*, lo que permite identificar a *f* y *g* como vectores cortos debido a que sus coeficientes originales son ternarios, es decir, pertenecientes al conjunto *{-1, 0, 1}*. Con la clave *f* recuperada, se procede a calcular su inversa módulo *p (p=3)* para poder revertir el enmascaramiento del mensaje original. Finalmente, es indispensable realizar un ajuste de rango centrando los coeficientes en el intervalo $[-q/2, q/2]$ tras multiplicar el criptograma por *f* módulo *q (q = 509)*, lo que garantiza que el "ruido" de la encripción se elimine por completo antes de extraer el mensaje $m$ mediante la reducción final módulo *p*.

Al usarlo en la página, obtenemos esto:
```
Reduciendo la red...
Resultado: picoCTF{th4ts_s0_N0t_TRU3_0729b9da}
```

picoCTF{th4ts_s0_N0t_TRU3_0729b9da}
# Notas
link del reto:
[https://play.picoctf.org/events/79/challenges/710?page=3](https://play.picoctf.org/events/79/challenges/718?page=3)