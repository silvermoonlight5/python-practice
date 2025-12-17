def almost_increasing(nums: list[int]) -> bool:
   s=0
   i = 0
   if s <= 1:
      return True
   else:
      return False
    

def main() -> None:

   print("almost_increasing([1,2,5,3,4]) =>",

         almost_increasing([1, 2, 5, 1, 6]))

   print("almost_increasing([1,2,3,2,1]) =>",

         almost_increasing([1, 2, 3, 2, 1]))

   print("almost_increasing([1,2,3,4]) =>",

         almost_increasing([1, 2, 3, 4]))

   assert almost_increasing([1, 2, 5, 3, 4]) is True

   assert almost_increasing([1, 2, 3, 2, 1]) is False

   assert almost_increasing([1, 2, 3, 4]) is True

 

if __name__ == "__main__":

   main()