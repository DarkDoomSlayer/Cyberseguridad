# information

# Descripción del reto:

Files can always be changed in a secret way. Can you find the flag?

# Solución:

exiftool cat.jpg

# Identificamos una cadena anómala codificada en Base64 en el campo "License"

echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d

'picoCTF{the_m3tadata_1s_modified}'

# Notas adicionales:

- La pista central del reto menciona modificaciones "secretas" a los archivos, lo que en análisis forense de imágenes apunta directamente a la manipulación de metadatos (EXIF data).
    
- Se utilizó la herramienta `exiftool` para extraer y enumerar toda la metadata incrustada estructuralmente en el archivo `cat.jpg`.
    
- Durante la inspección de los campos de metadatos, se identificó un valor sospechoso en la etiqueta `License`. Este valor correspondía a una cadena de texto ofuscada utilizando el esquema de codificación Base64.
    
- Al pasar esa cadena por el decodificador estándar `base64 -d` directamente en la terminal, se reveló la bandera oculta en texto plano, demostrando que la imagen fue alterada a nivel de propiedades.
    

# Referencias:

[https://linux.die.net/man/1/exiftool](https://linux.die.net/man/1/exiftool) [https://linux.die.net/man/1/base64](https://linux.die.net/man/1/base64)