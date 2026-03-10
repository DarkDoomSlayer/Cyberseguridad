# extensions
# Descripción del reto:
This is a really weird text file TXT? Can you find the flag?
# Solución:
wget https://challenge-files.picoctf.net/c_fickle_tempest/31fe772e6a4c71e867af0b2a93818e06d8f8ebf8af2a9615495d00356ff576da/flag.txt

file flag.txt
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced

dark@kali:~$ mv flag.txt flag.png

* Se procedió a abrir el archivo flag.png con el visor de imágenes del sistema.
* Al visualizar la imagen, se observó que la bandera estaba escrita gráficamente sobre un fondo blanco.

'picoCTF{now_you_know_about_extensions}'

# Notas adicionales:
* Los "Magic Bytes" al inicio de un archivo definen su tipo real, independientemente de la extensión que tenga.
* El comando 'file' permitió identificar que el archivo .txt era en realidad un .png.
* Una vez corregida la extensión, el software de visualización pudo renderizar la imagen correctamente para revelar el secreto.
# Referencias: