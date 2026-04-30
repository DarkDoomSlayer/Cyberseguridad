# vault-door-5

# Descripción del reto:
In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding!
The source code for this vault is here: `VaultDoor5.java`

# Solución:
En este reto de Ingeniería Inversa, el mecanismo de validación somete la entrada del usuario a un proceso de doble codificación antes de compararla con una cadena estática. 

### Vulnerabilidad: Codificación Insegura (Double Encoding)
La validación consta de dos pasos estándar:
1. **URL Encoding:** Convierte caracteres en un formato seguro para transmisión web (ej. el espacio se vuelve `%20`, la 'c' minúscula `%63`).
2. **Base64 Encoding:** Traduce bytes a un formato ASCII seguro utilizando un alfabeto de 64 caracteres, reconocible por su sufijo de relleno (padding) `=`.

La vulnerabilidad fundamental es que la codificación (Encoding) a menudo se confunde con el cifrado (Encryption). Debido a que Base64 y URL Encoding carecen de claves secretas, cualquier adversario que identifique el tipo de codificación puede revertirlo utilizando decodificadores estándar.

### Proceso de explotación:
Se desarrolló un script en Python para invertir el flujo de validación:
1. Se descargó el archivo fuente `VaultDoor5.java`.
2. Se extrajo mediante Expresiones Regulares la cadena almacenada en la variable `expected`. El script consideró la sintaxis de Java para concatenar cadenas fragmentadas (`"..." + "..."`).
3. Se aplicó la función `base64.b64decode()` al texto extraído, obteniendo una cadena en formato URL (`%63%30%6e...`).
4. Se aplicó la función `urllib.parse.unquote()` sobre el resultado anterior para resolver la sustitución de caracteres y recuperar el texto plano.

**Bandera final:**
picoCTF{c0nv3rt1ng_fr0m_ba5e_64_4185551e}

# Notas adicionales:
* En auditorías de seguridad reales (Pentesting), es muy común encontrar contraseñas, JWTs (JSON Web Tokens) o información sensible codificada exclusivamente en Base64 dentro de cookies o cabeceras HTTP. Descifrar este tipo de "protección" suele ser el primer paso en un ataque a aplicaciones web.

# Referencias:
* [Base64 (Wikipedia)](https://en.wikipedia.org/wiki/Base64)
* [Percent-encoding / URL Encoding (Wikipedia)](https://en.wikipedia.org/wiki/Percent-encoding)