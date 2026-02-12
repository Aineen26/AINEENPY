"""PROGRAM FOR VALIDATING EMAIL
PROGRAM NAME: EMAIL VALIDATOR
AUTHOR: AINEEN SAYYED
DATE CREATED: 31/01/2026"""

def validate_email(email):
   if"@" in email and email.count("@")==1:
       at_index = email.find("@")
       local_part = email[:at_index]
       domain_part = email[at_index+1:]
       #check if domain part and local part are not empty
       if len(local_part)>0 or len(domain_part)>0:
           #using nesting statement for checking dot(.) in domain not at very start and end
           dot_index = domain_part.find(".")
           if 0 < dot_index < len(domain_part) - 1:
               return True
           else:
               return False
       else:
           return False
   else:
       return False
#Function testing
user_input = input("Enter your email: ").strip()
if validate_email(user_input):
    print("Valid Email")
else:
    print("Invalid Email")