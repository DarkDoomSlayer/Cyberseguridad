# waves over lambda

# Descripción del reto:

We made a lot of substitutions to encrypt this. Can you decrypt it? Connect with nc fickle-tempest.picoctf.net 51811.

# Solución:

El reto presenta un clásico cifrado de sustitución monoalfabética, donde el texto plano ha sido ofuscado cambiando cada letra del abecedario por otra distinta de forma fija.

En lugar de utilizar herramientas automatizadas de análisis de frecuencias, se explotó una vulnerabilidad de "texto plano conocido" (Known-Plaintext) en la cabecera del mensaje cifrado.

El servidor arrojó la siguiente línea inicial: `xtcvrgmy diri by atsr kqgv - krifsicxa_by_x_tlir_qgoujg_k3kk3g4j`

Por contexto de competencias CTF, se infirió que la primera parte correspondía a la frase estándar `congrats here is your flag`. Esto permitió mapear la sustitución de caracteres clave:

- k = f
    
- q = l
    
- g = a
    
- v = g
    
- ...etc.
    

Al aplicar este mapeo directo a la segunda parte de la cadena (`krifsicxa_by_x_tlir_qgoujg_k3kk3g4j`), se reveló el texto en claro.

Bandera final: 'picoCTF{frequency_is_c_over_lambda_f3ff3a4d}'

# Notas adicionales:

- El nombre del reto "waves over lambda" es una pista sutil, ya que en física, la frecuencia es igual a la velocidad de la onda (c) dividida por su longitud (lambda): f=c/λ. Esta es exactamente la frase que se forma en la bandera decodificada.
    
- La reutilización de frases predecibles (como saludos o encabezados) es una de las debilidades más grandes al usar cifrados de sustitución, facilitando la deducción de la llave sin esfuerzo computacional.
    

# Referencias:

- [https://en.wikipedia.org/wiki/Substitution_cipher](https://en.wikipedia.org/wiki/Substitution_cipher)
    
- [https://en.wikipedia.org/wiki/Frequency_analysis](https://en.wikipedia.org/wiki/Frequency_analysis)
    

---