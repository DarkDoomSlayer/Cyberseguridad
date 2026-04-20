# Mind your Ps and Qs

# Descripción del reto:
In RSA, a small e value can be problematic, but what about N? Can you decrypt this? `values`

# Solución:
El reto nos proporciona un archivo de texto con los parámetros $c$ (texto cifrado), $n$ (módulo) y $e$ (exponente público). La pista clave en la descripción sugiere analizar la viabilidad del módulo $N$.

### Vulnerabilidad: Módulo débil (Factorización)
La seguridad del algoritmo RSA recae enteramente en la dificultad computacional de factorizar un número semiprimo gigante ($N$) en sus componentes primos ($p$ y $q$). Si la longitud en bits de $N$ es pequeña (en este caso, apenas 81 dígitos), es vulnerable a algoritmos matemáticos como la Criba General del Cuerpo de Números (GNFS) o puede encontrarse previamente calculado en bases de datos de dominio público.

### Proceso de explotación:
1. **Extracción y Análisis:** Se descargaron los valores y se analizó la longitud de $N$ (81 dígitos, extremadamente débil).
2. **Factorización:** En lugar de intentar cálculos computacionalmente pesados localmente, se elaboró un script en Python que consultó la API REST de **FactorDB** (`factordb.com`), una base de datos en línea de números factorizados, obteniendo $p$ y $q$ al instante.
3. **Cálculo de Llaves:** Al obtener $p$ y $q$ de la base de datos, el resto del criptosistema quedó expuesto. Se calculó la función totiente de Euler:
   $$\phi(N) = (p-1)(q-1)$$
4. **Descifrado:** Se calculó la llave privada $d$ hallando el inverso multiplicativo modular de $e$:
   $$d \equiv e^{-1} \pmod{\phi(N)}$$
   Finalmente, se aplicó la llave privada sobre el criptograma para recuperar el texto plano original:
   $$M = c^d \pmod N$$

El número $M$ resultante se transformó a representación de cadena de bytes (ASCII). La cadena resultante estaba invertida por cuestiones de *endianness*, por lo que al leerla de atrás hacia adelante se desveló la bandera.

**Bandera final:**
`picoCTF{sma11_N_n0_g0od_1dc7ae91}`

# Notas adicionales:
* Este reto demuestra por qué generar llaves RSA con suficiente entropía y tamaño (mínimo 2048 bits según estándares actuales del NIST) es vital en ciberseguridad.
* La automatización de la consulta a bases de datos externas como FactorDB ahorra horas de cómputo en auditorías y competencias tipo CTF.

# Referencias:
* [FactorDB](http://factordb.com/)
* [RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))