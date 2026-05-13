# asm1

# Descripción del reto:
What does asm1(0x2ff) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format.

# Solución:
Este reto de Ingeniería Inversa nos introduce al análisis estático de código en Ensamblador x86. El objetivo es rastrear manualmente el flujo de control de una función dada una entrada específica, evaluando condiciones y operaciones aritméticas en los registros.

### Concepto: Flujo de Control en Ensamblador (x86)
En la convención de llamadas de x86 de 32 bits, el primer argumento de una función se empuja a la pila y se accede a él a través del desplazamiento `[ebp+0x8]`. El valor de retorno de cualquier función siempre se almacena en el acumulador principal, el registro `eax`, justo antes de ejecutar la instrucción `ret`.

### Proceso de explotación (Static Analysis):
Se realizó un "dry-run" (rastreo manual) del código `test.S` inyectando el valor `0x2ff` en la dirección de la variable de entrada:
1. **Validación 1:** El programa compara `0x2ff` con `0x753` (`cmp`). La instrucción siguiente es `jg` (Jump if Greater). Como `0x2ff` no es mayor, la ejecución continúa linealmente.
2. **Validación 2:** El programa compara `0x2ff` con `0x5af`. La instrucción siguiente es `jne` (Jump if Not Equal). Como son diferentes, la condición se cumple y la ejecución salta a la etiqueta `<asm1+33>`.
3. **Operación Aritmética:** * `mov eax, DWORD PTR [ebp+0x8]`: Se copia nuestro argumento (`0x2ff`) al registro de retorno `eax`.
   * `sub eax, 0x7`: Se le resta `0x7` al registro `eax`. Operación resultante: `0x2ff - 0x7 = 0x2f8`.
4. **Retorno:** El código salta al epílogo de la función (`pop ebp`, `ret`), devolviendo el valor almacenado en `eax`.

**Bandera final:**
`0x2f8`

# Notas adicionales:
* Entender las instrucciones de salto condicional (branching) como `jg` (mayor), `jl` (menor), `je` (igual) y `jne` (no igual) es fundamental para leer ensamblador, ya que representan la forma a bajo nivel de las estructuras `if/else` y `for/while` de lenguajes como C.

# Referencias:
* [x86 Assembly/Control Flow](https://en.wikibooks.org/wiki/X86_Assembly/Control_Flow)