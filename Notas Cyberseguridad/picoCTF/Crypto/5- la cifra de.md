# la cifra de

# Descripción del reto:

I found this cipher in an old book. Can you figure out what it says? Connect with nc fickle-tempest.picoctf.net 54340.

# Solución:

Se utilizó `nc` (netcat) en la terminal para conectar al servidor y obtener el texto cifrado. El texto hace referencia a Giovan Battista Bellaso, el verdadero inventor del cifrado comúnmente conocido como Vigenère.

Dado que no se proporcionó la clave de cifrado, se recurrió a un **Ataque de Texto Plano Conocido (KPA)**. Se identificó la estructura estándar de las banderas (`picoCTF{`) cerca del final del texto cifrado (`...pohzCZK{...`).

Al calcular la diferencia matemática entre el texto cifrado y la palabra `picoCTF`, se descubrió que la clave subyacente era la palabra `FLAG`.

Finalmente, se ejecutó un script en Python para aplicar la inversa del algoritmo de Vigenère sobre el contenido de la llave, utilizando la secuencia desplazada de la clave (`LAGF`):

Bash

```
python3 -c '
cifrado = "m311a50_0x_a1rn3x3_h1ah3x149hNchj"
llave = "LAGF"
descifrado = ""
i = 0
for c in cifrado:
    if c.isalpha():
        base = 65 if c.isupper() else 97
        descifrado += chr((ord(c) - base - (ord(llave[i%4]) - 65)) % 26 + base)
        i += 1
    else:
        descifrado += c
print(f"picoCTF{{{descifrado.lower()}}}")
'
```

Bandera final: `picoCTF{b311a50_0r_v1gn3r3_c1ph3r149cccbe}`

# Notas adicionales:

- El cifrado de Bellaso (Vigenère) fue considerado indescifrable ("le chiffre indéchiffrable") durante siglos hasta que Charles Babbage y Friedrich Kasiski desarrollaron métodos para romperlo basados en el análisis de frecuencias y la repetición de patrones.
    
- En ciberseguridad moderna, el uso de formatos predecibles (como el inicio `picoCTF{`) representa una vulnerabilidad crítica que facilita los ataques KPA, permitiendo deducir la clave criptográfica sin necesidad de romper la matemática del algoritmo.
    

# Referencias:

- [https://en.wikipedia.org/wiki/Known-plaintext_attack](https://en.wikipedia.org/wiki/Known-plaintext_attack)
    
- [https://en.wikipedia.org/wiki/Giovan_Battista_Bellaso](https://en.wikipedia.org/wiki/Giovan_Battista_Bellaso)