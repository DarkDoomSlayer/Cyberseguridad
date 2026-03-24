# Operation Oni

# Descripción del reto:

Download this disk image, find the key and log into the remote machine. [https://artifacts.picoctf.net/c/70/disk.img.gz](https://artifacts.picoctf.net/c/70/disk.img.gz)

# Solución:


```
wget https://artifacts.picoctf.net/c/70/disk.img.gz
gzip -d disk.img.gz
```



```
mmls disk.img
```

_

```
fls -r -o 206848 disk.img | grep -E "id_ed25519"
```



```
icat -o 206848 disk.img 2345 > id_ed25519
chmod 600 id_ed25519
```


```
ssh -i id_ed25519 -p 62986 ctf-player@saturn.picoctf.net
cat flag.txt
```

**Flag:** `picoCTF{k3y_5l3u7h_b5066e83}`

# Notas adicionales:

- **Análisis de Inodos:** El uso de `fls` permitió localizar el archivo `id_ed25519` dentro de la estructura de directorios oculta (`.ssh`) sin necesidad de montar la imagen.
    
- **Seguridad de SSH:** Es imperativo aplicar `chmod 600` a la llave privada extraída; de lo contrario, el cliente SSH rechazará la conexión por considerar que los permisos son demasiado abiertos (protección contra accesos no autorizados en el sistema local).
    
- **Persistencia:** Al ser un reto de instancia dinámica, el puerto de conexión cambia en cada intento, pero la estructura del sistema de archivos dentro de la imagen de disco se mantiene constante.
    

# Referencias:

[https://wiki.sleuthkit.org/index.php?title=Mmls](https://wiki.sleuthkit.org/index.php?title=Mmls) [https://linux.die.net/man/1/ssh](https://linux.die.net/man/1/ssh)