'''
Check if the given string is Palindrome or not 
// using two pinters
Input  = "MADAM"
Output = True
'''
def recursion(Left,Right,String):
    if Left<Right:
        if String[Left]!=String[Right]:
            return False
        return recursion(Left+1,Right-1,String)  
    return True    
String=input()
print(recursion(0,len(String)-1,String))


'''
// using One Pointer
'''

def recursion(Left,Right,String):
    if Left>Right//2:
        return True
    if String[Left]!=String[Right-Left-1]:
        return False
    return recursion(Left+1,Right,String)
String=input()
print(recursion(0,len(String),String))
