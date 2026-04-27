# EVEN RSA CAN BE BROKEN???

# Descripción del reto:
This service provides you an encrypted flag. Can you decrypt it with just N & e?
Connect to the program with netcat: `nc verbal-sleep.picoctf.net 54593`

# Solución:
El reto nos presenta un servicio TCP que nos devuelve los parámetros públicos de un cifrado RSA ($N$, $e$) junto con el texto cifrado ($c$). El título del reto utiliza un juego de palabras con "EVEN" (Incluso / Par), sugiriendo una anomalía matemática en la generación del módulo $N$.

### Vulnerabilidad: Módulo RSA Par (Factorización Trivial)
En una implementación segura de RSA, el módulo $N$ es el producto de dos números primos grandes ($p$ y $q$). Dado que todos los números primos mayores a 2 son impares, el producto de dos impares resultará siempre en un módulo $N$ impar.

Si un sistema genera un módulo $N$ que es un número **par**, significa obligatoriamente que uno de sus factores primos es el número **2**. Esto reduce la complejidad computacional de la factorización a una simple división aritmética:
$$p = 2$$
$$q = \frac{N}{2}$$

Al conocer $p$ y $q$, la seguridad del esquema RSA se rompe por completo, ya que se puede calcular la función totiente de Euler y derivar la llave privada.

### Proceso de explotación:
Se desarrolló un script en Python utilizando `pwntools` para interactuar con la instancia remota y automatizar el cálculo.
1. Se capturaron los valores de $N$, $e$ y $c$ desde la salida del socket TCP.
2. Se verificó mediante una operación de módulo aritmético que $N \pmod 2 == 0$.
3. Se asignaron los factores triviales: $p = 2$ y $q = N / 2$.
4. Se calculó el totiente $\phi(N)$ utilizando la fórmula:
   $$\phi(N) = (p - 1) \cdot (q - 1)$$
   Al ser $p=2$, la fórmula se simplifica lógicamente a $\phi(N) = 1 \cdot (q - 1) = q - 1$.
5. Se obtuvo la llave privada $d$ calculando el inverso multiplicativo modular:
   $$d \equiv e^{-1} \pmod{\phi(N)}$$
6. Se descifró el criptograma mediante la operación $M = c^d \pmod N$ y se decodificó de formato bytes a ASCII.

**Bandera final:**
`picoCTF{tw0_1$_pr!m3df98b648}`

# Notas adicionales:
* Generar primos para RSA utilizando generadores de números pseudoaleatorios (PRNG) defectuosos o sin verificar la paridad de los candidatos es un error crítico en la programación criptográfica.
* Este ataque demuestra que la seguridad de RSA no recae en el tamaño de $N$, sino en la imposibilidad de hallar sus componentes $p$ y $q$. Si uno de los componentes se revela o se vuelve obvio, no importa si $N$ tiene 4096 bits.