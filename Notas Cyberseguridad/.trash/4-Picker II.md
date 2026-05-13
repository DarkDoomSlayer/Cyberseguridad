# Picker II

# Descripción del reto:
Can you figure out how this program works to get the flag?
Connect to the program with netcat: `nc saturn.picoctf.net 64187`
The program's source code can be downloaded `here`.

# Solución:
Este reto es la continuación directa de Picker I. El desarrollador intentó mitigar la vulnerabilidad de Inyección de Código implementando un filtro que bloquea específicamente la ejecución de la función `win()`.

### Vulnerabilidad: Blacklisting ineficaz sobre `eval()`
El desarrollador confió en un enfoque de "Lista Negra" (Blacklisting), prohibiendo únicamente la subcadena `'win'`. Sin embargo, la función altamente peligrosa `eval()` se mantuvo en el código.
Dado que `eval()` permite la ejecución arbitraria de comandos Python en el contexto del servidor, no es necesario utilizar las funciones predefinidas del script. Un atacante puede introducir código Python puro para interactuar directamente con el sistema de archivos del sistema operativo host (OS Command Injection / LFI a través de Python).

### Proceso de explotación:
1. Se analizó el nuevo filtro en el código fuente, confirmando que la palabra `win` estaba bloqueada.
2. Se aprovechó la sintaxis del programa: `eval(user_input + '()')`.
3. Se construyó una carga útil (payload) utilizando funciones nativas de Python: `print(open('flag.txt').read)`.
4. Al inyectarse, el servidor evaluó la sentencia `print(open('flag.txt').read)()`. 
5. La función `read()` devolvió el contenido de la bandera, `print()` lo envió por el socket TCP hacia nuestro cliente, y finalmente el programa lanzó una excepción `TypeError` (al intentar llamar a `None()`), lo cual no impidió la exfiltración de los datos.

**Bandera final:**
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}

# Notas adicionales:
* El *Blacklisting* rara vez es una solución definitiva en ciberseguridad, ya que los atacantes siempre encontrarán vectores alternativos (en este caso, llamadas nativas del sistema).
* La mitigación correcta para este sistema sería abandonar `eval()` por completo y usar una tabla de enrutamiento (ej. un diccionario que mapee el input del usuario a punteros de funciones seguras) o Whitelisting estricto.

# Referencias:
* [OWASP: Improper Input Validation](https://owasp.org/www-community/vulnerabilities/Improper_Input_Validation)