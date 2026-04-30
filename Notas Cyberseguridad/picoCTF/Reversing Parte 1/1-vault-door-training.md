# vault-door-training

# Descripción del reto:
Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. The source code for the training vault is here: `VaultDoorTraining.java`

# Solución:
Este reto sirve como introducción a la categoría de Ingeniería Inversa. Se nos proporciona el código fuente de un programa en Java que simula el mecanismo de bloqueo de una puerta blindada. El objetivo es analizar la lógica de validación para extraer la contraseña correcta.

### Vulnerabilidad: Credenciales Hardcodeadas (Hardcoded Credentials)
El error más fundamental en la seguridad de aplicaciones es almacenar contraseñas, llaves API o tokens de acceso directamente en el código fuente en texto plano. Cualquier persona con acceso al código (o que logre descompilar el archivo `.class` a `.java`) puede leer la información sensible con una simple inspección visual.

### Proceso de explotación:
1. Se descargó el archivo fuente `VaultDoorTraining.java`.
2. Se analizó la estructura de la clase principal, enfocándose en el método `checkPassword(String password)`.
3. Se observó que el método retorna una comparación booleana utilizando `password.equals("w4rm1ng_Up_w1tH_jAv4_3808d338b46")`.
4. Al no existir ningún mecanismo de ofuscación o cifrado, la contraseña se extrajo directamente.
5. El código en la función `main` indicaba que la entrada del usuario se le recortaba la subcadena "picoCTF{" al inicio y "}" al final, lo que confirmaba que la cadena descubierta era el interior de la bandera.

**Bandera final:**
picoCTF{w4rm1ng_Up_w1tH_jAv4_000iPnsaWOY}


# Notas adicionales:
* Jamás se debe confiar en la ofuscación del cliente. La validación de contraseñas reales debe ocurrir del lado del servidor utilizando comparaciones de Hashes con Salting, no comparaciones de cadenas estáticas en el cliente.
* Herramientas básicas de línea de comandos como `cat file.java | grep "equals"` son suficientes para auditorías rápidas de este nivel.