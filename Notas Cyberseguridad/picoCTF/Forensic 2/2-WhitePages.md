# WhitePages

# Descripción del reto:

I stopped using YellowPages and moved onto WhitePages... but the page they gave me is all blank!

# Solución:

wget [https://challenge-files.picoctf.net/c_fickle_tempest/ab5453de03105a8aab9c68b0b46e66a4fe0a781c3915ab519f7fab31b3ce6894/whitepages.txt](https://challenge-files.picoctf.net/c_fickle_tempest/ab5453de03105a8aab9c68b0b46e66a4fe0a781c3915ab519f7fab31b3ce6894/whitepages.txt)

cat << 'EOF' > solve.py with open("whitepages.txt", "rb") as f: data = f.read()

data = data.replace(b'\xe2\x80\x83', b'0') data = data.replace(b'\x20', b'1')

binary_string = data.decode('ascii')

flag = "" for i in range(0, len(binary_string), 8): byte = binary_string[i:i+8] if len(byte) == 8: flag += chr(int(byte, 2))

print(flag) EOF

python3 solve.py

'picoCTF{not_all_spaces_are_created_equal_bbc4f54c75763bd78dc840f05eb7a752}'

# Notas adicionales:

- Al intentar leer el archivo de forma convencional con un editor de texto o comando básico, parece estar completamente vacío.
    
- Se revela que la página contiene datos reales compuestos por una mezcla de dos caracteres invisibles diferentes: el espacio estándar (`0x20`) y un carácter Unicode más ancho conocido como "Em Space" (`0xE28083`).
    
- El reto utiliza **Whitespace Steganography** (Esteganografía de espacios en blanco), una técnica que aprovecha la invisibilidad de estos caracteres para codificar datos en binario, donde un tipo de espacio representa un `0` y el otro un `1`.
    
- Un script en Python resulta ideal para automatizar la lectura de los bytes crudos, sustituir los caracteres por su equivalente binario y convertir la cadena en bloques de 8 bits hacia el texto ASCII legible que revela la bandera.
    

# Referencias:

[https://docs.python.org/3/library/functions.html#int](https://www.google.com/search?q=https://docs.python.org/3/library/functions.html%23int)