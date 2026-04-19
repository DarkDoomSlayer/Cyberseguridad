# interencdec

# Descripción del reto:

Can you get the real meaning from this file. Download the file here.

# Solución:

mkdir reto_interencdec && cd reto_interencdec wget [https://artifacts.picoctf.net/c_titan/3/enc_flag](https://artifacts.picoctf.net/c_titan/3/enc_flag)

El reto presenta múltiples capas de codificación y cifrado (matrioska criptográfica). Analizando la estructura, se determinó que el archivo contenía una cadena en Base64, la cual, al decodificarse, revelaba un formato de _byte-string_ de Python (`b'...'`) que contenía otra cadena en Base64.

Al decodificar esta segunda capa, se obtuvo una cadena con la estructura de la bandera (`wpjvJAM{...}`), pero cifrada mediante sustitución (César). Sabiendo que `wpjvJAM` corresponde a `picoCTF`, se calculó un desplazamiento de -7 posiciones (o +19).

Todo el proceso se automatizó en Linux mediante un encadenamiento de comandos (`pipes`):

Bash

```
cat enc_flag | base64 -d | awk -F "'" '{print $2}' | base64 -d | tr 'a-zA-Z' 't-za-sT-ZA-S'
```

Bandera final: 'picoCTF{caesar_d3cr9pt3d_b204ad6}'

# Notas adicionales:

- El reto demuestra la diferencia fundamental entre **Codificación** (Encoding) y **Cifrado** (Encryption). Base64 es un esquema de codificación (sin llave secreta) para representar datos binarios en texto, mientras que César es un método de cifrado histórico.
    
- La automatización en Bash con `awk`, `base64` y `tr` permite resolver cadenas de ofuscación complejas sin intervención manual, una habilidad esencial en entornos de operaciones de ciberseguridad.
    

# Referencias:

- [https://en.wikipedia.org/wiki/Base64](https://en.wikipedia.org/wiki/Base64)
    
- [https://en.wikipedia.org/wiki/Caesar_cipher](https://en.wikipedia.org/wiki/Caesar_cipher)