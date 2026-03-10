# So Meta
# Descripción del reto:
Find the flag in this picture.
# Solución:
wget https://challenge-files.picoctf.net/c_fickle_tempest/d534c920bd33d42b413e67d21cacbf7aa232c4823ce29872eca285471558f00a/pico_img.png

dark@kali:~$ exiftool pico_img.png | grep picoCTF
Artist                          : picoCTF{s0_m3ta_74af23ab}

'picoCTF{s0_m3ta_74af23ab}'

# Notas adicionales:
El análisis forense revela que los archivos multimedia contienen metadatos (información sobre el archivo, como fecha, ubicación o autor). La herramienta de línea de comandos 'exiftool' permite extraer estos metadatos. En este caso, la bandera fue inyectada intencionalmente como texto plano en la propiedad "Artist" (Artista) de la imagen PNG.
# Referencias: