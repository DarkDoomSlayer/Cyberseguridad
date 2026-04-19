# b00tl3gRSA3

# Descripción del reto:
Why use p and q when I can use more? Connect with `nc fickle-tempest.picoctf.net 65478`.

# Solución:
El reto expone una implementación asimétrica de RSA a través de una conexión TCP. Al analizar el enunciado ("¿Por qué usar p y q cuando puedo usar más?"), se deduce de inmediato que estamos ante una arquitectura **Multi-prime RSA**, donde el módulo $N$ no es el producto de dos números primos, sino de múltiples primos.

### Vulnerabilidad: Multi-prime RSA y Primos Pequeños
Aunque usar más de dos primos es una variante matemática válida, en el contexto de la generación de llaves de este reto, fragmentar $N$ en decenas de factores provoca que cada número primo individual sea extremadamente pequeño. Al ser diminutos, estos componentes son susceptibles a ataques de factorización rápida matemática en procesadores convencionales.

### Proceso de explotación:
Se desarrolló un exploit híbrido que utiliza Python para la conexión de red y la orquestación, y el motor **PARI/GP** (escrito en C) para el cálculo matemático pesado.

1. **Extracción:** El script de Python (`pwntools`) se conectó a la instancia dinámica generada por el servidor y extrajo los valores $c$, $n$ y $e$.
2. **Factorización Local de Alto Rendimiento:** Dado que $N$ se generó en tiempo real, no existía en repositorios públicos. El script invocó un subproceso llamando a la herramienta `gp` (PARI/GP), pasándole el valor de $N$. El motor logró destrozar el módulo en **34 factores primos distintos** en fracciones de segundo.
3. **Cálculo de Totiente Extendido:** Para que el algoritmo RSA funcione con múltiples primos, la función totiente de Euler $\phi(N)$ se adaptó iterando sobre los 34 factores ($p_i$) devueltos por PARI/GP:
   $$\phi(N) = (p_1 - 1) \cdot (p_2 - 1) \cdot (p_3 - 1) \dots (p_{34} - 1)$$
4. **Descifrado:** Tras calcular $\phi(N)$, se generó la llave privada $d$:
   $$d \equiv e^{-1} \pmod{\phi(N)}$$
   Finalmente, se aplicó la desencriptación estándar $M = c^d \pmod N$ y se decodificaron los bytes resultantes.

**Bandera final:**
`picoCTF{too_many_fact0rs_3023548}`

# Notas adicionales:
* Este reto demuestra que añadir "complejidad" (más números primos) no se traduce en mayor seguridad si los fundamentos matemáticos de entropía y tamaño de bit no se respetan.
* El uso de herramientas especializadas como PARI/GP o SageMath es indispensable en criptoanálisis, ya que lenguajes de alto nivel como Python puro no están optimizados para algoritmos de criba o factorización elíptica a gran escala.

# Referencias:
* [PARI/GP](https://pari.math.u-bordeaux.fr/)
* [RSA Variants (Multi-prime)](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Variants)