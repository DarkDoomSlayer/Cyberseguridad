# Insp3ct0r
# Descripción del reto:
Kishor Balan tipped us off that the following code may need inspection: http://fickle-tempest.picoctf.net:57151
# Solución:
curl -s http://fickle-tempest.picoctf.net:57151/ | grep "flag"
	<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
curl -s http://fickle-tempest.picoctf.net:57151/mycss.css | grep "flag"
/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */
curl -s http://fickle-tempest.picoctf.net:57151/myjs.js | grep "flag"
/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?302945a7} */

'picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?302945a7}'
# Notas adicionales
# Referencias
https://youtu.be/f1infpFomIM?si=TBVaJMZy91CYlwyZ