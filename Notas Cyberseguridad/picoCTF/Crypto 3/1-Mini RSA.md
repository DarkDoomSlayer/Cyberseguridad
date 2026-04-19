# Mini RSA

# Descripción del reto:
What happens if you have a small exponent? There is a twist though, we padded the plaintext so that $(M^e)$ is just barely larger than $N$. Let's decrypt this: values

# Solución:
El reto proporciona los parámetros $N$, $e$ y $c$ de un criptosistema RSA. Al analizar los datos, se observa un exponente público extremadamente pequeño ($e=3$) y un módulo $N$ de gran magnitud (1006 dígitos).

### Vulnerabilidad: Ataque de Exponente Pequeño (Small Exponent Attack)
En RSA, el texto cifrado se calcula como $c = m^e \pmod N$. Si el mensaje $m$ es corto o el exponente $e$ es pequeño, existe la posibilidad de que $m^e < N$. En este escenario, la operación de módulo no tiene efecto, reduciendo el problema de descifrado a una simple operación aritmética de raíz enésima sobre los números enteros:
$$m = \sqrt[e]{c}$$

### Proceso de explotación:
Aunque la descripción sugería que $m^e$ era ligeramente mayor a $N$ (lo que requeriría probar $m = \sqrt[e]{c + k \cdot N}$ para valores pequeños de $k$), el script de automatización desarrollado en Python determinó que para $k=0$ existía una raíz cúbica exacta.

Se utilizó un algoritmo de búsqueda binaria para raíces enteras para evitar errores de precisión de punto flotante, los cuales son comunes al manejar números de más de 1000 dígitos en lenguajes de programación convencionales.

Al calcular $\sqrt[3]{c}$, se obtuvo un entero que, al ser convertido de bytes a ASCII, reveló la bandera.

**Bandera final:**
`picoCTF{n3v3r_y35_m0r3_3xp0n3nt_a22916ee}`

# Notas adicionales:
* Este reto enfatiza que un exponente pequeño ($e=3$) es peligroso no solo por ataques de fuerza bruta, sino porque invalida la propiedad matemática del módulo si el mensaje no es lo suficientemente grande.
* El "padding" mencionado en la descripción es una técnica para mitigar esto, pero en este caso, el relleno no fue suficiente para mover el valor de $M^e$ más allá de una vuelta del módulo.

# Referencias:
* [RSA Small encryption exponent](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Small_encryption_exponent)
* [PyCryptodome Documentation](https://pypi.org/project/pycryptodome/)