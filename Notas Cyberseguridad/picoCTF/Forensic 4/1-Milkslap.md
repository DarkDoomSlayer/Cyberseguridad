# Milkslap

# Descripción del reto:

 [http://wily-courier.picoctf.net:64653/](https://www.google.com/search?q=http://wily-courier.picoctf.net:64653/)

# Solución:

wget [http://wily-courier.picoctf.net:64653/concat_v.png](http://wily-courier.picoctf.net:64653/concat_v.png)

RUBY_THREAD_VM_STACK_SIZE=50000000 zsteg concat_v.png

'picoCTF{imag3_m4n1pul4t10n_sl4p5}'

# Notas adicionales:

- El reto consiste en inspeccionar una página web y sus hojas de estilo (`style.css`), donde se descubre que la animación utiliza un _sprite sheet_ gigante llamado `concat_v.png` como imagen de fondo.
    
- Se emplea la herramienta forense `zsteg` para buscar archivos o texto ocultos mediante esteganografía dentro de la imagen descargada.
    
- Debido a las dimensiones inusuales de la imagen, la ejecución normal de `zsteg` provoca un desbordamiento de pila (_stack level too deep_). Esto se soluciona asignando más memoria a la máquina virtual de Ruby mediante la variable de entorno `RUBY_THREAD_VM_STACK_SIZE=50000000` antes de ejecutar el comando.
    
- La bandera se extrae decodificando el bit menos significativo (LSB) exclusivamente en el canal de color azul de los píxeles (indicado por el resultado `b1,b,lsb,xy`).
    

# Referencias:

[https://github.com/zed-0xff/zsteg](https://github.com/zed-0xff/zsteg) [https://linux.die.net/man/1/wget](https://linux.die.net/man/1/wget)