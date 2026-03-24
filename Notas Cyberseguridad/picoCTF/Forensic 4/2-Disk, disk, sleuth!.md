# Disk, disk, sleuth!

# Descripción del reto:

Use srch_strings from the sleuthkit and some terminal-fu to find a flag in this disk image. [https://challenge-files.picoctf.net/c_wily_courier/7317ac746dd0d2429c9f16875e0c4b41673375678a980746ea9b618f8ed6aa72/dds1-alpine.flag.img.gz](https://challenge-files.picoctf.net/c_wily_courier/7317ac746dd0d2429c9f16875e0c4b41673375678a980746ea9b618f8ed6aa72/dds1-alpine.flag.img.gz)

# Solución:

wget [https://challenge-files.picoctf.net/c_wily_courier/7317ac746dd0d2429c9f16875e0c4b41673375678a980746ea9b618f8ed6aa72/dds1-alpine.flag.img.gz](https://challenge-files.picoctf.net/c_wily_courier/7317ac746dd0d2429c9f16875e0c4b41673375678a980746ea9b618f8ed6aa72/dds1-alpine.flag.img.gz)

gzip -d dds1-alpine.flag.img.gz

srch_strings dds1-alpine.flag.img | grep "picoCTF{"

'picoCTF{f0r3ns1c4t0r_n30phyt3_5e56e786}'

# Notas adicionales:

- El reto consiste en extraer información legible de una imagen de disco comprimida (`.img.gz`).
    
- Tras descargar el archivo con `wget`, se utiliza `gzip -d` para descomprimirlo y obtener la imagen de disco en crudo.
    
- Se emplea la herramienta `srch_strings`, que forma parte del paquete **The Sleuth Kit (TSK)**, diseñada para el análisis forense de sistemas de archivos. A diferencia del comando `strings` convencional, `srch_strings` es capaz de extraer cadenas de texto de áreas específicas de una imagen de disco que podrían pasar desapercibidas.
    
- Al canalizar la salida hacia `grep`, se filtra la cadena que cumple con el formato de la bandera, localizándola dentro de los datos binarios de la imagen de Alpine Linux.
    

# Referencias:

[https://wiki.sleuthkit.org/index.php?title=Srch_strings](https://www.google.com/search?q=https://wiki.sleuthkit.org/index.php%3Ftitle%3DSrch_strings) [https://linux.die.net/man/1/grep](https://linux.die.net/man/1/grep)

---