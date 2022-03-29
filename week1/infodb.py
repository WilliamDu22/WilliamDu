infodb = [{
            "Name": "William",
            "Favorite Food": "medkits so i can hit a medkit momentum sui",
            "Top 3 Favorite Activities": ["Video Games", "Sleeping", "Talking With Friends"],
            "Favorite Word": "https://www.youtube.com/channel/UC38EVQw1_nh4L5w37nhmlig yes"

          },
          {
            "Name": "Alex",
            "Favorite Food": "Apples",
            "Top 3 Favorite Activities": ["Watch YouTube", "Homework", "Running"],
            "Favorite Word": "k"

          },
          {
            "Name": "Ryan",
            "Favorite Food": "Cow",
            "Top 3 Favorite Activities": ["Eating Cow", "Sleeping", "Walking On My Head"],
            "Favorite Word": "Cow"

          },
          {
            "Name": "Bobby Boi",
            "Favorite Food": "glizzy",
            "Top 3 Favorite Activities": ["Traveling", "Sleeping", "Video Games"],
            "Favorite Word": "boi"

          }
          ]


def print_data(n):
    print("\t", infodb[n]["Name"])
    print("Favorite Food: ", end="")
    print(infodb[n]["Favorite Food"])
    print("Top 3 Favorite Activities: ", end="")
    print(", ".join(infodb[n]["Top 3 Favorite Activities"]))
    print("Favorite Word: ", end="")
    print(infodb[n]["Favorite Word"])
    print()

def forl():
  for i in range(len(infodb)):
    print_data(i)


def whilel():
  n = 0
  while n < len(infodb):
    print_data(n)
    n += 1
  return


def recursive(n):
  if n >= len(infodb):
    return
  elif n < len(infodb):
    print_data(n)
    return recursive(n + 1)
def recursivel():
  recursive(0)