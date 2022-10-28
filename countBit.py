# Function to count total bits in a number
 
def countTotalBits(num):
     
     # bit_length function return
     # total bits in number
     B_len = num.bit_length()
     print("Total bits in binary are : ", B_len)
 
# Driver program
if __name__ == "__main__":
    num = 13
    countTotalBits(num)
