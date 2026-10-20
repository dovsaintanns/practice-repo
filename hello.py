def main():
  name = input("What's your name, friend?")
  print(f"Hello {name}!")
  print(f"Nice to meet you!")
  grade = int(input(f"What grade are you in? Enter 9, 10, 11, or 12\n> "))
  if grade == 9:
    print("You're a freshman.")
  elif grade == 10:
    print("You're a sophomore.")
  elif grade == 11:
    print("You're a junior.")
  elif grade == 12: 
    print("You're a senior.")
  else:
    print("You're not a high school student!")

if __name__=="__main__":
  main()
