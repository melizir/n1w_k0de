s=input("enter a word: ")
reverse=s[::-1]
def palindrom(s):
    while True:
        if s[::1]==reverse:
            print(s,"is palindrome ")
            break
        if s!=reverse:
            print(s,"not a palindrome !")
            continue 
            
print(palindrom(s))   
