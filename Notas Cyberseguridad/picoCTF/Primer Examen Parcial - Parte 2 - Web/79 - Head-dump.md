# Descripción
Welcome to the challenge! In this challenge, you will explore a web application and find an endpoint that exposes a file containing a hidden flag. The application is a simple blog website where you can read articles about various topics, including an article about API Documentation. Your goal is to explore the application and find the endpoint that generates files holding the server’s memory, where a secret flag is hidden. The website is running [picoCTF News](http://verbal-sleep.picoctf.net:53815/).
# Solución
Entrar a la página y revisarla, descargar el archivo headdump y inspeccionarlo para conseguir la flag

- Entrar al link dado, después entrar a "Api Documentation", alli pasar hasta donde aparece el headdump, alli descargar el archivo que aparece y simpplemente buscar con un grep "picoCTF" y con ello obtener la flag

picoCTF{Pat!3nt_15_Th3_K3y_59106086}


# Notas adicionales
- 
# Referencias
- 