def math_Happy(n):
    sum = 0
    while n > 0:
        a = n % 10
        sum += a * a
        n //= 10
    return sum

def isHappy(n):
    """
    Return True if n is a happy number, and False if not.
    """
    seen = set()
    while n != 1:
        k = math_Happy(n)
        if k in seen:
            return False
        seen.add(k)
        n = k
    return True 
    
if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
    
    print("Results saved to /app/bind_mount/output.txt")
