# basic-mod1

# Descripción del reto:
We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Download the message `here`.
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

# Solución:
El reto nos presenta un archivo de texto (`message.txt`) que contiene una serie de números enteros separados por espacios. La descripción detalla un algoritmo de codificación personalizado basado en aritmética modular y sustitución de caracteres.

### Vulnerabilidad: Codificación Personalizada (Sustitución Simple)
Más que una vulnerabilidad criptográfica real, este reto presenta un esquema de codificación (encoding) simple. La debilidad principal de los esquemas de sustitución de índice directo es que la lógica es trivialmente reversible si se conoce el algoritmo de mapeo (la tabla de sustitución) y la operación matemática aplicada a la entrada original. 

La operación aplicada a cada número $n$ es:
$$v \equiv n \pmod{37}$$

Donde el valor resultante $v$ siempre estará en el rango de $0$ a $36$.

### Proceso de explotación:
Se desarrolló un script en Python para parsear el archivo y decodificar el mensaje numérico aplicando las reglas de conversión descritas.

1. **Extracción y Parseo:** Se descargó el archivo de texto y se separó la cadena de caracteres utilizando los espacios como delimitadores, generando una lista de enteros.
2. **Operación Modular:** Se iteró sobre la lista, aplicando la operación de módulo 37 a cada número.
3. **Mapeo de Caracteres:** Dependiendo del valor resultante $v$, se realizó el siguiente mapeo basado en la tabla de código ASCII:
   * Si $0 \le v \le 25$: Se sumó 65 para obtener letras mayúsculas de la 'A' a la 'Z'.
   * Si $26 \le v \le 35$: Se restó 26 y se sumó 48 para obtener los caracteres numéricos del '0' al '9'.
   * Si $v = 36$: Se asignó directamente el carácter guion bajo `_`.
4. **Ensamblado:** Los caracteres decodificados se concatenaron secuencialmente y se envolvieron en el formato estándar de la bandera (`picoCTF{...}`).

**Bandera final:**
'picoCTF{R0UND_N_R0UND_ADD17EC2}'

# Notas adicionales:
* Este ejercicio sirve como introducción a las operaciones con módulos que son la base teórica subyacente para esquemas de encriptación asimétrica reales, como RSA o Diffie-Hellman.
* La operación de módulo asegura que sin importar el tamaño del número original de entrada, la salida siempre mapeará limpiamente al índice del conjunto de caracteres limitados (de 37 elementos).