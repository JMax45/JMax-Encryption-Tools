morse_dict1 = [("A",".- "),("B","-... "),("C","-.-. "),
               ("D","-.. "),("E",". "),("F","..-. "),
               ("G","--. "),("H",".... "),("I",".. "),
               ("J",".--- "),("K","-.- "),("L",".-.. "),
               ("M","-- "),("N","-. "),("O","--- "),
               ("P",".--. "),("Q","--.- "),("R",".-. "),
               ("S","... "),("T","- "),("U","..- "),
               ("V","...- "),("W",".-- "),("X","-..- "),
               ("Y","-.-- "),("Z","--.. "),(" ","/ ")]

morse_dict2 = [(".- ","A"),("-... ","B"),("-.-. ","C"),
               ("-.. ","D"),(". ","E"),("..-. ","F"),
               ("--. ","G"),(".... ","H"),(".. ","I"),
               (".--- ","J"),("-.- ","K"),(".-.. ","L"),
               ("-- ","M"),("-. ","N"),("--- ","O"),
               (".--. ","P"),("--.- ","Q"),(".-. ","R"),
               ("... ","S"),("- ","T"),("..- ","U"),
               ("...- ","V"),(".-- ","W"),("-..- ","X"),
               ("-.-- ","Y"),("--.. ","Z"),("/ "," ")]

encrypted_text = ("null")
decrypted_text = ("null")
def morse_crypt():
    from __main__ import to_encrypt
    mytext = to_encrypt
    crypted_text = mytext.upper().translate(str.maketrans(dict(morse_dict1)))
    global encrypted_text
    encrypted_text = crypted_text
def morse_decrypt():
    from __main__ import to_decrypt
    mytext = to_decrypt
    morse_to_letter3 = dict(morse_dict2)
    morse_to_decrypt = mytext.strip()
    decrypted_text1 = ("".join([morse_to_letter3.get(c + " ", "#error#")
                            for c in morse_to_decrypt.split(" ")]))
    global decrypted_text
    decrypted_text = decrypted_text1
