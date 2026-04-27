# credstuff

# Descripción del reto:
We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it? Download the leak `here`.
The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.

# Solución:
El reto nos presenta un escenario de análisis forense sobre un volcado de datos (data leak) empaquetado en un archivo `.tar`. Al extraerlo, obtenemos dos archivos de texto (`usernames.txt` y `passwords.txt`) que funcionan bajo una estructura de base de datos relacional implícita (arreglos paralelos), donde el índice de línea correlaciona ambos registros.

### Vulnerabilidad: Almacenamiento Inseguro y Cifrado ROT13
La base de datos filtrada no utiliza funciones de hash criptográficas unidireccionales (como bcrypt o SHA-256) para almacenar las contraseñas. En su lugar, utiliza un esquema de ofuscación trivial basado en **ROT13**, una variante del cifrado César que simplemente desplaza cada letra 13 posiciones en el alfabeto. Dado que el alfabeto inglés tiene 26 letras, aplicar ROT13 dos veces devuelve el texto original, lo que lo hace completamente inseguro.

### Proceso de explotación:
Se desarrolló un script en Python para automatizar el análisis del volcado:
1. **Extracción:** Se descargó y extrajo el archivo comprimido `leak.tar` utilizando la librería nativa `tarfile`.
2. **Correlación de Índices:** Se cargaron ambos archivos de texto en memoria como listas. Se utilizó la función `index()` para buscar la posición exacta de la cadena `cultiris` dentro del arreglo de usuarios.
3. **Extracción de Credenciales:** Con el índice identificado, se extrajo la cadena correspondiente en el arreglo de contraseñas.
4. **Decodificación:** El criptograma obtenido tenía el formato de la bandera pero con los caracteres alterados. Se aplicó la función `codecs.decode(..., 'rot_13')` para revertir la sustitución alfabética y recuperar el texto plano original.

**Bandera final:**
'picoCTF{C7r1F_54V35_71M3}'

# Notas adicionales:
* En sistemas reales, una filtración de este tipo es crítica. Las credenciales deben ser almacenadas utilizando *salting* y *hashing* fuerte para evitar que un volcado de datos exponga las contraseñas en texto plano o fácilmente reversibles.
* Este reto enfatiza la diferencia entre *ofuscación* (como Base64 o ROT13) y *cifrado real* (como AES).

# Referencias:
* [ROT13 (Wikipedia)](https://en.wikipedia.org/wiki/ROT13)
* [Python codecs module](https://docs.python.org/3/library/codecs.html)