def safe_divide(a: float, b: float) -> float | None:
     if b == 0:
      return None
     else:
      return (a/b)
def main() -> None:

  

   assert safe_divide(10, 2) == 5.0

   assert safe_divide(10, 0) is None

 

if __name__ == "__main__":

   main()
