# Flags

# Descripción del reto:

What do the flags mean?

# Solución:

El reto proporciona un archivo de imagen (`flag.png`) que contiene una secuencia de banderas coloridas de diferentes diseños (cuadros, rayas, cruces, etc.) separadas por unas llaves. La pregunta "¿Qué significan las banderas?" es una pista directa.

### Vulnerabilidad: Codificación de Sustitución Visual

El cifrado utilizado no es un algoritmo criptográfico computacional, sino un sistema de comunicación visual estandarizado: el **Código Internacional de Señales Marítimas**. En este sistema, cada diseño de bandera corresponde a una letra del alfabeto inglés o a un dígito numérico. Al tratarse de un estándar público, decodificar el mensaje es un proceso trivial de sustitución 1 a 1 (mapping) utilizando cualquier tabla de referencia disponible en línea.

### Proceso de explotación:

1. **Identificación:** Se identificó visualmente el sistema de símbolos como banderas de señales marítimas.
    
2. **Decodificación:** Se contrastó cada bandera de la imagen con una tabla estándar del Código Internacional de Señales.
    
3. **Traducción:**
    
    - Las banderas iniciales se tradujeron a `P I C O C T F`.
        
    - Se identificaron los caracteres de formato de la bandera `{ }`.
        
    - Las banderas interiores se tradujeron como `F 1 A G 5 A N D 5 T U F F`.
        
4. **Ensamblado:** Se construyó la cadena final respetando el formato estándar (las letras suelen interpretarse en minúsculas para los hashes internos de las banderas, salvo excepciones).
    

**Bandera final:** `picoCTF{f1ag5and5tuff}`

# Notas adicionales:

- Este tipo de retos pertenecen a la categoría de "Criptografía Clásica" o "Sustitución de Símbolos".
    
- Es común encontrar en CTFs otros alfabetos visuales como Pigpen (cifrado masónico), código Braille, alfabeto semáforo, o incluso lenguajes ficticios populares (como el Alfabeto Galáctico Estándar de Commander Keen / Minecraft).
    

# Referencias:

- [International maritime signal flags](https://en.wikipedia.org/wiki/International_maritime_signal_flags)