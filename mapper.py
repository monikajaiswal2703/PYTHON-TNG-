def maper(b):
    for line in b:
        c=[]
        line=line.strip()
        words=line.split(',')
        for w in words:
            return w,1
            # prev_word=None
            # prev_count=0
            # for i in (c):
            #     i=i.strip()
            #     word,count=i.split()
            #     count=int(count)

            #     if prev_word==word:
            #         prev_count+=count
            #     else:
            #         if prev_word:
            #             print((prev_word,prev_count))
            #         prev_count=count
            #         prev_word=word
            # if prev_word==word:
            #     print((prev_word,prev_count))
a="AABCBBCDCCDAEEECDDEC"
b=(maper(a))
print(b)

def redcr(b,):
    prev_word=None
    prev_count=0
    for i in a:
        i=i.strip()
        word,count=i.split()
        count=int(count)

        if prev_word==word:
            prev_count+=count
        else:
            if prev_word:
                print((prev_word,prev_count))
            prev_count=count
            prev_word=word
    if prev_word==word:
        print((prev_word,prev_count))
redcr(b)
