import validators

# Get email
email = input('What\'s your email address?: ')

# Check whether valid or invalid
print('Valid') if validators.email(email) else print('Invalid')
