
def password_strength(password):
    if not password:
        return "Very Weak", 0, ["Password Cannot Be Empty."]
    rules = {
        "At least 8 characters long":len(password) >= 8,
        "An UpperCase letter":any(c.isupper() for c in password),
        "A LowerCase letter":any(c.islower() for c in password),
        "A Number":any(c.isdigit() for c in password),
        "A Special Character": any(not c.isalnum() for c in password)
             }
    completed_rules = [description for description, met in rules.items() if  met]
    missing_rules = [description for description,met in rules.items() if not met]
    score_ = len(completed_rules)
    if score_ < 3:
        rating = "Weak"
    elif score_ < 5:
        rating = "Medium"
    else:
        rating = "Strong"
    return rating, score_, missing_rules
user_password = input("Enter Password: ")
label, score, missing = password_strength(user_password)
print(f"\nResults: {label} ({score}5)")
if missing:
    print("To make it stronger, add:")
    for item in missing:
        print(f"- {item}")
print(score)
