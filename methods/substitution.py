symbolsAlpha = [chr(x) for x in range(65,91)]
symbolsCrypt = ['!','@','#','$','%','^','&','*','(',')','-','=',
'+','?',':',';','<','>','/','[',']','{','}','|','.',',','~']
keys = dict(zip(symbolsAlpha,symbolsCrypt))

def encryptDecrypt(mode, message, final = ""):
	if mode == 'E':
		for symbol in message:
			if symbol in keys: final += keys[symbol]
	if mode == 'D':
		for symbol in message:
			for key in keys:
				if symbol == keys[key]: final += key
	return final
    
encrypted_text = ("null")
decrypted_text = ("null")
def substitution_crypt():
    from __main__ import to_encrypt
    mytext = to_encrypt
    cryptMode=("E")
    crypted_text=(encryptDecrypt(cryptMode, mytext))    
    global encrypted_text
    encrypted_text = crypted_text
def substitution_decrypt():
    from __main__ import to_decrypt
    mytext = to_decrypt
    cryptMode=("D")
    crypted_text=(encryptDecrypt(cryptMode, mytext))
    global decrypted_text
    decrypted_text = crypted_text
