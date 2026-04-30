# vault-door-3

# Descripción del reto:
This vault uses for-loops and byte arrays.
The source code for this vault is here: `VaultDoor3.java`

# Solución:
En este nivel de Ingeniería Inversa, el mecanismo de validación de la bóveda utiliza múltiples bucles `for` para mezclar las posiciones de los caracteres de la contraseña introducida por el usuario, almacenándolos en un búfer temporal que finalmente se compara con una cadena codificada (hardcoded).

### Vulnerabilidad: Ofuscación Reversible en el Cliente
La seguridad del sistema se basa en la "Seguridad por Oscuridad" (Security through Obscurity). Como la lógica de mezcla y la cadena de comparación final se encuentran íntegramente del lado del cliente (en el código Java), el algoritmo completo queda expuesto. Dado que las operaciones de asignación de índices son matemáticas y deterministas, el proceso puede revertirse invirtiendo las asignaciones en un script externo.

### Proceso de explotación:
Se desarrolló un script en Python para automatizar el ataque de reensamblaje:
1. Se descargó el archivo y se extrajo la cadena objetivo mediante expresiones regulares (`s.equals("...")`).
2. Se analizó la lógica de los bucles en Java. Si el programa original hacía `buffer[i] = password[f(i)]`, el script de reversión simplemente asignaba `password[f(i)] = buffer[i]`.
3. Se inicializó un arreglo vacío de 32 posiciones.
4. Se programaron los 4 bucles iterativos en Python siguiendo exactamente los mismos saltos y límites que el código Java, pero asignando las letras de la cadena objetivo en sus posiciones originales del arreglo vacío.
5. Se unió el arreglo y se le dio el formato de la bandera.

**Bandera final:**
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c2b680}

# Notas adicionales:
* Este reto demuestra un concepto clave en Reversing: no es necesario descifrar todo mentalmente. Si tienes el algoritmo de cifrado, puedes reutilizar sus propias estructuras de control (como los bucles) para programar una función de descifrado.