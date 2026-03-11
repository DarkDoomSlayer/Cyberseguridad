# c0rrupt (mystery)

# Descripción del reto:

We found this file. Recover the flag.

# Solución:

wget [https://challenge-files.picoctf.net/c_fickle_tempest/87bdc8ce30b177d033b3d68bca4647950bb07304032861baa912ebe08701d355/mystery](https://challenge-files.picoctf.net/c_fickle_tempest/87bdc8ce30b177d033b3d68bca4647950bb07304032861baa912ebe08701d355/mystery)

file mystery

binwalk mystery

cat << 'EOF' > solve.py with open("mystery", "rb") as f: data = bytearray(f.read())

# 1. Reparar la firma PNG (Magic Bytes)

data[0:8] = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'

# 2. Reparar el bloque principal IHDR

data[12:16] = b'IHDR'

# 3. Reparar el valor del eje X en el bloque pHYs

data[70] = 0x00

# 4. Reparar la longitud del primer bloque de datos IDAT

data[83:85] = b'\x00\x00'

# 5. Reparar el nombre del bloque IDAT

data[87:91] = b'IDAT'

with open("flag.png", "wb") as f: f.write(data)

print("[+] Archivo 'mystery' reparado a nivel hexadecimal. Guardado como flag.png") EOF

python3 solve.py

xdg-open flag.png

'picoCTF{c0rrupt10n_1847995}'

# Notas adicionales:

- El comando `file` no pudo identificar el tipo de archivo inicial porque sus "Magic Bytes" (la firma hexadecimal inicial que identifica el formato ante el sistema operativo) estaban destruidos.
    
- La herramienta `binwalk` detectó datos comprimidos con Zlib en el offset 91, lo cual es la firma característica de los bloques de imagen de un archivo PNG.
    
- La estructura de un archivo PNG estándar está compuesta por fragmentos (chunks) secuenciales esenciales como `IHDR` (cabecera principal), `pHYs` (tamaño físico de los píxeles) e `IDAT` (los datos comprimidos de la imagen propiamente).
    
- El reto consistió en realizar una reparación a nivel binario (hex editing) mediante un script en Python para restaurar la firma global y los identificadores de los bloques que fueron sobrescritos intencionalmente. Una vez restaurada la integridad estructural, los visores de imágenes estándar pueden renderizar el contenido oculto.
    

# Referencias:

[https://en.wikipedia.org/wiki/Portable_Network_Graphics#File_header](https://www.google.com/search?q=https://en.wikipedia.org/wiki/Portable_Network_Graphics%23File_header) [https://linux.die.net/man/1/binwalk](https://www.google.com/search?q=https://linux.die.net/man/1/binwalk)