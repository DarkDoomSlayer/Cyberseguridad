
# CanYouSee

# Descripción del reto:

How about some hide and seek? Download this file here.

# Solución:

mkdir reto_canyousee && cd reto_canyousee

wget [https://artifacts.picoctf.net/c_titan/6/unknown.zip](https://artifacts.picoctf.net/c_titan/6/unknown.zip)

unzip unknown.zip

find . -type f -not -name "*.zip" -exec exiftool {} ; | grep -oE "cGlj[a-zA-Z0-9+/=]+" | base64 -d && echo ""

'picoCTF{ME74D47A_HIDD3N_a6df8db8}'

# Notas adicionales:

- El reto es un ejercicio clásico de esteganografía aplicada a los metadatos de un archivo multimedia.
    
- Al descomprimir el archivo ZIP proporcionado, se obtiene la imagen `ukn_reality.jpg`. A simple vista, la imagen no revela ninguna bandera.
    
- Se utilizó la herramienta `exiftool` para extraer toda la información EXIF y propiedades incrustadas en el archivo.
    
- Dentro de los metadatos, se ocultó una cadena ofuscada utilizando codificación Base64.
    
- Mediante el uso de un _pipeline_ en la terminal, se automatizó el proceso: `exiftool` volcó los datos, `grep -oE` filtró exclusivamente la cadena que coincidía con el patrón de Base64 de picoCTF (que suele empezar con `cGlj`), y finalmente `base64 -d` tradujo esa cadena a texto plano, revelando la bandera oculta.
    

# Referencias:

[https://linux.die.net/man/1/exiftool](https://linux.die.net/man/1/exiftool) [https://linux.die.net/man/1/grep](https://linux.die.net/man/1/grep)