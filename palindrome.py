def isPalindrome(word):
    if  len(word) < 1:
        return True
    else:
        if  word[0]==word[-1]:
            return isPalindrome(word[1:-1])
        else:
            return False
    def fileInput(filename):
        palindromes = False
        fh = open(filename,"r")
        length=input("Enter length of palindromes:")
        d=int(length)
        try:
            for line in fh:
                for s in str(len(line)):
                    if isPalindrome(line.strip()):
                        palindromes = True
                        if(len(line.strip())==d):
                            print(line.strip())
        except:
             print("no palindromes found for length entered.")
        finally:
             fh.close()
                    
