class Solution(object):
    def addBinary(self, a, b):
        result = []  # List to store the binary sum
        carry = 0  # Initialize carry to 0

        # Pad the shorter binary number with zeros to make their lengths equal
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        # Iterate through the binary strings from right to left
        for i in range(max_len - 1, -1, -1):
            bit_sum = int(a[i]) + int(b[i]) + carry  # Sum of current bits and carry
            result.insert(0, str(bit_sum % 2))  # Insert the remainder in the front
            carry = bit_sum // 2  # Update the carry

        # If there's a remaining carry, add it to the front of the result
        if carry:
            result.insert(0, str(carry))

        return ''.join(result)  # Convert the list to a string and return