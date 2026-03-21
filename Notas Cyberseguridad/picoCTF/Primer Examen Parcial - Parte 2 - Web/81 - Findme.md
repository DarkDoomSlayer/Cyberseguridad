# Descripción
Help us test the form by submiting the username as `test` and password as `test!` The website running [here](http://saturn.picoctf.net:56421/).
# Solución
Entrar a la página, después interceptar el redireccionamiento y con ello conseguir nuestra flag

- Primero entramos al link que se nos da, después abrimos burpsuite y tratamos de loguearnos, interceptando, luego vamos avanzando poco a poco y los ids, los pasamos a decodificar en base64 en cyberchef

picoCTF{proxies_all_the_way_3d9e3697}


# Notas adicionales
- 
# Referencias
- https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=Y0dsamIwTlVSbnR3Y205NGFXVnpYMkZzYkY5MGFHVmZkMkY1WHpOa09XVXpOamszZlE