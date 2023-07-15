s=input("enter a word: ")
reverse=s[::-1]
def palindrom(s):
    while True:
        if s[::1]==reverse:
            print("True")
            break
        if s!=reverse:
            print("False")
            continue 
            
print(palindrom(s))   
