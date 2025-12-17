def unique_in_order(items: list[int]) -> list[int]:
   new = []
   for i in items:
      if i not in new:
         new.append(i)
   return new
      
def main() -> None:

   print("unique_in_order([3,3,1,3,2,2]) =>",

         unique_in_order([3, 3, 1, 3, 2, 2]))

   assert unique_in_order([3, 3, 1, 3, 2, 2]) == [3, 1, 2]

   assert unique_in_order([]) == []

 

if __name__ == "__main__":

   main()


