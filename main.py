from crawlers import tgju_creawler
from utils import write_to_file

if __name__ == "__main__":
    print("Hey, let's see gold coins price for now... ")
    data = tgju_creawler()
    write_to_file(text = data)
    print(data)
    print("Bye.")
