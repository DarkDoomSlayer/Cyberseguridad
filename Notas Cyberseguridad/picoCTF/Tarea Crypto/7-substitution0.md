# substitution0

# Descripción del reto:
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher? Download the message `here`.

# Solución:
El reto nos presenta un archivo de texto cifrado mediante un **Cifrado de Sustitución Monoalfabética**. A diferencia del cifrado César (que solo desplaza las letras), este método mezcla el alfabeto de forma arbitraria. La debilidad en este reto en particular es que la primera línea del archivo contiene la llave exacta utilizada para la sustitución (una permutación de 26 caracteres del alfabeto).

### Concepto: Mapeo de Caracteres
Para descifrar el mensaje, solo necesitamos crear una relación bidireccional entre la llave proporcionada y el alfabeto estándar (`A-Z`). 
Si la llave empieza con `ZGSJ...`, significa que la letra 'A' original fue reemplazada por 'Z', la 'B' por 'G', y así sucesivamente. Invirtiendo este mapeo, podemos recuperar el texto plano.

### Proceso de explotación:
Se desarrolló un script en Python para automatizar la extracción y el mapeo:
1. **Parseo del archivo:** Se dividió el archivo descargado por saltos de línea. La línea `0` se asignó como la variable `key`, y el resto del documento se unió como el `ciphertext`.
2. **Tabla de Traducción:** Se utilizó el método nativo `str.maketrans()` de Python. Se mapearon los 26 caracteres de la llave (tanto en mayúsculas como en minúsculas) hacia los 26 caracteres del alfabeto estándar.
3. **Descifrado:** Se aplicó el método `.translate()` sobre el texto cifrado, lo que reemplaza cada carácter en un solo paso computacional (operación $O(N)$), dejando intactos los espacios, números y símbolos de puntuación (como las llaves `{}`).
4. **Extracción de la bandera:** Se utilizó la expresión regular `picoCTF\{.*?\}` sobre el texto ya descifrado para aislar la bandera del resto de la narrativa del mensaje (que resultó ser un fragmento de Sherlock Holmes).

**Bandera final:**
`picoCTF{5UB5717U710N_3V0LU710N_59533A2E}`

# Notas adicionales:
* En casos donde *no* se proporciona la llave (como en retos más avanzados), estos cifrados de sustitución pueden romperse mediante **Análisis de Frecuencias**, contando las letras más repetidas (como la 'E' o la 'A' en inglés) o analizando digramas comunes (como 'TH' o 'HE').
* Python hace que los ataques de sustitución 1 a 1 sean extremadamente eficientes gracias a su manejo nativo de tablas de traducción en cadenas de texto.

# Referencias:
* [Substitution cipher (Wikipedia)](https://en.wikipedia.org/wiki/Substitution_cipher)
* [Python `str.maketrans` documentation](https://docs.python.org/3/library/stdtypes.html#str.maketrans)
