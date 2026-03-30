# Redaction gone wrong

# Descripción del reto:

Now you DON’T see me. This report has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?

# Solución:

mkdir reto_redaction && cd reto_redaction

wget [https://artifacts.picoctf.net/c/84/Financial_Report_for_ABC_Labs.pdf](https://artifacts.picoctf.net/c/84/Financial_Report_for_ABC_Labs.pdf)

pdftotext Financial_Report_for_ABC_Labs.pdf - | grep "picoCTF{"

'picoCTF{C4n_Y0u_S33_m3_fully}'

# Notas adicionales:

- El reto expone una vulnerabilidad humana muy común en la seguridad de la información: la falsa censura de documentos (redaction fail).
    
- Al intentar ocultar información sensible en un PDF, a menudo los usuarios simplemente dibujan formas geométricas (como rectángulos negros) sobre el texto usando editores visuales. Sin embargo, esto solo añade una capa gráfica superpuesta; el texto original sigue existiendo en el código fuente del documento y puede ser seleccionado o extraído.
    
- Para vulnerar esta "censura", se utilizó la herramienta `pdftotext`, la cual ignora completamente el renderizado visual (imágenes, formas, colores) y extrae únicamente los datos en texto plano.
    
- Al pasar la salida en crudo hacia el comando `grep`, se localizó instantáneamente la cadena con el formato de la bandera que estaba oculta bajo uno de los bloques negros.
    

# Referencias:

[https://linux.die.net/man/1/pdftotext](https://linux.die.net/man/1/pdftotext)