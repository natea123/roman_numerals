def romanToDigit(s):

	rom_val={
	         "I":1,
	         "V":5,
	         "X":10,
	         "L":50,
	         "C":100,
	         "D":500,
	         "M":1000,
	         }

	int_val = 0
	"""for x, y in range(len(s)-1):
		if numerals[s[x]]<numerals[s[y]]:
			final_sum+=(numerals[s[y]]-numerals[s[x]])
		else:
			final_sum+=(numerals[s[x]]+numeral[s[y]])
	return final_sum"""

	for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

"""I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

IV = 4
IX = 9
XL = 40
XC = 90
CD = 400
CM = 900"""

year = raw_input("Please enter a year in roman numerals: ")

print(romanToDigit(year))
