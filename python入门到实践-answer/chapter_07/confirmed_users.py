# Start out with some users that need to be verified,
#  and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []



while unconfirmed_users:  			# Verify each user, until there are no more unconfirmed users.
    current_user = unconfirmed_users.pop(0)	  
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)   #  Move each verified user into the list of confirmed users.
    
print("\nThe following users have been confirmed:") # Display all confirmed users.
for confirmed_user in confirmed_users:
    print('\t'+confirmed_user.title())
