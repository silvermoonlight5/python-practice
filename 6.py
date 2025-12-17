def word_count(text: str) -> dict[str, int]:
   text = text.lower()
   from collections import Counter
   words = text.split()
   freq = Counter(words)
   a = dict()
   for w, c in freq.items():
      a.update({w:c})
   return a

def main() -> None:

   print("word_count('Hi hi  HI') =>", word_count("Hi hi  HI"))

   print("word_count('one two two') =>", word_count("one two two"))

   assert word_count("hI Hi  HI") == {"hi": 3}

 

if __name__ == "__main__":

   main()
def main() -> None:

   print("word_count('Hi hi  HI') =>", word_count("Hi hi  HI"))

   print("word_count('one two two') =>", word_count("one two two"))

   assert word_count("Hi hi  HI") == {"hi": 3}

 

if __name__ == "__main__":

   main()
