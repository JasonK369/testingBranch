<<<<<<< HEAD
def check_palindrome(s):
	s = s.lower()
	for i in range (len(s)):
			if (s[i] != s[len(s) - 1 - i]):
				return False
	return True

input_str = input("Please input a palindrome: ")
while True:
	if not check_palindrome(input_str):
		input_str = input("No, you must input a palindrome: ")
	else:
		print ("Welcome to the wonderland!")
		break
=======
print("heha")

>>>>>>> development
