def find_dom(stickers):
    for i in range(len(stickers)):
        for j in stickers[i+1:]:
            a = stickers[i]  # a = {'a': 2, 'b': 1, 'c': 1}
            print('a',a)
            b = j  # b = {'a': 1, 'b': 1}
            print('b',b)
            akey = set(a.keys())
            bkey = set(b.keys())
            breaker = False
            if bkey == (akey & bkey):   # a is dominant.
                print('a is dom')
                for x in bkey:
                    if b[x] > a[x]:
                        breaker = True
                        break
                if breaker:
                    break
                stickers.remove(b)
            elif akey == (akey & bkey):   # b is dominant.
                print('b is dom')
                for y in akey:
                    if a[y] > b[y]:
                        breaker = True
                        break
                if breaker:
                    break
                stickers.remove(a)

# stickers = [{'a': 2, 'b': 1, 'c': 1}, {'a': 1, 'b': 1}]
stickers = [{'a': 2, 'b': 2, 'c': 1, 'd': 1}, {'a': 2, 'b': 2, 'c': 2}, {'a': 1, 'b': 1}, {'c':2}, {'c':1,'f':1}]
print('main',stickers)
find_dom(stickers)
print('main',stickers)