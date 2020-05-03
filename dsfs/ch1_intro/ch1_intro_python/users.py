#!/usr/bin/python3.6 


users = [{"id":0,"name":"Hero"},
         {"id":1,"name":"Dunn"},
         {"id":2,"name":"Sue"},
         {"id":3,"name":"Chi"},
         {"id":4,"name":"Thor"},
         {"id":5,"name":"Clive"},
         {"id":6,"name":"Hicks"},
         {"id":7,"name":"Devin"},
         {"id":8,"name":"Kate"},
         {"id":9,"name":"Klien"},]


friendships = [(0,1),
               (0,2),
               (1,2),
               (1,3),
               (2,3),
               (3,4),
               (4,5),
               (5,6),
               (6,8),
               (7,8),
               (8,9)]

'''
Add the list of friends to each user's 'object' 
'''
for u in users:
    u["friends"] = []
'''
for u in users:
    print(u)
'''

def avg_num_friend_connections():
    sum = 0
    avg = 0
    for u  in users:
        sum += len(u['friends'])
    avg = sum/len(users)
    return avg

def bootstrap():
    for u in range(len(users)):
        id = users[u].get("id")
        for f in friendships:
            if f[0] == id:
                users[u]['friends'].append(f[1])
def __main__():
    bootstrap()
    print(users)


__main__()



'''
for u in users:
    print(u)

'''