
from pprint import pprint
def sort(arr, k):
    m_ = {}
    for ele in arr:
        try:
            m_[ele]+=1
        except:
            m_[ele] = 1

    max1 = 0
    max2 = 0
    res = []
    
    for key in m_:
        if m_[key] > m_[max1]:
            max2 = max1
            max1 = key
        elif m_[max2] < m_[key] < m_[max1]:
            max2 = key

    res.append(m_[max1])
    res.append(m_[max2])

    return res








if __name__ == "__main__":
    #arr = [0,0,1,1,1,2,2,3,3,3,3,3,4,4,4,4,4,4,4,4]
    #print(sort(arr, 2))
