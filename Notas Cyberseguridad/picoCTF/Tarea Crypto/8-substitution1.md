# substitution1

# Descripción del reto:
A second message has come in the mail, and it seems almost identical to the first one. Maybe the same thing will work again. Download the message `here`.

# Solución:
El reto nos presenta un texto cifrado mediante un **Cifrado de Sustitución Monoalfabética**, pero a diferencia del nivel anterior (`substitution0`), el autor ha omitido la llave de sustitución en el archivo. Esto simula un escenario de intercepción real donde solo poseemos el criptograma.

### Concepto: Análisis de Frecuencias y Texto Conocido
Para romper una sustitución monoalfabética sin la llave, se recurre a dos técnicas:
1. **Análisis de Frecuencias:** Las letras en el idioma inglés tienen una distribución de probabilidad predecible (la 'e' es la más común, seguida de la 't', 'a', 'o', etc.). Contando la frecuencia de los caracteres en el criptograma, se pueden inferir sus equivalentes en texto plano.
2. **Known-Plaintext Attack (KPA):** Sabemos que la bandera tiene el formato `picoCTF{...}`. Si buscamos un patrón de caracteres en el criptograma que tenga la estructura `abcdEFG{...}`, podemos derivar inmediatamente 7 letras de la llave.

### Proceso de explotación:
Dado que programar un motor de análisis de frecuencias manual desde cero es ineficiente y propenso a errores por variaciones estadísticas, la aproximación estándar en auditorías y CTFs es utilizar solvers heurísticos.
1. Se interceptó y copió el texto cifrado completo.
2. Se procesó el criptograma a través del motor de fuerza bruta estadística **quipqiup**.
3. El algoritmo evaluó las frecuencias y la topología de las palabras contra un diccionario de idioma inglés, deduciendo la llave subyacente de forma automática.
4. Se inspeccionó el texto plano resultante para localizar y extraer el formato de la bandera.

**Bandera final:**
`picoCTF{FR3QU3NCY_4774CK5_4R3_C001_6E0659FB}`

# Notas adicionales:
* El análisis de frecuencias demuestra por qué los cifrados de sustitución clásicos (César, Vigenère simple, etc.) se consideran criptográficamente rotos desde hace siglos. No ocultan la estructura ni los patrones estadísticos del mensaje original.
* Quipqiup es una herramienta indispensable en el arsenal de cualquier jugador de CTF para resolver criptogramas de sustitución rápidamente.

# Referencias:
* [Frequency analysis (Wikipedia)](https://en.wikipedia.org/wiki/Frequency_analysis)
* [quipqiup - Automated cryptogram solver](https://quipqiup.com/)