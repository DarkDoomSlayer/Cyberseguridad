# Timeline 1

# Descripción del reto:

Can you find the flag in this disk image? Wrap what you find in the picoCTF flag format.
# Solución:

fls -r -m / partition4.img > body.txt

mactime -b body.txt > timeline.txt

mkdir mnt_p4

sudo mount -o loop partition4.img mnt_p4

cat mnt_p4/etc/chat NTczNDE3aDEzcl83aDRuXzdoM18xNDU3XzU4NTI3YmIyMjIK

echo "NTczNDE3aDEzcl83aDRuXzdoM18xNDU3XzU4NTI3YmIyMjIK" | base64 -d 573417h13r_7h4n_7h3_1457_58527bb222

'picoCTF{573417h13r_7h4n_7h3_1457_58527bb222}'

# Notas adicionales:

- El análisis forense de la línea de tiempo (Timeline) permite identificar archivos creados o modificados en fechas específicas que no coinciden con la instalación original del sistema.
    
- Se detectó actividad sospechosa el **1 de diciembre de 2025**, lo que llevó al descubrimiento del archivo `/etc/chat`.
    
- El archivo contenía una cadena en **Base64**, una técnica de codificación común para ocultar texto simple de escaneos rápidos como `grep`.
    
- Al decodificar la cadena y aplicar el formato requerido, se obtuvo la bandera final.
    

_y recuerden, esta es la historia que los pixeles nos han dejado..._
# Referencias:

[https://sleuthkit.org/sleuthkit/man/fls.html](https://www.google.com/search?q=https://sleuthkit.org/sleuthkit/man/fls.html) [https://sleuthkit.org/sleuthkit/man/mactime.html](https://www.google.com/search?q=https://sleuthkit.org/sleuthkit/man/mactime.html)