"""
The Array balancing problem,
non optimized version
"""


def countBalancingElements_(arr):
    a_e = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    a_o = [arr[i] for i in range(len(arr)) if i % 2 != 0]

    s_a_e = sum(a_e)
    s_a_o = sum(a_o)

    bal_element = None
    if s_a_e > s_a_o:
        for ele in a_e:
            if s_a_e - ele == s_a_o:
                bal_element = ele
                break
    elif s_a_o > s_a_e:
        for ele in s_a_o:
            if s_a_o - ele == s_a_e:
                al_element = ele
                break

    bal_elements = [arr[k] for k in range(len(arr)) if arr[k] == bal_element]

    return len(bal_elements)


def sub_arr(arr):
    arr_e = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    arr_o = [arr[i] for i in range(len(arr)) if i % 2 != 0]
    return arr_e, arr_o


def countBalancingElements(arr):
    bal_ele = []

    for i in range(len(arr)):
        left_sub_arr = arr[0:i]
        righ_sub_arr = arr[i + 1:]

        lsa_es, lsa_os = sub_arr(left_sub_arr)
        print(f"lsa_es-{lsa_es}, lsa_os-{lsa_os}")

        rsa_os, rsa_es = sub_arr(righ_sub_arr)
        print(f"rsa_os-{rsa_os}, rsa_es-{rsa_es}")

        if sum(lsa_es + rsa_es) == sum(rsa_os + lsa_os):
            bal_ele.append(arr[i])

    return len(bal_ele)


if __name__ == '__main__':
    print(countBalancingElements([4, 1, 6, 2]))
