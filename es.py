# Weekly task 7
# Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
# The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
# Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.

# -------------------


# I assume that the number of e's means the number of e in both lowercase and uppercase.

# Create a file moby_dick.txt in my repository pands-weekly-tasks

# Create function to read and count a specific letter
# Function takes 2 parameters: textfile (name of the file needed to be read) and letter (the specific letter needed to be counted) which takes value 'e' by default
def numletter(textfile, letter = 'e'):
  try:
  # Open text file
    with open(textfile, 'r', encoding='utf-8') as f:
      # Read file
      data = f.read()
      # Uppercase the letter
      letter_uppercase = letter.upper()
      # Output the number of the letter
      return data.count(letter) + data.count(letter_uppercase)
  except FileNotFoundError:
    print(f"Error: The file '{textfile}' does not exist.")
  except UnicodeDecodeError:
    print(f"Error: The file '{textfile}' is not a text file.")


# Output the number of the letter 'e' in moby_dick.txt
numletter("moby_dick.txt",)



# Ressources
# https://www.w3schools.com/python/ref_string_count.asp
# https://www.w3schools.com/python/ref_string_upper.asp
# https://www.w3schools.com/python/python_ref_exceptions.asp
# https://docs.python.org/3/tutorial/errors.html



