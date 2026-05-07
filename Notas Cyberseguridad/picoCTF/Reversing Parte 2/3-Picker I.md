# Picker I

# Descripción del reto:
This service can provide you with a random number, but can it do anything else? Connect to the program with netcat: `nc saturn.picoctf.net 59885`. The program's source code can be downloaded `here`.

# Solución:
El reto nos presenta un servicio de red programado en Python que permite al usuario interactuar con diferentes funciones predefinidas. Se nos proporciona el código fuente para realizar un análisis de caja blanca (White-box testing).

### Vulnerabilidad: Code Injection via `eval()` y Hex Output
Al analizar el código fuente, se descubre que la entrada del usuario se procesa de manera insegura utilizando la función nativa `eval()`. 

python
user_input = input("Try entering one of our functions: ")
eval(user_input + '()')`eval()` interpreta cadenas de texto como sentencias de código Python ejecutables. Dado que el código también contiene una función oculta llamada `win()` que lee el contenido del archivo `flag.txt`, el atacante puede realizar un secuestro del flujo de ejecución introduciendo el nombre de esa función exacta. Adicionalmente, la función `win()` devuelve la salida ofuscada en formato Hexadecimal en lugar de texto plano.

### Proceso de explotación:

1. Se analizó el código fuente `picker-I.py` identificando la vulnerabilidad en `eval()` y la función objetivo `win()`.
    
2. Se desarrolló un script de explotación utilizando sockets en Python para automatizar la conexión TCP.
    
3. Se interceptó el prompt del servidor y se inyectó la cadena `win` como carga útil (payload).
    
4. El servidor evaluó y ejecutó `win()`, pero devolvió la bandera fragmentada en valores hexadecimales (`0x70 0x69 0x63 0x6f...`).
    
5. Se modificó el script de ataque para interceptar la respuesta, extraer los valores mediante Expresiones Regulares, y decodificarlos de Hexadecimal a caracteres ASCII.
    

**Bandera final:** `picoCTF{4_d14m0nd_1n_7h3_r0ugh_b523b2a1}`

# Notas adicionales:

- El uso de `eval()` o `exec()` con entradas controladas por el usuario es una de las vulnerabilidades más críticas y documentadas en aplicaciones Python (CWE-94: Improper Control of Generation of Code).
    
- La ofuscación de la salida (convertir a Hex) no mitiga la ejecución remota de código (RCE). El servidor ya fue comprometido desde el momento en que aceptó la inyección.
    

# Referencias:

- [Python `eval()` function documentation](https://docs.python.org/3/library/functions.html#eval)
    
- [CWE-94: Improper Control of Generation of Code ('Code Injection')](https://cwe.mitre.org/data/definitions/94.html)