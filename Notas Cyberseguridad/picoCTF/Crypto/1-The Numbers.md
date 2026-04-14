# The Numbers

# Descripción del reto:

The numbers... what do they mean?

# Solución:

El reto proporciona una imagen con la siguiente secuencia numérica: `16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }`

Al analizar los primeros números (`16 9 3 15 3 20 6`), se observa que corresponden directamente a la palabra "picoCTF" si aplicamos un cifrado de sustitución simple donde cada número representa su posición en el alfabeto inglés (A1Z26).

- 16 = P
    
- 9 = I
    
- 3 = C
    
- 15 = O
    
- 3 = C
    
- 20 = T
    
- 6 = F
    

Aplicando la misma lógica al contenido dentro de las llaves:

- 20, 8, 5 -> THE
    
- 14, 21, 13, 2, 5, 18, 19 -> NUMBERS
    
- 13, 1, 19, 15, 14 -> MASON
    

La bandera decodificada es: 'picoCTF{THENUMBERSMASON}'

# Notas adicionales:

- Este es un ejemplo básico de criptografía de sustitución conocido como A1Z26.
    
- La frase "The numbers, Mason, what do they mean?" es una referencia a la cultura popular (videojuego Call of Duty: Black Ops), lo cual es común encontrar como easter eggs en competiciones de tipo CTF.
    

# Referencias:

[https://en.wikipedia.org/wiki/Substitution_cipher](https://en.wikipedia.org/wiki/Substitution_cipher)