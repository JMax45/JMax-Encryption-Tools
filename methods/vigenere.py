import string
import random

encrypted_text = ("null")
decrypted_text = ("null")
encryption_key = ("null")
vigenere_translate = [("","")]

def vigenere_crypt():
    from __main__ import to_encrypt
    mytext = to_encrypt
    m=str(mytext.upper())
    def randomStringDigits(stringLength=6):
        var1SET = ("")
        var2SET = ("")
        var3SET = ("")
        var1SET = string.ascii_letters
        var2SET = string.digits
        var3SET = string.punctuation

        lettersAndDigits = var1SET + var2SET + var3SET
        return ''.join(random.choice(lettersAndDigits) for i in range(6))
            
    generated_password = randomStringDigits(8)
    k=str(generated_password)
    k*=len(m)//len(k)+1 
    c=""
    for i,j in enumerate(m):
            gg=(ord(j)+ord(k[i])) 
            c+=chr(gg%26+65)
    global encrypted_text
    encrypted_text = c        
    global encryption_key
    encryption_key = k
def vigenere_decrypt():
    from __main__ import to_decrypt,encryption_key
    c=str(to_decrypt)
    k=str(encryption_key)
    d="" 
    for i,j in enumerate(c): 
            gg=(ord(j)-ord(k[i])) 
            d+=chr(gg%26+65)
    global decrypted_text        
    decrypted_text = d
