# where are the robots
# Descripción del reto:
Can you find the robots? http://fickle-tempest.picoctf.net:64922
# Solución:
curl -s http://fickle-tempest.picoctf.net:64922/robots.txt
User-agent: *
Disallow: /cc6b1.html
curl -s http://fickle-tempest.picoctf.net:64922/cc6b1.html | grep "picoCTF"
      <flag>picoCTF{ca1cu1at1ng_Mach1n3s_cc6b1}</flag></p>

'picoCTF{ca1cu1at1ng_Mach1n3s_cc6b1}'
# Notas adicionales
# Referencias
https://youtu.be/LRgg3Kcnbuw?si=yeXfc8PYZ5p1fe6H