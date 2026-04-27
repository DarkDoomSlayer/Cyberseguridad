# Crack the Power

# Descripción del reto:
We received an encrypted message. The modulus is built from primes large enough that factoring them isn't an option, at least not today. See if you can make sense of the numbers and reveal the flag.

# Solución:
El reto nos proporciona un archivo de texto con los parámetros clásicos del algoritmo RSA: el módulo $n$, el exponente público $e$ y el criptograma $c$. La descripción descarta explícitamente cualquier ataque basado en la factorización de $n$, indicando que la debilidad reside en otro elemento de la ecuación.

### Vulnerabilidad: Ataque de Exponente Pequeño (Small Exponent Attack)
El título del reto ("Crack the Power") hace una alusión directa al exponente de la función de cifrado. Al inspeccionar los valores, se descubre que el exponente utilizado es extremadamente pequeño (usualmente $e=3$). 

Cuando $e$ es muy pequeño y el mensaje original $m$ no tiene un relleno (padding) adecuado, es matemáticamente posible que el resultado de la exponenciación sea estrictamente menor que el módulo:
$$m^e < n$$

En esta condición, la operación de módulo $\pmod n$ se vuelve inútil porque no hay desbordamiento circular. El problema de revertir el RSA asimétrico decae a un simple problema aritmético de extraer la raíz enésima del criptograma:
$$m = \sqrt[e]{c}$$

### Proceso de explotación:
Se implementó un script en Python para automatizar el ataque de raíz.
1. Se descargó el archivo y se extrajeron las variables $n$, $e$ y $c$ utilizando expresiones regulares para evitar errores de parseo por formato.
2. Se descartó la factorización debido al inmenso tamaño de $n$.
3. Se utilizó la librería de álgebra computacional `sympy`, específicamente la función optimizada en C `integer_nthroot()`, la cual es capaz de calcular raíces de números con miles de dígitos sin pérdida de precisión por punto flotante.
4. El script calculó directamente $m = \sqrt[e]{c}$ y obtuvo una raíz entera exacta al primer intento (con 0 vueltas al módulo, $k=0$).
5. El entero $m$ resultante se convirtió de formato de bytes a caracteres ASCII legibles.

**Bandera final:**
`picoCTF{t1ny_e_2fe2da79}`

# Notas adicionales:
* Este ataque demuestra por qué los estándares de criptografía actuales (como PKCS#1 v1.5 u OAEP) requieren rellenar el mensaje con entropía aleatoria antes de cifrarlo, garantizando siempre que $m^e > n$.
* Intentar sacar la raíz cúbica de un número de miles de dígitos usando funciones tradicionales como `math.pow(c, 1/3)` en Python fallará catastróficamente debido a la limitación de bits de los números de punto flotante flotante (float64). Por ello, el uso de `sympy` o herramientas como GMP es obligatorio.

# Referencias:
* [SymPy: Integer nth root](https://docs.sympy.org/latest/modules/core.html#sympy.core.power.integer_nthroot)
* [RSA Small public exponent attack](https://en.wikipedia.org/wiki/Coppersmith%27s_attack#Small_public_exponent)