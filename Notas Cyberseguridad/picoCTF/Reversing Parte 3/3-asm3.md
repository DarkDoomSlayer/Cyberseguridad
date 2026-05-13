# asm3

# Descripción del reto:
What does asm3(0xb58568e8,0xc63ab2a1,0xf9d33ef4) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format.

# Solución:
Este es el desafío final y más complejo de la serie de análisis estático de ensamblador x86 en picoCTF. A diferencia de los retos anteriores que evaluaban saltos lógicos y bucles, `asm3` evalúa el conocimiento profundo sobre la manipulación a nivel de bytes, la arquitectura Little-Endian y la estructura de los sub-registros de la CPU.

### Concepto 1: Little-Endian
En la arquitectura x86, los datos en memoria se almacenan en formato "Little-Endian", lo que significa que el byte menos significativo se guarda en la dirección de memoria más baja. Por ejemplo, el primer argumento `0xb58568e8` se almacena en memoria secuencialmente como `e8 68 85 b5`. Extraer un solo byte en un offset específico requiere conocer esta inversión.

### Concepto 2: Sub-registros x86
El código manipula fracciones del registro acumulador de 32 bits (`EAX`):
* `AX`: Los 16 bits inferiores de `EAX`.
* `AH`: Los 8 bits altos de `AX` (High).
* `AL`: Los 8 bits bajos de `AX` (Low).

### Proceso de explotación (Rastreo Mental y Aritmética Binaria):
1. **Mapeo de Memoria:**
   * `[ebp+0x8]` a `[ebp+0xb]`: `e8 68 85 b5`
   * `[ebp+0xc]` a `[ebp+0xf]`: `a1 b2 3a c6`
   * `[ebp+0x10]` a `[ebp+0x13]`: `f4 3e d3 f9`
2. **Ejecución de Instrucciones:**
   * `xor eax, eax`: Pone el registro en `0x00000000`.
   * `mov ah, BYTE PTR [ebp+0xb]`: Mueve el byte `0xb5` a `ah`. (`eax = 0x0000b500`)
   * `shl ax, 0x10`: Desplaza `ax` a la izquierda 16 bits. Al ser `ax` un registro de 16 bits, la operación empuja todos los datos fuera del límite, vaciando el registro a `0x0000`. (`eax = 0x00000000`)
   * `sub al, BYTE PTR [ebp+0xd]`: Resta el byte `0xb2` a `al` (0). `0x00 - 0xb2 = 0x4e` por underflow. (`eax = 0x0000004e`)
   * `add ah, BYTE PTR [ebp+0xc]`: Suma el byte `0xa1` a `ah`. (`eax = 0x0000a14e`)
   * `xor ax, WORD PTR [ebp+0x10]`: Extrae un *Word* (16 bits) a partir del offset `0x10` (`f4 3e` en Little-Endian = `0x3ef4`). Realiza un XOR bit a bit: `0xa14e ^ 0x3ef4 = 0x9fba`.
3. **Retorno:** El valor final almacenado en el registro de retorno `eax` es `0x00009fba`.

**Bandera final:**
`0x9fba`

# Notas adicionales:
* El uso de `shl ax, 0x10` es un truco de ofuscación clásico utilizado por compiladores (o creadores de malware) para limpiar un registro de 16 bits en lugar de utilizar operaciones más evidentes como `xor ax, ax` o `mov ax, 0`.

# Referencias:
* [Endianness (Wikipedia)](https://en.wikipedia.org/wiki/Endianness)
* [x86 Registers](https://en.wikibooks.org/wiki/X86_Assembly/X86_Architecture#General-Purpose_Registers_(GPR)_-_16-bit_naming_conventions)