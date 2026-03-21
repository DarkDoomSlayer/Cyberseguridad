# Descripción
The agents interrupted the perpetrator's disk deletion routine. Can you recover this git repo? Download the disk image [here](https://challenge-files.picoctf.net/c_plain_mesa/5815a97d35f9214aebb870586256eb241b51eddc4967fd7f3ca815a190012d54/disk.img.gz).
# Solución
Descargar el archivo indicado, descomprimirlo y hacer todo el proceso de recuperación de los datos (Los cuales no fueron borrados) para con ello inspeccionar los commits y con ello obtener la flag

- Primero descargamos el archivo que se nos indica y lo descomprimimos, después para darnos una mejor idea de con que vamos a trabajar, le hacemos un "file" y con este nos damos cuenta que es un disco con 3 particiones, por lo que para poder maniobrar más sencillo, vamos a apoyarnos de The Sleuth Kit aplicándole un "mmls", después al observar las particiones usamos un "fls -o" en la que es más grande siendo la "1140736" , después aquí es ir indagando por los archivos, primero pasar por el home, luego por el usuario ctf-player y así sucesivamente hasta llegar a donde se encuentra el .git, con esto al ver que nada fue eliminado solamente hacemos un copiado de las carpetas usando "tsk_recover", nos traemos todo a una carpeta que queramos, hacemos una pequeña reconstrucción de la estructura agregando refs y aplicamos un "git status" y comprobamos directamente los commits con "cat .git/logs/HEAD", aqui podemos ver uno curioso que habla de agregar un escondite secreto y luego lo borra, por lo que solo mostramos el commit con "git show" y con ello obtenemos la flag

picoCTF{g17_r35cu3_16ac6bf3}

# Notas adicionales
- 
# Referencias
- 
