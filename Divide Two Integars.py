class Solution:
	def divide(self, dividend, divisor):
		"""
		This function performs integer division of two numbers
		and returns the result. It handles the edge cases for
		negative numbers and overflow.
		"""
		# Check if both numbers have the same sign
		positive = (dividend < 0) is (divisor < 0)

		# Convert both numbers to positive and initialize result
		dividend, divisor, res = abs(dividend), abs(divisor), 0

		# Perform division
		while dividend >= divisor:
			# Initialize variables for division
			temp, i = divisor, 1

			# Perform binary division
			while dividend >= temp:
				dividend -= temp
				res += i
				i <<= 1
				temp <<= 1

		# Handle negative result if necessary
		if not positive:
			res = -res

		# Handle overflow
		return min(max(-2 ** 31, res), 2 ** 31 - 1)
