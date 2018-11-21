total_gpa = 0
total_credit = 0

while True:
	input_num = input()
	if input_num == "-1":
		break
	input_gpa, input_credit = input_num.split(" ")
	if float(input_gpa) < 0 or float(input_credit) < 0:
		print ("Wrong input!")
		continue
	#gpa = total gpa / total credit
	total_gpa += float(input_gpa) * float(input_credit)
	total_credit += float(input_credit)
	gpa = total_gpa / total_credit
	print ("Current GPA: "  + "{0:.2f}".format(gpa))
print ("Program ends.")
