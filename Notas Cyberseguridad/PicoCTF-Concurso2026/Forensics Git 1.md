# Descripción:
Can you find the flag in this disk image?

# Solución:
## 1. Descargamos y descomprimimos la imagen del disco crudo
wget https://challenge-files.picoctf.net/c_plain_mesa/4538dd1f2e93e907c17f0b663c0e1fae2d7054a72b4ee36977f20cfbf3b0a01c/disk.img.gz
gunzip disk.img.gz

## 2. Analizamos la tabla de particiones del disco
fdisk -l disk.img
## (Se identifica la partición 3 (Linux) iniciando en el sector 1140736)

## 3. Calculamos el offset (1140736 sectores * 512 bytes = 584056832) y montamos la partición
mkdir mnt_p3
sudo mount -o loop,offset=584056832 disk.img mnt_p3

## 4. Buscamos repositorios Git ocultos en el sistema de archivos montado
find mnt_p3 -name ".git" -type d 2>/dev/null
## Resultado: mnt_p3/home/ctf-player/Code/secrets/.git

## 5. Navegamos al directorio y extraemos el historial de cambios (commits)
cd mnt_p3/home/ctf-player/Code/secrets/
git log --all -p | grep "picoCTF"
-picoCTF{g17_r3m3mb3r5_d4ddf904}
+picoCTF{g17_r3m3mb3r5_d4ddf904}

picoCTF{g17_r3m3mb3r5_d4ddf904}

# Notas adicionales:
Este reto demuestra los riesgos de seguridad al utilizar sistemas de control de versiones. Un error común es hacer "commit" de información sensible y luego intentar borrarla en un commit posterior. Herramientas como 'git log -p' permiten inspeccionar los parches y diferencias de todo el historial, revelando la información eliminada. Además, el reto requiere conocimientos sólidos de montaje de sistemas de archivos de Linux calculando el offset de los sectores.

# Referencias: