# Includes

# Descripción del reto:

Can you get the flag? Go to this website and see what you can discover. [http://saturn.picoctf.net:62007/](https://www.google.com/search?q=http://saturn.picoctf.net:62007/)

# Solución:

dark@kali:~$ curl -s [http://saturn.picoctf.net:62007/](https://www.google.com/search?q=http://saturn.picoctf.net:62007/)

# (Al inspeccionar el HTML devuelto, se observa que incluye dos archivos externos: style.css y script.js)

dark@kali:~$ curl -s [http://saturn.picoctf.net:62007/style.css](http://saturn.picoctf.net:62007/style.css) /* picoCTF{1nclu51v17y_1of2_ */

dark@kali:~$ curl -s [http://saturn.picoctf.net:62007/script.js](http://saturn.picoctf.net:62007/script.js) // f7w_2of2_b8f4b022}

picoCTF{1nclu51v17y_1of2_f7w_2of2_b8f4b022}

'picoCTF{1nclu51v17y_1of2_f7w_2of2_b8f4b022}'
# Notas adicionales:

El reto demuestra cómo el código HTML incluye archivos externos (hojas de estilo y scripts) para separar el diseño y la lógica. La bandera fue dividida en dos partes y oculta dentro de los comentarios de estos archivos.

# Referencias: