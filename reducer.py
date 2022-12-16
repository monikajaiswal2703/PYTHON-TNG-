# import sys
# import mapper
# prev_word=None
# prev_count=0
# for i in sys.stdin:
#     i=i.strip()
#     word,count=i.split('\t')
#     count=int(count)

#     if prev_word==word:
#         prev_count+=count
#     else:
#         if prev_word:
#             print('%s\t%s'%(prev_word,prev_count))
#         prev_count=count
#         prev_word=word
# if prev_word==word:
#      print('%s\t%s'%(prev_word,prev_count))

# a="i am monika and i live in ujjain this is a mahakal nagary"
# a=a.split()
# # print(a)
# count=1
# prev_count=0
# prev_word=None
# for i in (a):
#     i=i.strip()
#     word=i.split()

#     if prev_word==word:
#         prev_count+=count
#     else:
#         if prev_word:
#             print(prev_word,prev_count)
#     prev_count=count
#     prev_word=word
# if prev_word==word:
#     print(prev_word,prev_count)
