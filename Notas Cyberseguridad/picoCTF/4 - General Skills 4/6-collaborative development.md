# collaborative development
# Descripción del reto:
My team has been working very hard on new features for our flag printing program! I wonder how they'll work together? You can download the challenge files here:
# Solución:
 unzip challenge.zip
Archive:  challenge.zip
replace drop-in/.git/description? [y]es, [n]o, [A]ll, [N]one, [r]ename: A
  inflating: drop-in/.git/description  
  inflating: drop-in/.git/hooks/applypatch-msg.sample  
  inflating: drop-in/.git/hooks/commit-msg.sample  
  inflating: drop-in/.git/hooks/fsmonitor-watchman.sample  
  inflating: drop-in/.git/hooks/post-update.sample  
  inflating: drop-in/.git/hooks/pre-applypatch.sample  
  inflating: drop-in/.git/hooks/pre-commit.sample  
  inflating: drop-in/.git/hooks/pre-merge-commit.sample  
  inflating: drop-in/.git/hooks/pre-push.sample  
  inflating: drop-in/.git/hooks/pre-rebase.sample  
  inflating: drop-in/.git/hooks/pre-receive.sample  
  inflating: drop-in/.git/hooks/prepare-commit-msg.sample  
  inflating: drop-in/.git/hooks/update.sample  
  inflating: drop-in/.git/info/exclude  
 extracting: drop-in/.git/refs/heads/main  
 extracting: drop-in/.git/refs/heads/feature/part-1  
 extracting: drop-in/.git/refs/heads/feature/part-2  
 extracting: drop-in/.git/refs/heads/feature/part-3  
 extracting: drop-in/.git/HEAD       
  inflating: drop-in/.git/config     
 extracting: drop-in/.git/objects/77/d6ceca6fe23b57d88cf16f20003e10d6715690  
 extracting: drop-in/.git/objects/b9/32e8c048154a46d224cd7691c99dc8cb88164a  
 extracting: drop-in/.git/objects/22/58a0f267d57e8b6025e2a020b77fac7a553c92  
 extracting: drop-in/.git/objects/6e/17fb3a35364b4f9bb8bef8b5e6a5af2d3e7dfa  
 extracting: drop-in/.git/objects/43/e44dd37ba0c0adc3d78d0b85d699859ec8d75c  
 extracting: drop-in/.git/objects/8e/ea0627726fc363246015cb4c7e927e70286e87  
 extracting: drop-in/.git/objects/7a/b4e25c0cd108374b2275fdb1fcdf635e591833  
 extracting: drop-in/.git/objects/d1/f3407cee4479c075997b497fa290ca636fe258  
 extracting: drop-in/.git/objects/05/db9e274ff691e0f9fb492403b570629eb80aa9  
 extracting: drop-in/.git/objects/4f/136da027f9a97032d53dd5f667dd6c7852737c  
 extracting: drop-in/.git/objects/dd/f6fd2129098bf677ac010259a2a642060aea47  
 extracting: drop-in/.git/objects/65/5c7bfebe9c221369ab00ac7374d0d4bd4d62a9  
  inflating: drop-in/.git/index      
 extracting: drop-in/.git/COMMIT_EDITMSG  
  inflating: drop-in/.git/logs/HEAD  
  inflating: drop-in/.git/logs/refs/heads/main  
  inflating: drop-in/.git/logs/refs/heads/feature/part-1  
  inflating: drop-in/.git/logs/refs/heads/feature/part-2  
  inflating: drop-in/.git/logs/refs/heads/feature/part-3  
  inflating: drop-in/flag.py  
flag.py  message.py  message.txt
git branch -a
  feature/part-1
  feature/part-2
  feature/part-3
* main
  master
$ git show feature/part-1:flag.py
print("Printing the flag...")
print("picoCTF{t3@mw0rk_", end='')

$ git show feature/part-2:flag.py
print("Printing the flag...")

print("m@k3s_th3_dr3@m_", end='')

$ git show feature/part-3:flag.py
print("Printing the flag...")

print("w0rk_6c06cec1}")
picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_6c06cec1}
# Notas adicionales

# Referencias