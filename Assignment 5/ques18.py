list1=[1,2,3,4]
list2=[5,6,7,8]


def analyze_sets(list1,list2):
    set1=set(list1)
    set2=set(list2)
    set3=set1^set2
    list1=list(set3)
    list4=[x*2 if x%2==0 else x+5 for x in list1 ]
    list4.sort()
    return list4
list4=analyze_sets(list1,list2)
print(list4)