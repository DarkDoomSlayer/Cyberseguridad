# hashcrack

# Descripción del reto:
A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?
Access the server using `nc verbal-sleep.picoctf.net 59633`

# Solución:
El reto expone un servicio TCP interactivo que simula un panel de autenticación o verificación. Al conectarse, el servidor entrega el hash de una contraseña y espera recibir la contraseña original en texto plano para liberar el acceso (la bandera).

### Vulnerabilidad: Hashing Débil (Diccionarios Predecibles)
Las funciones de hash (como MD5, SHA-1 o SHA-256) son algoritmos matemáticos unidireccionales diseñados para no ser reversibles. Sin embargo, si la contraseña original es débil (por ejemplo, "password123" o "admin"), el hash resultante es vulnerable a **Ataques de Diccionario** o de **Fuerza Bruta**. El atacante solo necesita calcular el hash de una lista de palabras comunes y compararlo con el hash objetivo hasta encontrar una coincidencia.

### Proceso de explotación:
Se desarrolló un script ofensivo en Python utilizando las librerías `pwntools`, `hashlib` y `re` (expresiones regulares) para automatizar el ciclo de ataque en milisegundos.
1. **Wordlist en memoria:** El script realiza una petición HTTP en segundo plano para descargar la lista *10k-most-common.txt* (de SecLists) directamente en la memoria del programa.
2. **Conexión y Parseo:** Se estableció un socket contra el servidor de la competencia y se capturó la salida inicial. Utilizando expresiones regulares, se identificó dinámicamente un hash hexadecimal válido y se determinó su algoritmo basándose en la longitud (32 caracteres para MD5, 40 para SHA1, 64 para SHA256).
3. **Cracking Local:** El script iteró sobre las 10,000 contraseñas, aplicando la misma función de hash criptográfico a cada una hasta obtener una firma idéntica a la del servidor.
4. **Bypass:** Al encontrar la colisión (el texto plano original), este se envió de regreso a través del socket, autenticando el desafío y recibiendo la bandera como respuesta.

**Bandera final:**
`picoCTF{UseStr0nG_h@shEs_&PaSswDs!_4de57566}`

# Notas adicionales:
* Este es el principio fundamental detrás de herramientas como *Hashcat* o *John the Ripper*. 
* La única forma de mitigar los ataques de diccionario en almacenamiento de contraseñas es exigiendo contraseñas con alta entropía (complejidad) y aplicando un *Salt* (cadena aleatoria única) antes de generar el hash, haciendo que los diccionarios y las *Rainbow Tables* precalculadas sean inútiles.

# Referencias:
* [SecLists - Passwords (GitHub)](https://github.com/danielmiessler/SecLists/tree/master/Passwords)
* [Python hashlib documentation](https://docs.python.org/3/library/hashlib.html)