# asm2

# Descripción del reto:
What does asm2(0xa,0x15) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format.

# Solución:
Este reto aumenta la dificultad al introducir estructuras iterativas (bucles) dentro del código en Ensamblador x86. El objetivo es identificar la inicialización de variables, la condición de ruptura del bucle y las operaciones internas, para luego replicar la lógica computacional y obtener el valor final del acumulador.

### Concepto: Bucles (Loops) en x86
En ensamblador, los bucles `while` o `for` de alto nivel no existen como instrucciones únicas. Se construyen utilizando una combinación de:
1. Una evaluación lógica (`cmp`).
2. Un salto condicional al inicio del bloque de código (`jle`, `jg`, `jne`, etc.) si la condición se sigue cumpliendo.
3. Un salto incondicional (`jmp`) que fuerza al programa a volver a evaluar la condición.

### Proceso de explotación (Análisis Dinámico Mental):
Se modeló el comportamiento del binario estructurándolo en un script equivalente en Python para evitar el cálculo manual de cientos de iteraciones:
1. **Paso de parámetros:** La convención dicta que los argumentos están en `[ebp+0x8]` (`0xa`) y `[ebp+0xc]` (`0x15`).
2. **Inicialización:** El programa asigna estos argumentos a variables locales en la pila: `var1 = 0x15` (`[ebp-0x4]`) y `var2 = 0xa` (`[ebp-0x8]`).
3. **Estructura iterativa:** * Se evalúa `cmp var2, 0x84ab`.
   * Si es menor o igual (`jle`), entra al bloque matemático donde `var1 += 1` y `var2 += 0x37`.
4. **Cálculo:** El bucle itera hasta que `var2` supera `0x84ab` (33,963 en decimal). Matemáticamente, esto toma 618 iteraciones.
5. **Retorno:** El valor final de `var1` es transferido al registro `eax` para ser retornado. $21 (\text{inicial}) + 618 (\text{iteraciones}) = 639$. El número 639 en base 16 corresponde a `0x27f`.

**Bandera final:**
`0x27f`

# Notas adicionales:
* Traducir ensamblador a pseudocódigo o a lenguajes como Python o C es la técnica estándar para realizar ingeniería inversa en algoritmos matemáticos, ofuscadores o rutinas de descifrado dentro de malware.

# Referencias:
* [x86 Assembly/Loops](https://en.wikibooks.org/wiki/X86_Assembly/Control_Flow#Loops)