'''
printing numbers up to 5
'''
def recursion(Count):
    if Count==5:
        return
    print(Count)
    Count+=1
    recursion(Count)
Count=1
recursion(Count)
