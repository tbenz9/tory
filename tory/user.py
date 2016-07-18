import psutil, pwd, grp
import pprint

def get_users():
    dict = {}
    #find current users and add to the the dictionary
    try:    
        users = psutil.users()

        names = []
        for user in users:
            names.append(user[0])
        dict['current_users'] = names
    except:
        print "Current Users not found"

    #find all users
    try:    
        all_users = []
        for p in pwd.getpwall():
            all_users.append(p[0])
        dict['all_users'] = all_users
    except:
        print "All Users not found"


    #make a dict of the groups of all the users
    try:
        groups = {}
        for p in pwd.getpwall():
            groups[p[0]] = grp.getgrgid(p[3])[0] 
        dict['groups'] = groups
    except:
        print "Groups not found"

    return dict


