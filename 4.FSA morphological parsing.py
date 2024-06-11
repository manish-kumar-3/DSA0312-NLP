
def generate_plural(word):
  """
  Generates the plural form of a noun using basic rules.

  Args:
      word: The singular noun to be pluralized.

  Returns:
      The plural form of the noun, or the original word if not recognized.
  """
  vowels = "aeiou"
  if word.endswith("y") and not word.endswith("ay"):
    return word[:-1] + "ies"  # Replace "y" with "ies" (except "play" etc.)
  elif word.endswith("f") or word.endswith("fe"):
    return word[:-1] + "ves"  # Replace "f" or "fe" with "ves"
  elif word[-1] in vowels:
    return word + "s"  # Add "s" for words ending in vowels
  else:
    return word + "s"  # Add "s" for most consonant cases

# Example usage with user input
while True:
  user_input = input("Enter a noun (or 'q' to quit): ")
  if user_input.lower() == 'q':
    break
  plural_form = generate_plural(user_input)
  print(f"Singular: {user_input} - Plural: {plural_form}")
