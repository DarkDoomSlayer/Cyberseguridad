# Vigenere

# Descripción del reto:
Can you decrypt this message?
Decrypt this `message` using this key "CYLAB".

# Solución:
El reto nos presenta un texto cifrado utilizando el clásico **Cifrado Vigenère**, un método de sustitución polialfabética diseñado para resistir los ataques de análisis de frecuencias que rompen los cifrados monoalfabéticos.

### Concepto: Sustitución Polialfabética
A diferencia del cifrado César (donde el desplazamiento es constante para todo el documento), Vigenère utiliza una palabra clave para cambiar el desplazamiento de cada letra. La clave se repite cíclicamente sobre el texto plano. Si la clave es `CYLAB`, el desplazamiento matemático de la primera letra está dictado por 'C', el de la segunda por 'Y', y así sucesivamente. Los caracteres no alfabéticos (números, signos de puntuación) se ignoran y no consumen posiciones de la llave.

### Proceso de explotación:
Se desarrolló un script en Python para automatizar el descifrado:
1. Se recuperó el criptograma desde el servidor.
2. Se iteró sobre cada carácter del texto. Si el carácter se identificaba como una letra (`.isalpha()`), se calculaba su distancia respecto a la letra correspondiente de la clave `CYLAB` utilizando aritmética modular sobre el alfabeto inglés (26 letras).
3. Se aplicó la fórmula inversa de Vigenère: $P_i = (C_i - K_i + 26) \pmod{26}$, donde $P$ es el texto plano, $C$ es el criptograma y $K$ es la llave, manteniendo la capitalización original intacta.

**Bandera final:**
"picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_2951a89h}'

# Notas adicionales:
* El cifrado Vigenère fue considerado indescifrable (*le chiffre indéchiffrable*) durante casi tres siglos, hasta que Friedrich Kasiski publicó un método general para romperlo en 1863 encontrando la longitud de la llave mediante la repetición de patrones.

# Referencias:
* [Vigenère cipher (Wikipedia)](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)