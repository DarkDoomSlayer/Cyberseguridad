# Picker III

# Descripción del reto:
Can you figure out how this program works to get the flag?
Connect to the program with netcat: `nc saturn.picoctf.net 53172`
The program's source code can be downloaded `here`.

# Solución:
En la tercera iteración de la serie Picker, el desarrollador reemplazó la ejecución directa del usuario (`eval`) con un menú de opciones estrictas (1-4) para limitar el alcance de las llamadas a funciones.

### Vulnerabilidad: Asignación Arbitraria de Variables y Secuestro de Funciones (Variable Overwriting / Function Pointer Hijacking)
A pesar de la restricción del menú, la opción 3 mapea a la función `write_variable()`, la cual solicita al usuario el nombre y valor de una variable para procesarlos dinámicamente mediante:
`exec('global ' + var_name + '; ' + var_name + ' = ' + value)`

En Python, todo es un objeto, incluidas las funciones. Esto permite al usuario declarar el nombre de una función existente (como `getRandomNumber`, asignada a la opción 4 del menú) y modificar su valor para que apunte a la función oculta `win`. De este modo, la tabla de enrutamiento del menú es subvertida en tiempo de ejecución.

### Proceso de explotación:
1. Se analizó el código fuente y se identificó la vulnerabilidad en la lógica de `write_variable()`.
2. Se desarrolló un script en Python para interactuar con la consola mediante sockets de red.
3. Se inyectaron los siguientes comandos secuenciales:
   * **`3`**: Activa el flujo de escritura de variables.
   * **`getRandomNumber`**: Selecciona el nombre del puntero asignado a la opción 4 como el objetivo a sobrescribir.
   * **`win`**: Reemplaza el puntero por la dirección de memoria de la función objetivo.
   * **`4`**: Ejecuta la opción 4, desencadenando la función `win()`.
4. La función devolvió la bandera en formato Hexadecimal ofuscado, por lo que el script interceptó y tradujo la respuesta mediante manipulación de N-gramas (Base 16 a ASCII).

**Bandera final:**
picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_226dd285}

# Notas adicionales:
* El uso de `exec()` para gestionar el estado de variables en una aplicación es una práctica inaceptable en producción. 
* La separación lógica entre "datos" y "código" no existe en lenguajes interpretados de alto nivel sin una fuerte validación de tipos, permitiendo que funciones y variables primitivas se traten de la misma manera.

# Referencias:
* [Python `exec()` function documentation](https://docs.python.org/3/library/functions.html#exec)