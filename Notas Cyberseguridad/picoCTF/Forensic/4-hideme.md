# hideme

# Descripción del reto:

Every file gets a flag. The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye here.

# Solución:

mkdir reto_hideme && cd reto_hideme

wget [https://artifacts.picoctf.net/c/262/flag.png](https://artifacts.picoctf.net/c/262/flag.png)

binwalk -e flag.png

unzip ./_flag.png.extracted/9B3B.zip -d ./_flag.png.extracted/

xdg-open ./_flag.png.extracted/secret/flag.png

'picoCTF{Hiddinng_An_imag3_within_@n_ima9e_82101824}'

# Notas adicionales:

- El reto demuestra una técnica clásica de ofuscación donde se adjunta un archivo comprimido (ZIP) al final de la estructura de datos de una imagen (PNG).
    
- A simple vista y para la mayoría de los visores convencionales, el archivo original parece un PNG normal porque el renderizado se detiene al encontrar el bloque de fin de archivo de imagen.
    
- Se utilizó la herramienta forense `binwalk`, la cual escanea los archivos en busca de firmas hexadecimales ("Magic Bytes") incrustadas. Al encontrar la firma de un archivo ZIP, pudo extraer la carpeta oculta.
    
- A diferencia de otros retos donde la información exfiltrada está en texto plano, aquí la bandera es puramente visual, obligando al analista a descomprimir y renderizar la imagen extraída para leerla.
    

# Referencias:

[https://linux.die.net/man/1/binwalk](https://linux.die.net/man/1/binwalk)