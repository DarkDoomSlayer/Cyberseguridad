# Scavenger Hunt
# Descripción del reto:
There is some interesting information hidden around this site. Can you find it? http://wily-courier.picoctf.net:63291/
# Solución:
curl -s http://wily-courier.picoctf.net:63291/ | grep "flag"
        curl -s http://wily-courier.picoctf.net:63291/mycss.css | grep "flag"
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
                                                                             
curl -s http://wily-courier.picoctf.net:63291/robots.txt
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
                                                                             
curl -s http://wily-courier.picoctf.net:63291/.htaccess
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
                                                                             
curl -s http://wily-courier.picoctf.net:63291/.DS_Store
Congrats! You've completed the scavenger hunt! Part 5: _9588550}

'picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_9588550}'
# Notas adicionales
# Referencias
https://youtu.be/E2gN3AGHirc?si=m0zEAmbOKh9yT1iE