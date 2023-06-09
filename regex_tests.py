# The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice.
# For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. 

import re

def repeating_letter_a(text):
    result = re.search(r"(a|A).*\1", text, re.IGNORECASE)
    return result is not None

print(repeating_letter_a("banana"))  # True
print(repeating_letter_a("pineapple"))  # False
print(repeating_letter_a("Animal Kingdom"))  # True
print(repeating_letter_a("A is for apple"))  # True


print("\n" + "-"*10 + "\n")


# Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters
# (including letters, numbers, and underscores) separated by one or more whitespace characters.

import re
def check_character_groups(text):
  result = re.search(r"\w+\s+\w+", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False


print("\n" + "-"*10 + "\n")


# Fill in the code to check if the text passed looks like a standard sentence,
# meaning that it starts with an uppercase letter, followed by at least some lowercase letters
# or a space, and ends with a period, question mark, or exclamation point. 

import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z\s]*[.!?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True


print("\n" + "-"*10 + "\n")


import re
def check_web_address(text):
  pattern = r"^[a-zA-Z0-9_.+-]+(?:\.[a-zA-Z0-9-]+)*$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True


print("\n" + "-"*10 + "\n")


import re
def check_time(text):
  pattern = r"^(1[0-2]|0?[1-9]):([0-5][0-9]) ?([ap]m|AM|PM)$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False


print("\n" + "-"*10 + "\n")


import re
def contains_acronym(text):
  pattern = r"\([A-Za-z0-9]{2,}\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


print("\n" + "-"*10 + "\n")


import re
def check_zip_code (text):
  result = re.search(r"\s\d{5}(?:-\d{4})?", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False