
import re

def match_and_search():
   while True:
       text = input("Enter text: ")
       pattern = input("Enter regex pattern: ")
       match = re.search(pattern, text)

       if match:
           print("Match found:", match.group())
           print("All matches:", re.findall(pattern, text))
           print("Match details:", match.span(), match.start(), match.end())
       else:
           print("No match found.")

       if input("Analyze another text (y/n)? ").lower() != "y":
           break

if __name__ == "__main__":
   match_and_search()
