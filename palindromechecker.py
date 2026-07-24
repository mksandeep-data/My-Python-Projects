s=input()
#print("It is a palindrome")
reverse = s[::-1]
print(s[::-1])
if reverse == s:
    print("It is a palindrome")
else:
    print("Not a palindrome")
