# Inspect HTML
# Descripción del reto:
Can you get the flag? Go to this website and see what you can discover. http://saturn.picoctf.net:54419/
# Solución:
dark@kali:~$ curl -s http://saturn.picoctf.net:54419/
# (Al inspeccionar el código fuente devuelto, se encuentra un comentario HTML oculto al final de la etiqueta body)
picoCTF{1n5p3t0r_0f_h7ml_8113f7e2}

'picoCTF{1n5p3t0r_0f_h7ml_8113f7e2}'
# Notas adicionales:
El reto es una introducción básica a la inspección de código fuente. La bandera estaba oculta simplemente como un comentario en el HTML, el cual no es visible en la renderización normal del navegador, pero sí al ver el código en crudo o al usar las herramientas de desarrollador.
# Referencias: