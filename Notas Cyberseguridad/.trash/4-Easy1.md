# Easy1

# Descripción del reto:

The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?

# Solución:

El reto proporciona un texto cifrado (`UFJKXQZQUNB`), una llave (`SOLVECRYPTO`) y un archivo `table.txt` que contiene una Tabula Recta. Estos elementos son los componentes clásicos del **Cifrado de Vigenère**.

En lugar de buscar manualmente las intersecciones en la tabla de texto, se puede automatizar el proceso de descifrado aplicando la operación matemática subyacente del cifrado de Vigenère mediante un script en Python en la terminal:

Bash

```
python3 -c '
cifrado = "UFJKXQZQUNB"
llave = "SOLVECRYPTO"
descifrado = "".join([chr((ord(c) - ord(k)) % 26 + 65) for c, k in zip(cifrado, llave)])
print(f"picoCTF{{{descifrado}}}")
'
```

El resultado de la decodificación revela el texto plano.

Bandera final: 'picoCTF{CRYPTOISFUN}'

# Notas adicionales:

- El **Cifrado de Vigenère** es un cifrado por sustitución polialfabética. A diferencia del cifrado César (donde el desplazamiento es constante), Vigenère utiliza una palabra clave para cambiar el desplazamiento letra por letra, haciéndolo resistente al análisis de frecuencias básico.
    
- El reto menciona "One time pad" (OTP). Un OTP real es inquebrantable si la llave es verdaderamente aleatoria, del mismo tamaño que el mensaje y nunca se reutiliza. En este caso, al darnos la llave explícitamente y ser una palabra con sentido (SOLVECRYPTO), se reduce a un ejercicio de Vigenère estándar.
    

# Referencias:

- [https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
    
- [https://en.wikipedia.org/wiki/Tabula_recta](https://en.wikipedia.org/wiki/Tabula_recta)