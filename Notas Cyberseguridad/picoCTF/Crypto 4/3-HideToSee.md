# HideToSee

# Descripción del reto:
How about some hide and seek heh? Look at this image `here`.

# Solución:
El reto proporciona un archivo de imagen llamado `atbash.jpg`. El problema requiere la combinación de dos disciplinas: esteganografía para la extracción de datos y criptografía clásica para el descifrado.

### Vulnerabilidades:
1. **Esteganografía sin autenticación:** Se ocultó información dentro del archivo JPEG utilizando herramientas convencionales sin establecer una frase de contraseña (passphrase vacía).
2. **Cifrado de sustitución simple (Atbash):** El nombre del archivo (`atbash.jpg`) actúa como indicador del algoritmo criptográfico utilizado. Atbash es un cifrado de sustitución monoalfabética que mapea el alfabeto a su reverso absoluto (A $\leftrightarrow$ Z, B $\leftrightarrow$ Y). Al ser estático, no requiere llave y es trivialmente reversible.

### Proceso de explotación:
Se desarrolló un script en Python para automatizar la cadena de ataque:
1. **Extracción Esteganográfica:** Se invocó el binario `steghide` mediante subprocesos en Python, apuntando a la imagen descargada con el argumento de contraseña en blanco (`-p ""`). Esto extrajo exitosamente un archivo de texto plano llamado `encrypted.txt`.
2. **Lectura de Criptograma:** El texto extraído mantenía el formato de la bandera pero con los caracteres alfabéticos sustituidos.
3. **Decodificación Atbash:** Se iteró sobre la cadena de texto y se aplicó una transformación matemática basada en los valores ASCII de los caracteres. Para mantener el formato intacto, solo las letras (mayúsculas y minúsculas) fueron invertidas, dejando los números y símbolos especiales inalterados.

**Bandera final:**
'picoCTF{atbash_crack_05b2a65a}'

# Notas adicionales:
* Herramientas como `steghide` son capaces de inyectar datos en archivos de audio e imagen (JPEG, BMP, WAV, AU) aprovechando los bits menos significativos (LSB) u otras técnicas de compresión para evitar alterar la apariencia visual.
* Los cifrados de sustitución como Atbash o ROT13 carecen de seguridad moderna y son fácilmente detectables mediante análisis de frecuencias o ingeniería inversa basada en el contexto (como reconocer el prefijo `picoCTF{`).

# Referencias:
* [Steghide Documentation](https://steghide.sourceforge.net/)
* [Atbash Cipher](https://en.wikipedia.org/wiki/Atbash)