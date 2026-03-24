# Sleuthkit Apprentice

# Descripción del reto:

Download this disk image and find the flag. [https://artifacts.picoctf.net/c/136/disk.flag.img.gz](https://artifacts.picoctf.net/c/136/disk.flag.img.gz)

# Solución:

wget [https://artifacts.picoctf.net/c/136/disk.flag.img.gz](https://artifacts.picoctf.net/c/136/disk.flag.img.gz)

gzip -d disk.flag.img.gz

mmls disk.flag.img

fls -r -o 360448 disk.flag.img | grep -i "flag"

icat -o 360448 disk.flag.img 2371

'picoCTF{by73_5urf3r_3497ae6b}'

# Notas adicionales:

- El reto consiste en localizar una bandera dentro de una imagen de disco con múltiples particiones.
    
- Tras descomprimir la imagen, se utilizó `mmls` para identificar la estructura de particiones. Se determinó que la partición principal de Linux comienza en el sector **360448** (offset), siendo esta la más grande y probable contenedora del sistema de archivos raíz.
    
- Se utilizó el comando `fls` con la opción `-r` para realizar una búsqueda recursiva de archivos dentro de la partición especificada por el offset. El filtrado con `grep` reveló dos archivos sospechosos: `flag.txt` (inode 2082) y `flag.uni.txt` (inode 2371).
    
- Mediante el uso de `icat`, se extrajo el contenido de los inodos identificados. El archivo con el inodo 2371 (`flag.uni.txt`) contenía la bandera en texto plano, mientras que el inodo 2082 resultó ser un bloque reasignado con datos irrelevantes.
    

# Referencias:

[https://wiki.sleuthkit.org/index.php?title=Fls](https://wiki.sleuthkit.org/index.php?title=Fls) [https://wiki.sleuthkit.org/index.php?title=Icat](https://wiki.sleuthkit.org/index.php?title=Icat)