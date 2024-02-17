from flask_login import current_user
from functools import wraps
from flask import abort

def admin_only(function):
    @wraps(function)
    def check_if_admin(*args, **kwargs):
        user_id = current_user.get_id()
        if user_id != None and int(user_id) == 1:
            print ("yesssssssssssssssssssssss create new post")
            return function(*args, **kwargs)
        else:
            print ("not authorized")
            return abort(403)


    return check_if_admin
