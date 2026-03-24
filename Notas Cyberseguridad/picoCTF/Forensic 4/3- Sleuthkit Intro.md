# Sleuthkit Intro

# Descripción del reto:

Download the disk image and use `mmls` on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag. [https://artifacts.picoctf.net/c/164/disk.img.gz](https://artifacts.picoctf.net/c/164/disk.img.gz) Access checker program: `nc saturn.picoctf.net 59864`

# Solución:

wget [https://artifacts.picoctf.net/c/164/disk.img.gz](https://artifacts.picoctf.net/c/164/disk.img.gz)

gzip -d disk.img.gz

mmls disk.img

nc saturn.picoctf.net 59864

'picoCTF{mm15_f7w!}'

# Notas adicionales:

- El reto introduce el uso de la herramienta `mmls` de **The Sleuth Kit (TSK)**, la cual permite visualizar el diseño de las particiones dentro de un archivo de imagen de disco.
    
- Tras descomprimir la imagen con `gzip -d`, se ejecutó `mmls` para analizar la tabla de particiones DOS. Se identificó la partición de tipo "Linux (0x83)" en el slot 002.
    
- Se extrajo el valor de la columna **Length** (202752), que representa el tamaño de la partición en sectores de 512 bytes.
    
- Finalmente, se utilizó `nc` (Netcat) para conectarse al servicio remoto del reto. Al proporcionar el valor de la longitud obtenido, el servidor validó la respuesta y entregó la bandera.
    

# Referencias:

[https://wiki.sleuthkit.org/index.php?title=Mmls](https://wiki.sleuthkit.org/index.php?title=Mmls) [https://linux.die.net/man/1/nc](https://linux.die.net/man/1/nc)