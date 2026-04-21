# Pixelated

# Descripción del reto:
I have these 2 images, can you make a flag out of them? `scrambled1.png` `scrambled2.png`

# Solución:
El reto nos proporciona dos imágenes del mismo tamaño que aparentan ser ruido visual o estática. Estas imágenes son componentes de un esquema de esteganografía conocido como **Criptografía Visual**, donde una imagen original ha sido separada en dos capas aparentemente aleatorias.

### Vulnerabilidad: Criptografía Visual (Suma Modular)
Para revelar el secreto, las imágenes deben ser recombinadas mediante una operación aritmética o lógica píxel por píxel (usualmente XOR o suma). En este caso, el algoritmo utilizado para dividir la imagen requiere que los valores RGB de cada píxel de la primera imagen se sumen a los de la segunda imagen, aplicando un módulo de 256 (el límite máximo del valor de color en formato de 8 bits).
La fórmula aplicada por píxel es:
$$P_{resultado} \equiv (P_1 + P_2) \pmod{256}$$

### Proceso de explotación:
Se desarrolló un script en Python utilizando las librerías `Pillow` y `numpy` para automatizar la descarga y recombinación.
1. Se descargaron ambas imágenes (`scrambled1.png` y `scrambled2.png`) y se cargaron en memoria.
2. Se convirtieron las imágenes en arreglos numéricos tridimensionales utilizando `numpy.array`, con un tipo de dato `uint8` (entero sin signo de 8 bits).
3. Se realizó una suma matricial simple: `arr1 + arr2`. Al ser matrices `uint8`, el desbordamiento de enteros (integer overflow) aplicó automáticamente la operación de módulo 256 para valores que superaban el límite de color.
4. El arreglo resultante se renderizó de nuevo a un archivo de imagen (`flag_pixelated.png`), revelando el texto plano de la bandera oculta en los colores corregidos.

**Bandera final:**
`picoCTF{8cdf93c3}`

# Notas adicionales:
* La criptografía visual permite que la información visual pueda ser cifrada de tal manera que el descifrado puede realizarse sin el uso de una computadora, simplemente imprimiendo ambas capas en transparencias y superponiéndolas. Sin embargo, en formatos digitales con alteración de color como este, se requieren operaciones matemáticas por canales.
* Utilizar `numpy` acelera radicalmente el proceso al vectorizar la suma de millones de píxeles de manera casi instantánea, a diferencia de iterar con bucles `for` nativos en Python.

# Referencias:
* [Visual cryptography](https://en.wikipedia.org/wiki/Visual_cryptography)
* [Pillow (PIL Fork) Documentation](https://pillow.readthedocs.io/)
* [NumPy arrays](https://numpy.org/doc/stable/reference/generated/numpy.array.html)