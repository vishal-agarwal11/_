#Find the occurences of a substr in a string 


def str_rem_duplicate(string):
    visited = []
    str_len = len(string)

    this_ptr = 0
    while this_ptr <= str_len - 1:
        if string[this_ptr] not in visited:
            visited.append(string[this_ptr])
            this_ptr+=1
        else:
            string = string[0:this_ptr]+string[this_ptr+1:]
            str_len-=1

    print(string)

str_rem_duplicate("astrsattpquv")






