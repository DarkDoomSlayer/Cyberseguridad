# rsa-pop-quiz

# Descripción del reto:

Class, take your seats! It's PRIME-time for a quiz... `nc fickle-tempest.picoctf.net 50333`

# Solución:

Este reto de nivel "Hard" consiste en un cuestionario interactivo a través de una conexión TCP donde se deben resolver múltiples operaciones matemáticas fundamentales del algoritmo de cifrado asimétrico RSA. Las preguntas tienen un límite de tiempo estricto y cambian de formato de manera dinámica, por lo que es indispensable automatizar la interacción.

Se desarrolló un exploit en Python utilizando la librería `pwntools` para conectarse al socket, analizar el texto recibido (parseo) y calcular las respuestas al vuelo.

El script aplica los siguientes conceptos y fórmulas matemáticas del criptosistema RSA extraídos de la teoría:

- Cálculo del módulo: n=p∗q.
    
- Cálculo del totiente de Euler: tn=(p−1)∗(q−1).
    
- Cálculo de la llave privada (inverso modular): d=e−1(modtn).
    
- Cifrado del mensaje plano: c=me(modn).
    
- Descifrado: m=cd(modn).
    

**Manejo de Excepciones y Trampas del Servidor:**

1. **Operaciones Inviables:** En los casos donde el servidor solicita operaciones computacionalmente imposibles de resolver en tiempo polinómico (como factorizar un módulo n gigante sin conocer los primos p y q), el script responde con un `N` indicando que no es factible.
    
2. **Ofuscación de Variables:** El servidor alterna entre pedir variables de un solo carácter (`m`, `c`) y las palabras completas (`plaintext`, `ciphertext`). El script incluye un mapeo dinámico para manejar estas variaciones.
    

**Obtención de la Bandera:** En el último paso, el servidor proporciona el texto cifrado (c), junto con p, e y n. El script calcula q=n//p, obtiene el totiente, genera la llave privada d y finalmente recupera el mensaje original m. Este mensaje numérico decimal es convertido internamente a hexadecimal y finalmente decodificado a texto plano ASCII (bytes) para revelar la bandera.

+1

Bandera final: `picoCTF{wA8_th4till3aGal..ob6435DeB}`

# Notas adicionales:

- RSA basa su seguridad en la asimetría computacional: es trivial multiplicar dos números primos gigantes para obtener n, pero es prácticamente imposible hacer la operación inversa (factorizar n) si no se conoce la llave privada.
    
- Automatizar con la librería `pwntools` de Python es un estándar en la resolución de retos CTF (Capture The Flag) que requieren interacción por red.
    

# Referencias:

- [https://en.wikipedia.org/wiki/RSA_(cryptosystem)](https://en.wikipedia.org/wiki/RSA_\(cryptosystem\))
    
- [https://docs.pwntools.com/en/stable/](https://docs.pwntools.com/en/stable/)