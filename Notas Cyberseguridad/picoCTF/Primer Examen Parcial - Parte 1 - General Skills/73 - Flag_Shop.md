# Descripción
There's a flag shop selling stuff, can you buy a flag? [Source](https://challenge-files.picoctf.net/c_fickle_tempest/00517bd6f4d62bae3c15297f6bf9305fc49253f0638e1c52580a02a1c8cbd8a7/store.c). Connect with nc fickle-tempest.picoctf.net 54628.
# Solución
Entrar a la página y causar un integer overflow para poder comprar la flag

- Primero entramos a la página, después compramos banderas, pero una cantidad "2400000" para con esto causar que nuestro estado de cuenta gane dinero por el overflow y con ello comprar nuestra flag

picoCTF{m0n3y_bag5_44cFf530}


# Notas adicionales
- 
# Referencias
- 