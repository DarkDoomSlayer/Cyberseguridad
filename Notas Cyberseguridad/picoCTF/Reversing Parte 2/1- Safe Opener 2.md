# Safe Opener 2

# Descripción del reto:
What can you do with this file? I forgot the key to my safe but this file is supposed to help me with retrieving the lost key. Can you help me unlock my safe? Download `SafeOpener.class`.

# Solución:
El reto nos entrega un archivo `.class`, el cual es un ejecutable de Java compilado (Java Bytecode). A diferencia del código fuente `.java`, este archivo está diseñado para ser interpretado por la Java Virtual Machine (JVM) y no es fácilmente legible por humanos.

### Vulnerabilidad: Análisis Estático de Binarios (Strings)
Una idea errónea común es creer que compilar un código protege las cadenas de texto estáticas (contraseñas, llaves API, banderas) que estaban en el código fuente. En Java, todas las cadenas hardcodeadas se almacenan en texto plano dentro de una estructura del archivo `.class` conocida como la *Constant Pool*. Estas cadenas pueden ser extraídas utilizando herramientas básicas de análisis estático, sin necesidad de ejecutar o descompilar el archivo.

### Proceso de explotación:
Existen dos formas principales de resolver esto:
1. **Método CLI (Rápido):** Utilizar la herramienta nativa de sistemas Unix `strings` para extraer todos los caracteres legibles del binario y filtrarlos:
   `strings SafeOpener.class | grep picoCTF`
2. **Método Scripting (Python):** Se desarrolló un script para automatizar la descarga y extracción:
   * Se descargó el archivo en modo binario.
   * Se aplicó una expresión regular de bytes (`rb'picoCTF\{.*?\}'`) para buscar la firma estándar de la bandera dentro del volcado de memoria en crudo.
   * Se decodificaron los bytes coincidentes a formato UTF-8.

**Bandera final:**
picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_de45efd6}

# Notas adicionales:
* Para auditorías más profundas donde la contraseña no está en texto plano, archivos `.class` se pueden descompilar casi a la perfección a su código fuente original usando herramientas como `JD-GUI`, `JADX` o `CFR`.
* Compilar no es ofuscar. Si necesitas almacenar un secreto en una aplicación, este nunca debe ir embebido en el código, compilado o no.

# Referencias:
* [Java class file (Wikipedia)](https://en.wikipedia.org/wiki/Java_class_file)
* [Linux `strings` command](https://man7.org/linux/man-pages/man1/strings.1.html)