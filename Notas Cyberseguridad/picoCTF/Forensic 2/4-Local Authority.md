# like1000

# Descripción del reto:

This .tar file got tarred a lot.

# Solución:

mkdir reto_1000 && cd reto_1000

wget [https://challenge-files.picoctf.net/c_fickle_tempest/96ad54735d25c18a159eb22cd408adc8dad73f855113b1b700a769d4fa9f2c10/1000.tar](https://challenge-files.picoctf.net/c_fickle_tempest/96ad54735d25c18a159eb22cd408adc8dad73f855113b1b700a769d4fa9f2c10/1000.tar)

for i in {1000..1}; do tar -xf $i.tar 2>/dev/null && rm $i.tar; done

ls -la

xdg-open flag.png

'picoCTF{l0t5_0f_TAR5}'

# Notas adicionales:

- El reto consiste en un archivo comprimido dentro de otro archivo comprimido, repitiendo este patrón estilo "Matryoshka" (muñecas rusas) exactamente 1000 veces (desde `1000.tar` hasta `1.tar`).
    
- Realizar la extracción de forma manual es ineficiente. La mejor estrategia forense para estos casos es la automatización.
    
- Se utilizó un bucle `for` en Bash que itera en orden inverso (de 1000 a 1). En cada iteración, el comando `tar -xf` extrae el contenido, y `rm` elimina el archivo `.tar` procesado para limpiar el directorio y evitar la saturación del disco.
    
- Al finalizar el proceso masivo, los únicos archivos sobrevivientes son un archivo basura (`filler.txt`) y la imagen final (`flag.png`), la cual contiene la bandera inyectada de forma gráfica.
    

# Referencias:

[https://linux.die.net/man/1/tar](https://linux.die.net/man/1/tar) [https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html](https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html)