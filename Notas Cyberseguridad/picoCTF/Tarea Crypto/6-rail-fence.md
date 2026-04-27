# rail-fence

# Descripción del reto:
A type of transposition cipher is the rail fence cipher, which is described `here`.
Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it?
Download the message `here`.
Put the decoded message in the picoCTF flag format, `picoCTF{decoded_message}`.

# Solución:
El reto nos presenta un texto encriptado mediante un cifrado clásico de transposición conocido como **Rail Fence** (Cifrado de Valla). A diferencia de los cifrados de sustitución, la transposición mantiene intactos los caracteres originales, pero altera su posición geométrica.

### Concepto: Cifrado Rail Fence
El algoritmo consiste en escribir el texto plano en un patrón de zigzag diagonal a través de un número predeterminado de "rieles" (filas) y luego leer el resultado concatenando cada fila de izquierda a derecha. La seguridad de este cifrado recae enteramente en el desconocimiento de la llave (el número de rieles utilizados). En este reto, la descripción revela que la llave es $N = 4$ rieles.

### Proceso de explotación:
Se desarrolló un script en Python para automatizar la reconstrucción de la matriz y el descifrado del texto:
1. **Modelado de la Matriz:** Se calculó la longitud del texto cifrado y se generó una matriz bidimensional (4 filas $\times$ longitud del texto).
2. **Trazado de la Ruta:** Se iteró sobre la matriz simulando el movimiento de zigzag (bajando hasta el riel inferior y subiendo hasta el superior), marcando con un carácter comodín (`*`) las celdas activas.
3. **Inyección de Datos:** Se leyó el texto cifrado de forma secuencial y se rellenaron los comodines fila por fila, restaurando la posición espacial original de cada letra.
4. **Extracción:** Se volvió a recorrer la matriz en zigzag, leyendo los caracteres restaurados para reconstruir el texto plano original.
5. **Formateo:** La cadena resultante se envolvió en el formato estándar `picoCTF{...}`.

**Bandera final:**
'picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_83F6D8D7}'

# Notas adicionales:
* Dado que el número de llaves posibles (rieles) está limitado por la longitud del mensaje, el cifrado Rail Fence es trivialmente vulnerable a ataques de fuerza bruta. Incluso si no se nos hubiera proporcionado el número de rieles, un script iterativo probando de 2 a $N$ rieles revelaría el texto plano al instante.

# Referencias:
* [Rail fence cipher (Wikipedia)](https://en.wikipedia.org/wiki/Rail_fence_cipher)