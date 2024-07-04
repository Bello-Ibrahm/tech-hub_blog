
from models.user import User
from models import storage

# Create a new user object
new_user = User(
    name='john_doe',
    email='john.doe@example.com',
    password='hashed_password'  # Ensure the password is hashed
)

# Add the user to the session and save to the database
storage.new(new_user)
storage.save()

print("User added successfully")
