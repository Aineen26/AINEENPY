
def validate_email(email):
   if"@" in email and email.count("@")==1:
       at_index = email.find("@")
       local_part = email[:at_index]
       domain_part = email[at_index+1:]
       
       if len(local_part)>0 or len(domain_part)>0:
           dot_index = domain_part.find(".")
           if 0 < dot_index < len(domain_part) - 1:
               return True
           else:
               return False
       else:
           return False
   else:
       return False
user_input = input("Enter your email: ").strip()
if validate_email(user_input):
    print("Valid Email")
else:
    print("Invalid Email")
