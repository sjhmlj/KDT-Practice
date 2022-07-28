'''
* 베스트 셀러
* 가장 많이 팔린 책의 제목 출력
'''

n = int(input())
sold_books = []
book_counter = {}

# input 
for i in range(n):
    book = input()
    sold_books.append(book)

# input -> dict 
for sold_book in sold_books:
    if sold_book in book_counter:
        book_counter[sold_book] += 1
    else:
        book_counter[sold_book] = 1

# 가장 많이 팔린 책 출력
# 단, 여러개일 경우 사전순으로 가장 앞서는 제목 출력
sold_max = list(book_counter.values()).count(max(book_counter.values()))

if sold_max >= 2:
    print(sorted(filter(lambda x : book_counter[x] == max(book_counter.values()), book_counter), key = lambda x : x)[0])
else:
    print(sorted(book_counter, key = lambda x : book_counter[x], reverse=True)[0])