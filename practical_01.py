# borrowing count of books by library members
borrow_counts=[3,5,0,2,5,1,0,4,5,2]

#1. calculate avarage number of  books borrowed
# total = sum(borrow_counts)
# avarage= total / len(borrow_counts)

# print("borrowing Recodes :",borrow_counts)

# print("Average number of books borrowed:",avarage)

#2.find highest and lowest borrowing counts
# highest = max(borrow_counts)
# lowest = min(borrow_counts)

# print("highest number of borrowings : ",highest)
# print("lowest number of borrowings : ",lowest)

#3.count members who have not borrowed any books

# Zero_count = borrow_counts.count(0)

# print("number of members who borrowed 0 books :", Zero_count)

# 4. find the mode (most frequently occurring borrowing count)
frequency = {}
for count in borrow_counts:
    if count in frequency:
        frequency[count] += 1
    else: 
        frequency[count] = 1
mode = max(frequency,key= frequency.get)

print("Most frequently occurring borrowing count (mode) :",mode)