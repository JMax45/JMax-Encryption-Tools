caesar_dict1 = [("A","C"),("B","D"),("C","E"),("D","F"),("E","G"),("F","H"),
                ("G","I"),("H","J"),("I","K"),("J","L"),("K","M"),("L","N"),
                ("M","O"),("N","P"),("O","Q"),("P","R"),("Q","S"),("R","T"),
                ("S","U"),("T","V"),("U","W"),("V","X"),("W","Y"),("X","Z"),
                ("Y","A"),("Z","B"),

                ("a","c"),("b","d"),("c","e"),("d","f"),("e","g"),("f","h"),
                ("g","i"),("h","j"),("i","k"),("j","l"),("k","m"),("l","n"),
                ("m","o"),("n","p"),("o","q"),("p","r"),("q","s"),("r","t"),
                ("s","u"),("t","v"),("u","w"),("v","x"),("w","y"),("x","z"),
                ("y","a"),("z","b"),

                ("1","2"),("2","3"),("3","4"),("4","5"),("5","6"),("6","7"),
                ("7","8"),("8","9")]

caesar_dict2 = [("C","A"),("D","B"),("E","C"),("F","D"),("H","F"),("I","G"),
                ("J","H"),("K","I"),("L","J"),("M","K"),("N","L"),("O","M"),
                ("P","N"),("Q","O"),("R","P"),("S","Q"),("T","R"),("U","S"),
                ("V","T"),("W","U"),("X","V"),("Y","W"),("Z","X"),("A","Y"),
                ("B","Z"),("G","E"),

                ("c","a"),("d","b"),("e","c"),("f","d"),("h","f"),("i","g"),
                ("j","h"),("k","i"),("l","j"),("m","k"),("n","l"),("o","m"),
                ("p","n"),("q","o"),("r","p"),("s","q"),("t","r"),("u","s"),
                ("v","t"),("w","u"),("x","v"),("y","w"),("z","x"),("a","y"),
                ("b","z"),("g","e"),

                ("2","1"),("3","2"),("4","3"),("5","4"),("6","5"),("7","6"),
                ("8","7"),("9","8")]

encrypted_text = ("null")
decrypted_text = ("null")
def caesar_crypt():
    from __main__ import to_encrypt
    mytext = to_encrypt
    crypted_text = mytext.translate(str.maketrans(dict(caesar_dict1)))
    global encrypted_text
    encrypted_text = crypted_text
def caesar_decrypt():
    from __main__ import to_decrypt
    crypted_text = to_decrypt.translate(str.maketrans(dict(caesar_dict2)))
    global decrypted_text
    decrypted_text = crypted_text
