# Unminify
# Descripción del reto:
I don't like scrolling down to read the code of my website, so I've squished it. As a bonus, my pages load faster! Browse here, and find the flag! http://titan.picoctf.net:63768/
# Solución:
curl -s http://titan.picoctf.net:63768/ | grep -o 'picoCTF{.*}'
picoCTF{pr3tty_c0d3_b99eb82e}"></p><p/ clas="picoctf{}">I just deliver flags, I don't know how to read them...</p></div></div><br class="picoctf{}

'picoCTF{pr3tty_c0d3_b99eb82e}'

# Notas adicionales:
El reto demuestra que la "minificación" (minification) de código HTML/JS/CSS es una técnica de optimización de rendimiento en el frontend, no una medida de seguridad ni de ofuscación. Aunque el código fuente pierda formato, espacios y saltos de línea volviéndose incómodo de leer para un humano, su contenido sigue expuesto en texto plano y puede ser analizado fácilmente utilizando herramientas de línea de comandos como 'curl' combinadas con expresiones regulares ('grep').
# Referencias: