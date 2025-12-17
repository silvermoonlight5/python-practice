def sum_of_multiples(n: int) -> int:
    sum=0
    for i in range(n+1) :
       if i%3 == 0 or i%5 == 0:
          sum += i
    return sum           
   
def main() -> None:

   print("sum_of_multiples(10) =>", sum_of_multiples(10))

   print("sum_of_multiples(0)  =>", sum_of_multiples(0))

   assert sum_of_multiples(10) == 33

   assert sum_of_multiples(0) == 0

 

if __name__ == "__main__":

   main()