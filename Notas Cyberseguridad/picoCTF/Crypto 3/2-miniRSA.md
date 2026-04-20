# miniRSA 

# Descripción del reto:
Let's decrypt this. Can you decrypt this ciphertext? Something seems a bit small.

# Solución:
El reto proporciona los parámetros $N$, $e$ y el `ciphertext` de un criptosistema RSA. La vulnerabilidad radica en un **Ataque de Exponente Pequeño** ($e=3$) combinado con la falta de un esquema de relleno (padding) adecuado.

### Vulnerabilidad: Exponente Pequeño y Mensaje Corto
En RSA, el cifrado es $c \equiv m^e \pmod N$. Si el mensaje $m$ no es lo suficientemente largo, $m^e$ será estrictamente menor que $N$. Cuando esto sucede, la operación de módulo no se ejecuta, haciendo que el algoritmo asimétrico degenere en una simple operación aritmética. El mensaje original se puede recuperar calculando la raíz exacta:
$$m = \sqrt[e]{c}$$

### Proceso de explotación:
Se desarrolló un script en Python preparado para iterar posibles desbordamientos modulares ($m^3 = c + k \cdot N$). Sin embargo, durante la ejecución se comprobó que el mensaje cifrado ni siquiera superó el valor del módulo ($k=0$).
1. Se capturó el valor de $c$ directamente del archivo descargado usando expresiones regulares para evadir trampas de formato.
2. Se utilizó la función optimizada en C `sympy.integer_nthroot(c, 3)` para verificar rápidamente si el criptograma original poseía una raíz cúbica exacta.
3. Al evaluarlo, la función devolvió la raíz exacta al instante.
4. El entero resultante correspondió al mensaje original $m$, el cual fue decodificado de representación numérica (bytes) a ASCII.

**Bandera final:**
`picoCTF{n33d_a_lArg3r_e_bc950e0e}`

# Notas adicionales:
* El título y la descripción ("Something seems a bit small") hacen alusión directa al peligro de utilizar $e=3$ sin implementar esquemas como OAEP.
* A pesar de preparar el entorno para un ataque de desbordamiento modular (Padding Attack), la simplicidad del reto demostró que no existía relleno alguno.

# Referencias:
* [Coppersmith's attack / Small public exponent](https://en.wikipedia.org/wiki/Coppersmith%27s_attack)
* [SymPy integer_nthroot](https://docs.sympy.org/latest/modules/core.html#sympy.core.power.integer_nthroot)