class Caesar:
    @staticmethod
    def encrypt (text,shift)-> str :
        if not text.isalpha():
            return None

        result=""
        for i in range(len(text)):

            #for upper-case letters
            if(text[i].isupper()):
                result+=chr((ord(text[i]) + shift - 65)% 26 +65)

                #for lower-case letters
            else:
                result+=chr((ord(text[i]) + shift - 97)% 26 +97)

        return result

    @staticmethod
    def decrypt (text,shift)-> str :
        if not text.isalpha():
            return None

        result=""
        for i in range(len(text)):

            #for upper-case letters
            if(text[i].isupper()):
                result+=chr((ord(text[i]) - shift - 65)% 26 +65)

                #for lower-case letters
            else:
                result+=chr((ord(text[i]) - shift - 97)% 26 +97)

        return result

    

