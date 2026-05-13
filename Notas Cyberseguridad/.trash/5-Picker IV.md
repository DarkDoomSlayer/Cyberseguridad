 Picker IV

# Descripción del reto:
Can you figure out how this program works to get the flag? Connect to the program with netcat: `nc saturn.picoctf.net 65054`. The program's source code and the binary can be downloaded `here`.

# Solución:
Este reto sirve como introducción práctica a la categoría de **Binary Exploitation (Pwn)**. El servidor ejecuta un binario en C que solicita un valor hexadecimal al usuario para utilizarlo directamente como una dirección de salto en memoria.

### Vulnerabilidad: Unvalidated Function Pointer (Arbitrary Code Execution)
El código en C procesa la entrada del usuario y realiza un moldeo de tipo (Type Casting) directo hacia un puntero de función, para luego invocarlo:
`void (*foo)(void) = (void (*)())val;`
`foo();`
Al no existir validaciones de límites ni verificaciones de seguridad sobre la dirección ingresada, se produce un Secuestro del Flujo de Control (Control Flow Hijacking) trivial. El atacante controla el *Instruction Pointer* y puede redirigir la ejecución de la CPU hacia cualquier bloque de código mapeado en el espacio de memoria del proceso, incluyendo la función oculta `win()`.

### Proceso de explotación:
1. Se descargó el ejecutable compilado en formato `ELF` (Executable and Linkable Format).
2. Se desarrolló un script utilizando el framework **pwntools** para automatizar el análisis y el ataque.
3. El script instanció el objeto `ELF()` y parseó la tabla de símbolos (Symbol Table) para localizar estáticamente la dirección de memoria exacta de la función `win` (ej. `0x40129e`).
4. Se estableció una conexión TCP remota.
5. Se formateó la dirección de memoria en una cadena hexadecimal sin el prefijo `0x` (requerimiento sintáctico de `scanf("%x")`).
6. Se envió la carga útil, forzando al programa a saltar a la dirección inyectada e imprimir el contenido del archivo `flag.txt` en el servidor.

**Bandera final:**
picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_b8de1af4}

# Notas adicionales:
* Este reto simula la fase final de un *Buffer Overflow* tradicional (ret2win), saltándose la parte de calcular el *offset* y sobrescribir el registro de retorno, entregando la capacidad de sobrescritura directamente mediante lógica de aplicación.
* En binarios modernos, protecciones como **PIE** (Position Independent Executable) aleatorizan las direcciones de memoria de las funciones en cada ejecución, mitigando los ataques estáticos de este tipo sin una filtración de memoria previa (Memory Leak).

# Referencias:
* [Function Pointers in C](https://en.wikipedia.org/wiki/Function_pointer)
* [Pwntools ELF module](https://docs.pwntools.com/en/stable/elf/elf.html)