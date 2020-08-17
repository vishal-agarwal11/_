"""
This code converts a nested list into aflat list
input: [1,2,3,4, [5,6,[7, 8, [9], 10], 11, [12, 13, [14]]], 15, 16, 17,[18, 19], [20]]
output:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
"""


def resolve_nested_list(array, final_array=[]):
    for ele in array:
        if isinstance(ele, list):
            resolve_nested_list(ele, final_array)
        else:
            final_array.append(ele)

    return final_array


if __name__ == "__main__":
    sample = [1, 2, 3, 4, [5, 6, [7, 8, [9], 10], 11, [12, 13, [14]]], 15, 16, 17, [18, 19], [20]]
    print(resolve_nested_list(sample))
