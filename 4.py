def is_palindrome(s: str) -> bool:
    if all(s[i] == s[-i-1] for i in range(len(s)//2)):
        return True
    else:
        return False
       
       
def main() -> None:

   print("is_palindrome('racecar') =>", is_palindrome("racecar"))

   print("is_palindrome('A man a plan a canal Panama') =>",

         is_palindrome("A man a plan a canal Panama"))

   print("is_palindrome('hello') =>", is_palindrome("hello"))

   assert is_palindrome("racecar") is True

   assert is_palindrome("hello") is False

 

if __name__ == "__main__":

   main()