import math
import re

def calculate_entropy(password): #defines function called calculate entropy
  charset_size = 0 #for now the character set has value of 0
  if re.search(r"[a-z]", password):# searches for lowercase letters a-z and adds 26 to charset_size if seen in password
    charset_size += 26
  if re.search(r"[A-Z]",password):#searches for uppercase letters A-Z and adds 26 to charset_size if seen in password
    charset_size += 26
  if re.search(r"[0-9]",password):#searches for numbers 0-9 and adds 10 to charset_size if seen in passwords
    charset_size +=10
  if re.search(r"[!@#$%^&*()_+\-=\[\]{};:'\",.<>/?\\|`~]",password):#searches for special characters and adds 32 to charset_size if seen in passwords
    charset_size += 32
  if charset_size == 0:# if password contains no letters,numbers,or special characters then it would be = to 0 which will then return 0
    return 0
  entropy = len(password)*math.log2(charset_size)#takes length of password times the math.log2 to determine if password is hard to guess
  return entropy

def evaluate_strength(entropy):#defines new function called evaluate strength
  if entropy < 28:#runs through if statements to see how hard the password is to guess and says 'very weak' when entropy < 28
    return "Very Weak" 
  elif entropy < 36: #checks if entropy < 36 and returns 'Weak' (THIS ONLY RUNS IF FIRST CONDITION IS FALSE)
    return "Weak"
  elif entropy < 60:#checks if entropy is between 36-59 and returns 'Reasonable'
    return "Reasonable"
  elif entropy < 80:#checks if entropy is between 60-79 and returns 'Strong'
    return "Strong"
  else:
    return "Very Strong"#checks if entropy is 80 or more and returns 'Very Strong'

def suggest_improvements(password):#creates new function to suggest improvements to current password
  suggestions = []#empty list which adds tips when problem in password
  if len(password)<12:#checks if under 12 characters and suggests to add more
    suggestions.append("Use at least 12 characters.")
  if not re.search(r"[a-z]", password):#checks if password has lowercase letters, if not suggests to add 
    suggestions.append("Add lowercase letters.")
  if not re.search(r"[A-Z]",password):#checks if password has uppercase letters, if not suggests to add 
    suggestions.append("Add uppercase letters.")
  if not re.search(r"[0-9]",password):#checks if password has numbers, if not suggests to add at least one digit
    suggestions.append("Include at least one digit.")
  if not re.search(r"[!@#$%^&*()_+\-=\[\]{};:'\",.<>/?\\|`~]",password):#checks if password has special characters, if not suggests to add one 
    suggestions.append("Add at least one special character/symbol for better variety")
  common_patterns = [#list of common patterns and mistakes
      "password", "1234", "abcd", "qwerty", "admin"
  ]
  for pattern in common_patterns:#checks whether any insecure pattern appears
    if pattern in password.lower():
      suggestions.append("Avoid common words or patterns.")
      break
  return suggestions #returns suggestions

def analyze_password(password): #new function called analyze password
  entropy = calculate_entropy(password)#calculates entropy of password
  strength = evaluate_strength(entropy)#gives how strong the password is 
  suggestions = suggest_improvements(password)#suggests improvements for password

  print("\n🔐 Password Analyzer 🔐")#Header of code
  print("---------------------")
  print(f"Password length: {len(password)}")#how long the password is
  print(f"Estimated entropy: {entropy:.2f} bits")#shows entropy
  print(f"Strength rating: {strength}")#tells how strong password is

  print("\nSuggestions:")#header for suggestions
  if suggestions:#lists the suggestions for password if any
        for s in suggestions:
            print(f" - {s}")
  else:
        print(" - Looks good! Your password has good variety and length.")#tells its already good

if __name__ == "__main__":#asks user to enter password
    pwd = input("Enter a password to analyze: ")
    analyze_password(pwd)
