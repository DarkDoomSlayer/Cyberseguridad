# m00nwalk

# Descripción del reto:

Decode this message from the moon.

# Solución:

wget [https://challenge-files.picoctf.net/c_fickle_tempest/67884a117da864fd93ca3cfc5d8b4d1aae71c84d7f3d2a89c1b5d0b3a19e0a71/message.wav](https://challenge-files.picoctf.net/c_fickle_tempest/67884a117da864fd93ca3cfc5d8b4d1aae71c84d7f3d2a89c1b5d0b3a19e0a71/message.wav)

git clone [https://github.com/colaclanth/sstv.git](https://github.com/colaclanth/sstv.git)

cd sstv

sudo python3 setup.py install

cd ..

sstv -d message.wav -o flag.png

xdg-open flag.png

'picoCTF{beep_boop_im_in_space}'

# Notas adicionales:

- El archivo de audio `message.wav` no es ruido estático al azar, sino una transmisión de **SSTV (Slow-Scan Television)**.
    
- SSTV es el método de transmisión analógica que utilizó la misión espacial Apolo 11 para enviar imágenes desde la Luna a la Tierra (de ahí la pista en el nombre del reto "m00nwalk" y "message from the moon").
    
- Mediante el uso de un script decodificador de SSTV en Python, es posible interpretar las frecuencias de sonido y reconstruirlas en su formato gráfico original, revelando una imagen con la bandera escrita en ella.
    

# Referencias:

[https://github.com/colaclanth/sstv](https://github.com/colaclanth/sstv)