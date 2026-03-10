# What Lies Within
# Descripción del reto:
There's something in the building. Can you retrieve the flag?

# Solución:
wget https://challenge-files.picoctf.net/c_fickle_tempest/c0eec6af0f04316e2bdc4a9f095afd0e2d0121f5e543dbc4a65bb0038d72a993/buildings.png

* Se procedió a abrir el archivo buildings.png con el visor de imágenes para realizar una inspección visual. No se detectaron anomalías, ruidos o distorsiones evidentes en los píxeles.
* Se determinó que la información podría estar oculta mediante esteganografía LSB (Least Significant Bit).

zsteg -a buildings.png | grep pico
b1,rgb,lsb,xy       .. text: "picoCTF{h1d1ng_1n_th3_b1t5}"

'picoCTF{h1d1ng_1n_th3_b1t5}'

# Notas adicionales:
* La esteganografía LSB altera el bit menos significativo de los componentes de color (R, G, B) de cada píxel para codificar datos.
* Estos cambios son tan sutiles que la imagen parece idéntica al original a simple vista.
* Herramientas como 'zsteg' son fundamentales en análisis forense para detectar patrones en estos bits y extraer cadenas de texto ocultas.

# Referencias:
https://youtu.be/bFUB-USG3sw