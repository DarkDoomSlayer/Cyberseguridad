# timer

# Descripción del reto:
You will find the flag after analysing this apk.
Download `here`.

# Solución:
El reto nos proporciona un archivo de aplicación de Android (`timer.apk`). El objetivo es realizar ingeniería inversa básica para extraer información sensible incrustada en la aplicación.

### Vulnerabilidad: Secretos Hardcodeados en Binarios DEX
Un archivo APK no es más que un archivo comprimido en formato ZIP que contiene los recursos y el código compilado de la aplicación. El código fuente de Java/Kotlin se compila en archivos `.dex` (Dalvik Executable). Al igual que los archivos `.class` estándar de Java, los archivos `.dex` mantienen las constantes de cadena (strings) en texto plano. Si un desarrollador incrusta llaves API, tokens o contraseñas en el código, estos quedarán expuestos a cualquiera que analice el APK.

### Proceso de explotación:
Se desarrolló un script en Python para automatizar el análisis estático sin depender de herramientas pesadas de decompilación (como `apktool` o `jadx`):
1. Se descargó el archivo `timer.apk`.
2. Utilizando la librería `zipfile`, se montó el archivo en memoria tratándolo como un archivo ZIP.
3. Se iteró secuencialmente por todos los archivos internos (como `classes.dex`, `resources.arsc`, `AndroidManifest.xml`).
4. Se leyó el contenido binario de cada archivo y se le aplicó una expresión regular (`rb'picoCTF\{.*?\}'`) para buscar la estructura de la bandera.
5. El patrón fue localizado con éxito dentro del ejecutable Dalvik (`classes.dex`), demostrando que la bandera fue hardcodeada en el código fuente de la aplicación.

**Bandera final:**
picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}

# Notas adicionales:
* Herramientas de terminal como `unzip -p timer.apk | strings | grep picoCTF` pueden lograr el mismo resultado en segundos.
* En escenarios de Pentesting Móvil real, se recomienda utilizar el framework `JADX` (JADX-GUI) para revertir los archivos `.dex` a código fuente `.java` altamente legible, lo que permite entender la lógica completa de la aplicación, no solo pescar cadenas estáticas.

# Referencias:
* [Android Package (APK) - Wikipedia](https://en.wikipedia.org/wiki/Apk_(file_format))
* [JADX - Dex to Java decompiler](https://github.com/skylot/jadx)