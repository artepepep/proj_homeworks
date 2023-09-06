def is_admin(func):
    def wrapper(*args, **kwargs):
        user_type = kwargs.get('user_type')
        if user_type == 'admin':
            return func(*args, **kwargs)
        else:
            raise ValueError("Permission denied")
    return wrapper
@is_admin
def show_customer_receipt(user_type: str):
    print("receipt")
try:
    show_customer_receipt(user_type='user')
except ValueError as e:
    print(e)
show_customer_receipt(user_type = 'admin')
