# Secrets
# Descripción del reto:
We have several pages hidden. Can you find the one with the flag? http://saturn.picoctf.net:52098/
# Solución:
 curl -s http://saturn.picoctf.net:52098/ | grep href
    <link href="secret/assets/index.css" rel="stylesheet" />

 curl -s http://saturn.picoctf.net:52098/secret/ | grep href
    <link rel="stylesheet" href="hidden/file.css" />

 curl -s http://saturn.picoctf.net:52098/secret/hidden/ | grep superhidden
    <input type="hidden" name="db" value="superhidden/xdfgwd.html" />

 curl -s http://saturn.picoctf.net:52098/secret/hidden/superhidden/xdfgwd.html

<h3 class="flag">picoCTF{succ3ss_@h3n1c@10n_51b260fe}</h3>

'picoCTF{succ3ss_@h3n1c@10n_51b260fe}'

# Notas adicionales:
Seguridad por oscuridad. El servidor ocultaba la bandera en una estructura profunda de directorios (/secret/hidden/superhidden/) que solo eran visibles analizando las rutas de los recursos CSS y campos ocultos del HTML.
# Referencias: