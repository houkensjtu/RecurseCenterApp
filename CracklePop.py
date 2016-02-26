# Print out the numbers 1 to 100 (inclusive).
# If the number is divisible by 3, print Crackle instead of the number.
# If it's divisible by 5, print Pop.
# If it's divisible by both 3 and 5, print CracklePop.

# Variables description:
# i : the number under test.
# Crackle_num : First divisor, print Crackle if divisible by this.
# Pop_num : Second divisor, print Pop if divisible by this.

def CracklePop(Crackle_num, Pop_num):
    for i in range(1,101):
        if i % Crackle_num == 0 and i % Pop_num == 0:
            print("CracklePop")
        elif i % Crackle_num == 0:
            print("Crackle")
        elif i % Pop_num == 0:
            print("Pop")
        else:
            print(i)

if __name__ == "__main__":    
    Crackle_num = 3
    Pop_num = 5
    CracklePop(Crackle_num, Pop_num)
