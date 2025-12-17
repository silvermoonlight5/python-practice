def seconds_to_hms(seconds: int) -> tuple[int, int, int]:
   hours = seconds // 3600
   minutes = (seconds - hours * 3600) // 60
   seconds = seconds % 60
   return (hours, minutes, seconds)

def main() -> None:

   print("seconds_to_hms(3661) =>", seconds_to_hms(3661))

   print("seconds_to_hms(59)   =>", seconds_to_hms(59))

   assert seconds_to_hms(3661) == (1, 1, 1)

   assert seconds_to_hms(0) == (0, 0, 0)

 

if __name__ == "__main__":

   main()