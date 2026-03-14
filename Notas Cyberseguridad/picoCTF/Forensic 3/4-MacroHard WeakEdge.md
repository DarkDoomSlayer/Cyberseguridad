# MacroHard WeakEdge

# Descripción del reto:

I've hidden a flag in this file. Can you find it?

# Solución:

mkdir reto_macro && cd reto_macro

wget [https://challenge-files.picoctf.net/c_wily_courier/d78815176c19ddc85a1388233268d2f4c459fcbbaab197b4a29ebafc88294c54/Forensics_is_fun.pptm](https://challenge-files.picoctf.net/c_wily_courier/d78815176c19ddc85a1388233268d2f4c459fcbbaab197b4a29ebafc88294c54/Forensics_is_fun.pptm)

unzip Forensics_is_fun.pptm

find . -name "hidden" -exec cat {} ; | tr -d ' ' | base64 -d && echo ""

'picoCTF{D1d_u_kn0w_ppts_r_z1p5}'

# Notas adicionales:

- Los archivos modernos de Microsoft Office (con extensiones como `.pptx`, `.docx` o `.pptm`) utilizan el estándar Office Open XML (OOXML), lo que significa que en realidad son archivos ZIP que contienen una estructura de carpetas, código XML y recursos multimedia.
    
- Al usar el comando `unzip` sobre la presentación, se puede extraer toda esta estructura sin necesidad de abrir PowerPoint, lo cual es una práctica segura de análisis forense para evitar la ejecución automática de macros maliciosas (almacenadas en el archivo `vbaProject.bin`).
    
- Tras extraer el contenido, se utilizó el comando `find` para localizar un archivo sospechoso llamado `hidden` (ubicado dentro de la carpeta `ppt/slideMasters/`).
    
- El contenido del archivo oculto era una cadena codificada en Base64 pero ofuscada con espacios en blanco. Mediante un _pipeline_ en la terminal, se leyó el archivo con `cat`, se limpiaron los espacios con `tr -d ' '` y finalmente se decodificó usando `base64 -d` para revelar la bandera en texto plano.
    

# Referencias:

[https://linux.die.net/man/1/unzip](https://linux.die.net/man/1/unzip) [https://linux.die.net/man/1/base64](https://linux.die.net/man/1/base64) [https://en.wikipedia.org/wiki/Office_Open_XML](https://en.wikipedia.org/wiki/Office_Open_XML)