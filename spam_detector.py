def spam_detector(alias):
    email_in_array = alias.split("@")
    
    if email_in_array[1] == "xyz.com":
        return "Spam!"
    else: 
        return "Não é Spam!"

email = "spam@xyza.com"
print(spam_detector(email))

#an another option would be: if email.endswith("@zyx.com")