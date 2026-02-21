# ### Special
# Descripción del reto:
Run the Python script `code.py` in the same directory as `codebook.txt`.

- [Download code.py](https://artifacts.picoctf.net/c/1/code.py)
- [Download codebook.txt](https://artifacts.picoctf.net/c/1/codebook.txt)
# Solución:
ssh -p 56563 ctf-player@saturn.picoctf.net
ctf-player@saturn.picoctf.net's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.8.0-1044-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Last login: Sat Feb 21 02:27:50 2026 from 127.0.0.1
Special$ a=1 cat * */*
A cat * */* 
sh: 1: A: not found
Special$ ../../bin/ls blargh
../../bin/ls large 
../../bin/ls: cannot access 'large': No such file or directory
Special$ ../../bin/cat blargh/flag.txt
../../bin/cat blargh/flag.txt 
picoCTF{5p311ch3ck_15_7h3_w0r57_a60bdf40}Special$ 

# Notas adicionales
# Referencias