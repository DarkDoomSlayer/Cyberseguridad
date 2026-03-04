# WebDecode
# Descripción del reto:
Do you know how to use the web inspector? http://titan.picoctf.net:50222/
# Solución:
dark@kali:~$ curl -s http://titan.picoctf.net:50222/about.html | grep notify_true
  <section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfZGYwZGE3Mjd9">

 echo "cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfZGYwZGE3Mjd9" | base64 -d
picoCTF{web_succ3ssfully_d3c0ded_df0da727}

'picoCTF{web_succ3ssfully_d3c0ded_df0da727}'

# Notas adicionales:
El reto consiste en identificar información oculta en atributos no estándar del HTML. En este caso, la bandera se encontraba codificada en Base64 dentro del atributo 'notify_true' de una etiqueta <section>. La codificación Base64 es fácilmente identificable por su juego de caracteres y se decodifica de forma directa en la terminal.

# Referencias: