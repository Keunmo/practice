# #Time Limit Exceeded
# def dailyTemperatures(T):
#     T.append('End')
#     days = []
#     print("T:", T)
#     today_index = -1
#     for today in T:
#         today_index += 1
#         if today == 'End':
#             break
#         count = 0
#         print("today:", today)
#         print("today_i:", today_index)
#         for findwarm in T[today_index+1:]:
#             print("findrange", T[today_index+1:])
#             count+=1
#             print("count:", count)
#             if findwarm == 'End':
#                 days.append(0)
#                 break
#             if findwarm > today:
#                 print("got it!")
#                 days.append(count)
#                 print("days:", days)
#                 break
#     print(days)
#     return days


def dailyTemperatures(T):
    day = []
    T.append("E")
    temps = str(T)
    temps=temps[1:-1]
    temps=temps.replace(",", "")
    count = 0
    for today in temps:
        today_index = temps.index(today)
        wammer = int(today)+1
        while wammer <= 100:
            warmday = temps[today_index:].find(str(wammer))
            if warmday > 0:
                day.append(warmday)
                break
            else:
                day.append(0)
                break
            warmmer+=1
    return day


dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])

# ans = [1, 1, 4, 2, 1, 1, 0, 0]