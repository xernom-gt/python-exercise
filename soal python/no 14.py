def cek_karakter(char):
    if char .isalpha():
        if char.lower() in "aiueo":
            return (f"huruf {char} adalah vokal")
        else :
            return (f"huruf {char} adalah konsonan")
    else :
        return (f"{char} bukanlah huruf")

char_input = input("masukan huruf :")

result = cek_karakter(char_input)

print(result)