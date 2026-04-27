# morse-code

# Descripción del reto:
Morse code is well known. Can you decrypt this?
Download the file `here`.
Wrap your answer with picoCTF{}, put underscores in place of pauses, and use all lowercase.

# Solución:
El reto proporciona un archivo de audio en formato `.wav` que contiene una transmisión de señales acústicas correspondientes al código Morse internacional. 

### Concepto: Codificación Acústica
El código Morse es un método de codificación de caracteres que transmite información telegráfica utilizando secuencias de marcas cortas (puntos) y largas (rayas). En los retos de tipo CTF, el análisis de estos archivos suele requerir la inspección visual de la forma de onda (waveform) o el uso de procesadores de señales digitales (DSP) para transcribir los intervalos de amplitud sonora a texto plano.

### Proceso de explotación:
1. **Análisis de Señal:** Se procesó el archivo `morse_chal.wav` extrayendo las secuencias de pulsos acústicos. Esto se puede lograr visualizando el archivo en una herramienta de edición de audio (como Audacity) o utilizando un decodificador adaptable que mide la duración de los tonos de alta frecuencia.
2. **Transcripción:** Los puntos y rayas se tradujeron a caracteres alfanuméricos según el estándar internacional, resultando en una cadena de texto plano con espacios delimitando las palabras.
3. **Formateo de Bandera:** Se desarrolló un script en Python para normalizar la salida de acuerdo con los requisitos del sistema:
   * Se aplicó la función `.lower()` para convertir todos los caracteres a minúsculas.
   * Se utilizó `.replace(" ", "_")` para sustituir las pausas acústicas (espacios) por guiones bajos.
   * Se concatenó el resultado dentro del wrapper estándar `picoCTF{...}`.

**Bandera final:**
picoCTF{wh47_h47h_90d_w20u9h7}

# Notas adicionales:
* El código Morse no es un esquema de encriptación, sino una codificación (encoding) pública, similar a Base64 o ASCII. No provee ninguna confidencialidad criptográfica, solo cambia la representación del mensaje.

# Referencias:
* [Morse code (Wikipedia)](https://en.wikipedia.org/wiki/Morse_code)
* [Audacity - Free Audio Editor](https://www.audacityteam.org/)