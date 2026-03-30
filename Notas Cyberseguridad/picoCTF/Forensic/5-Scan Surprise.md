# Scan Surprise

# Descripción del reto:

I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead? You can download the challenge files here: `challenge.zip`. The same files are accessible via SSH here: `ssh -p 60391 ctf-player@atlas.picoctf.net`

# Solución:

mkdir reto_scansurprise && cd reto_scansurprise

wget [https://artifacts.picoctf.net/c_atlas/14/challenge.zip](https://artifacts.picoctf.net/c_atlas/14/challenge.zip)

unzip challenge.zip

sudo dnf install zbar -y

find . -type f -name "*.png" -exec zbarimg -q {} ; | grep "picoCTF{"

'picoCTF{p33k_@_b00_0194a007}'

# Notas adicionales:

- El reto proporciona un archivo comprimido que, al ser extraído, revela una imagen PNG con un código QR (Quick Response).
    
- En lugar de depender de herramientas gráficas o lectores de teléfonos móviles, se puede automatizar el análisis forense de códigos de barras y QR directamente desde la terminal.
    
- Se instaló la suite de herramientas `zbar` (disponible en los repositorios de Fedora) para obtener la utilidad de línea de comandos `zbarimg`.
    
- Al ejecutar el comando junto con `find`, la imagen extraída fue procesada por `zbarimg`, el cual decodificó exitosamente los bloques del QR y devolvió la cadena de texto plano oculto, capturada fácilmente con `grep`.
    

# Referencias:

[https://linux.die.net/man/1/zbarimg](https://linux.die.net/man/1/zbarimg)