# remove empty spaces
text = input("Enter a string: ").replace(" ", "").lower()



def isPalindrome(text):
    low = 0
    high = len(text)-1
    while low<=high:
        if text[low]!=text[high]:
            return False
        low+=1
        high-=1
    return True
    
    
print(isPalindrome(text))