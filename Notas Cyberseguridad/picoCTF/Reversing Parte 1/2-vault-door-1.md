# vault-door-1

# Descripción del reto:
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: `VaultDoor1.java`

# Solución:
Este reto de Ingeniería Inversa nos presenta un mecanismo de validación de contraseña ligeramente más ofuscado que el nivel de entrenamiento. La contraseña sigue estando codificada en el código fuente (hardcoded), pero la validación se realiza carácter por carácter en un orden no secuencial.

### Vulnerabilidad: Validación Desordenada (Scrambled Index Validation)
El código Java utiliza múltiples comprobaciones lógicas con el método `String.charAt(index)`, comparando cada posición de la entrada del usuario contra un carácter estático. Aunque los índices están barajados para dificultar la lectura humana a simple vista, la información completa necesaria para reconstruir el texto plano reside en las propias instrucciones de validación.

### Proceso de explotación:
Se desarrolló un script en Python para extraer, ordenar y ensamblar la contraseña automáticamente:
1. Se descargó el archivo fuente `VaultDoor1.java`.
2. Se aplicó una expresión regular (`password\.charAt\((\d+)\)\s*==\s*'(.+?)'`) para iterar sobre el código y extraer en una lista de tuplas tanto el índice requerido como el carácter esperado.
3. Se convirtió el índice capturado de cadena de texto (string) a entero (int) para permitir un ordenamiento numérico correcto.
4. Se ordenó la matriz resultante de forma ascendente (del índice 0 al 31).
5. Se concatenaron secuencialmente los caracteres ordenados para revelar la contraseña subyacente.

**Bandera final:**
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_e79c38}

# Notas adicionales:
* Ofuscar el orden de las comparaciones lógicas no añade seguridad real a una aplicación. Si la lógica de validación del cliente contiene los elementos esperados, es trivial extraerlos utilizando expresiones regulares o comandos de terminal como `grep`, `awk` y `sort`.