# Glory of the Garden
# Descripción del reto:
This file contains more than it seems. Get the flag from garden.jpg.
# Solución:
dark@kali:~$ wget https://challenge-files.picoctf.net/c_fickle_tempest/150b6eaad43200d3dc91f98c390e4c6168620b57d0b95a7e9d04c92910bbbe16/garden.jpg

dark@kali:~$ strings garden.jpg | grep pico
Here is a flag: picoCTF{more_than_m33ts_the_3y3a63b5b27}

'picoCTF{more_than_m33ts_the_3y3a63b5b27}'

# Notas adicionales:
El reto es una introducción básica al análisis forense de archivos. La herramienta 'strings' extrae secuencias de caracteres imprimibles ocultas dentro de archivos binarios (como imágenes). La bandera estaba inyectada en texto plano dentro del código de la imagen original, la cual debe descargarse sin alteraciones para evitar que se corrompa la data inyectada.
# Referencias: