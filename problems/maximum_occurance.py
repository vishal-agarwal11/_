"""
Max Occurance
"""
def maxOccurace(string):
    max_count = 0
    max_chr = None
    d = {}
    for chr in string:
        try:
            d[chr] = d[chr] + 1
            if d[chr] > max_count:
                max_count = d[chr]
                max_chr = chr
        except:
            d[chr] = 1

    print(f"{max_chr} occured {max_count} times.")
    print(d)

str_ = "ababccbdde"
#maxOccurace(str_)