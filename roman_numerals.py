def romanToDigit(s):

	numerals={
	         "I":1,
	         "V":5,
	         "X":10,
	         "L":50,
	         "C":100,
	         "D":500,
	         "M":1000,
	         }

	final_sum = 0
	for x, y in s:
		if numerals[x]<numerals[y]:
			final_sum+=(numerals[y]-numerals[x]
		else:
			final_sum+=(numerals[x]+numerals[y]
	return final_sum

"""I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

IV = 4
IX = 9
XL = 40
XC = 90
CD = 400
CM = 900"""

roman = "XXX"

print(romanToDigit(roman))
