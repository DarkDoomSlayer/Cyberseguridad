# vault-door-4

# Descripción del reto:
This vault uses ASCII encoding for the password.
The source code for this vault is here: `VaultDoor4.java`

# Solución:
En este nivel, la contraseña se encuentra fragmentada y almacenada en un arreglo de bytes (`byte[]`). El mecanismo de ofuscación no utiliza operaciones lógicas, sino una representación variada de tipos de datos que el compilador de Java interpreta nativamente.

### Vulnerabilidad: Codificación de Bases Numéricas (Number Base Encoding)
El código fuente oculta la bandera representando los valores ASCII de los caracteres en cuatro bases distintas:
1. **Decimal** (Base 10): Representación numérica estándar.
2. **Hexadecimal** (Base 16): Utilizando el prefijo estándar `0x`.
3. **Octal** (Base 8): En Java (y C), los números con un `0` a la izquierda (ej. `0142`) son tratados como octales.
4. **Char Literal**: Representación directa de caracteres ASCII entre comillas simples.

Dado que todos estos valores se resuelven en la tabla ASCII durante la compilación, la contraseña real está técnicamente codificada (hardcoded) en el texto.

### Proceso de explotación:
Se desarrolló un script en Python para extraer el arreglo dinámicamente y revertir la codificación:
1. Se descargó el archivo y se utilizó la expresión regular `byte\[\] myBytes = \{(.*?)\};` para extraer el contenido del bloque.
2. Se normalizó la cadena resultante y se dividió en una lista por comas.
3. Se iteró sobre la lista aplicando lógica condicional basada en prefijos léxicos:
   * Si el elemento inicia con `0x`, se utiliza `int(val, 16)`.
   * Si el elemento inicia con `0`, se utiliza `int(val, 8)`.
   * Si el elemento está envuelto en `' '`, se extrae directamente.
   * Por defecto, se asume decimal y se utiliza `int(val)`.
4. Los valores numéricos resultantes se convirtieron a caracteres utilizando la función `chr()` y se concatenaron.

**Bandera final:**
picoCTF{jU5t_4_bUnCh_0f_bYt3s_13df618a23}

# Notas adicionales:
* Este reto demuestra que cambiar la representación base de los datos no constituye una medida de cifrado real. Es una ofuscación léxica trivial que puede ser rápidamente mitigada con cualquier lenguaje de scripting moderno.