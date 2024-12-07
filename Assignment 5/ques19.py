
def unique_pairs(words):
    newlist=[x for x in words if len(x)>=4]
    newlist.sort()
    res=set()
    for i in range(len(newlist)):
        for j in range(i+1,len(newlist)):
            word1=newlist[i]
            word2=newlist[j]
            if set(word1).isdisjoint(set(word2)):
                res.add((word1,word2))
    return res
words = ["apple", "dogs", "cat", "bird", "fish", "zebra", "lion"]
print(unique_pairs(words))