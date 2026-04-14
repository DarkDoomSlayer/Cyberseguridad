# caesar

# Descripción del reto:

Decrypt this message.

# Solución:

Se creó un entorno de trabajo y se descargó el archivo cifrado proporcionado por la plataforma:

Bash

```
mkdir reto_caesar && cd reto_caesar
wget https://challenge-files.picoctf.net/c_fickle_tempest/416ba12d66a8544f2d97e21fb165aa02f99c01ea26c5cec454a98c24c2e538d0/data.enc -O mensaje.txt
```

Al inspeccionar el archivo, se encontró una cadena cifrada dentro del formato estándar de la plataforma. Debido a que el cifrado César tiene un espacio de claves limitado (26 posibles desplazamientos), se ejecutó un script de fuerza bruta en Python para probar todas las rotaciones posibles del alfabeto.

**Resultado de la terminal:** La herramienta de fuerza bruta identificó que con una rotación de 10 posiciones, el texto se volvía legible: `¡AQUÍ ESTÁ LA BANDERA! -> picoCTF{crossingtherubiconywvaddee}`

**Bandera final:** `picoCTF{crossingtherubiconywvaddee}`

# Notas adicionales:

- **Vulnerabilidad:** El cifrado César es extremadamente débil contra ataques de fuerza bruta (brute-force) debido a que solo existen 25 claves útiles antes de que el texto vuelva a su estado original.
    
- **Referencia Histórica:** El texto plano "crossing the rubicon" hace referencia al cruce del río Rubicón por Julio César en el 49 a.C., un acto que marcó un punto de no retorno en la historia romana, lo cual es temático dado el nombre del reto.
    
- **Proceso Técnico:** El script de Python utilizó el operador de módulo `% 26` para asegurar que el desplazamiento de las letras se mantuviera dentro de los límites del abecedario (A-Z).
    

# Referencias:

- [https://en.wikipedia.org/wiki/Caesar_cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
    
- [https://picoctf.org/](https://picoctf.org/)