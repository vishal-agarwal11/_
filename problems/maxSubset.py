
def maxSubset(arr):
    incl = arr[0]
    excl = 0
    
    for idx in range(1,len(arr)):
        excl_new = incl if incl > excl else excl
        incl = excl + arr[idx]
        excl = excl_new
        print(f"Inclusive - {incl}, Exclusive - {excl}")

    return incl if incl > excl else excl


if __name__ == "__main__":
    print(maxSubset([4,1,1,4,2,1]))

    print(maxSubset([-2,1,3, -4, 5]))