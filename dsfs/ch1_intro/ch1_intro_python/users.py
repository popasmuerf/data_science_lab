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

def avg_connections():
    sum = 0
    avg = 0
    for u  in users:
        sum += len(u['friends'])
    avg = sum/len(users)
    return avg

def most_connected_users():
    _users = []
    for u in users:
        _users.append(u)
        _users['sum_connects'] = len(u.get('friends'))
    return _users

def most_connected_users_by_id():
    _users = []
    for u in users:
        _users.append((u['id'],len(u['friends'])))
    return _users

def get_their_friends(friend):
    return friend.get('friends')

def who_you_may_know(id):
    _id = id
    friends = []
    who_i_may_know = []
    for u in users :
        if _id == users.get('id'):
            friends = u.get('friends')
            for f in friends:
                who_i_may_know = f.get('friends')
                break
            break
    return who_i_may_know






    '''
    for u in users:
        id = u.get('id')
        friends = u.get('friends')
        for f in friends:
            who_i_may_know.append(f)
    '''


        
        

def bootstrap():
    for u in range(len(users)):
        id = users[u].get("id")
        for f in friendships:
            if f[0] == id:
                users[u]['friends'].append(f[1])

def __main__():
    bootstrap()
    print(avg_connections())
    _users = most_connected_users_by_id()
    #print(_users)
    print(users)



__main__()



'''
for u in users:
    print(u)

'''