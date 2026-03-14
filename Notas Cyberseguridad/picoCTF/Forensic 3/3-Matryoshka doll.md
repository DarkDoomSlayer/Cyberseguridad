# Matryoshka doll

# Descripción del reto:

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one?

# Solución:

mkdir reto_dolls && cd reto_dolls

wget [https://challenge-files.picoctf.net/c_wily_courier/0f5ef9c383aa83d319ccb01805f4b9499934bf6a44fdcb5a9f2039de92b6c24a/dolls.jpg](https://challenge-files.picoctf.net/c_wily_courier/0f5ef9c383aa83d319ccb01805f4b9499934bf6a44fdcb5a9f2039de92b6c24a/dolls.jpg)

binwalk -Me dolls.jpg

grep -r "picoCTF{" .

'picoCTF{LL9lb1dR4QbGe4l4iWCvGq9pdtwt7392}'

# Notas adicionales:

- El reto utiliza la técnica de esteganografía mediante la concatenación de archivos, ocultando un archivo comprimido ZIP al final de los datos de una imagen JPG.
    
- Haciendo honor a su nombre, la estructura es recursiva: la primera imagen contiene un ZIP oculto que al extraerse revela una segunda imagen más pequeña, la cual contiene otro ZIP, y así sucesivamente en cuatro capas de profundidad.
    
- Se utilizó la herramienta `binwalk` con los parámetros `-M` (para extracción recursiva/Matryoshka) y `-e` (para extracción automática). Esto permite que la herramienta analice el archivo, extraiga los datos ocultos y vuelva a analizar automáticamente los nuevos archivos resultantes hasta agotar todas las capas.
    
- Finalmente, se empleó `grep -r` (búsqueda recursiva) para escanear todo el árbol de directorios generado y localizar rápidamente la cadena de texto de la bandera.
    

# Referencias:

[https://linux.die.net/man/1/binwalk](https://www.google.com/search?q=https://linux.die.net/man/1/binwalk) [https://linux.die.net/man/1/grep](https://linux.die.net/man/1/grep)