# Secret of the Polyglot

# Descripción del reto:

The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?

# Solución:

mkdir reto_polyglot && cd reto_polyglot

wget [https://artifacts.picoctf.net/c_titan/9/flag2of2-final.pdf](https://artifacts.picoctf.net/c_titan/9/flag2of2-final.pdf)

pdftotext flag2of2-final.pdf -

head -c 914 flag2of2-final.pdf > imagen_limpia.png && xdg-open imagen_limpia.png

'picoCTF{f1u3n7_1n_pn9_&_pdf_7f9bccd1}'

# Notas adicionales:

- El reto explora el concepto de archivos "políglotas" (polyglots), que son archivos manipulados a nivel hexadecimal para ser estructuralmente válidos en múltiples formatos al mismo tiempo (en este caso, un híbrido de PDF y PNG).
    
- Al tratar el archivo como un documento PDF utilizando `pdftotext`, se extrajo la capa de texto plano, la cual contenía la segunda mitad de la bandera.
    
- Debido a que los visores de imágenes modernos en Linux leen los "Magic Bytes" y se confunden con la cabecera del PDF incrustado, la herramienta `binwalk` reveló que la estructura PNG terminaba en el byte 914.
    
- Se utilizó el comando `head -c 914` para rebanar el archivo exactamente en ese punto, descartando la basura del PDF y extrayendo la imagen pura, la cual reveló visualmente la primera mitad de la bandera.
    

# Referencias:

[https://en.wikipedia.org/wiki/Polyglot_(computing](https://en.wikipedia.org/wiki/Polyglot_\(computing\))