def balance(arr):
    for i in range(len(arr)):
        this_arr = []
        if i != 0:
            this_arr = this_arr + arr[:i]

        if i != len(arr)-1:
            this_arr = this_arr + arr[i+1:]

        e_s, r_s = 0, 0
        for j in range(len(this_arr)):
            if j % 2 == 0:
                e_s+=this_arr[j]
            else:
                r_s+=this_arr[j]

        if e_s == r_s:
            print(arr[i])


balance([4,1,6,2])