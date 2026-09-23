################ Sensitive info delete from dictitionary ################

user = {
    "user_name": "John",
    "password" : "test@123",
    "email":"john@example.com",
    "address" : "123 Main St",
    "country": "Australia"
}

sensitive_info = ["password", "address", "phone"]

for key in sensitive_info:
    if key in user:
        user.pop(key)
    else:
        print(f"{key} not found in user dictionary.")

print(f"User information after removing sensitive info: {user}")

