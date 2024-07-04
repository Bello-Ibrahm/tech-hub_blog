<<<<<<< HEAD

=======
>>>>>>> 405d5c8 (DB is now connected with the models)
from models.user import User
from models import storage

# Create a new user object
new_user = User(
<<<<<<< HEAD
    name='john_doe',
    email='john.doe@example.com',
=======
    username='john_doe',
    email='john.doe@example.com',
    image_file='default.jpg',
>>>>>>> 405d5c8 (DB is now connected with the models)
    password='hashed_password'  # Ensure the password is hashed
)

# Add the user to the session and save to the database
storage.new(new_user)
storage.save()

print("User added successfully")
<<<<<<< HEAD

=======
>>>>>>> 405d5c8 (DB is now connected with the models)
