# MatchTheRegex
# Descripción del reto:
How about trying to match a regular expression. The website is running here. http://saturn.picoctf.net:49211/
# Solución:
curl -s http://saturn.picoctf.net:49211/ | grep "//"
                // ^p.....F!?

curl -s "http://saturn.picoctf.net:49211/flag?input=picoCTF"
{"flag":"picoCTF{succ3ssfully_matchtheregex_2375af79}"}

'picoCTF{succ3ssfully_matchtheregex_2375af79}'
# Notas adicionales
# Referencias