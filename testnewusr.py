from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

# Provided database connection details
db_type = "mysql"
username = "tech_hub_blog_dev"
password = "tech_hub_blog_dev_pwd"
hostname = "localhost"
port = "3306"
database_name = "tech_hub_blog_db"
echo_status = False # Disabling echo by default, change to True if needed

# Construct the database URL
db_url = f"{db_type}://{username}:{password}@{hostname}:{port}/{database_name}"

# Create an engine to connect to the database
engine = create_engine(db_url, echo=echo_status)

# Create a base class for our declarative class definitions
Base = declarative_base()

# Define a Credentials class to represent the table structure
class User(Base):
    __tablename__ = 'users'

    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    image_file = Column(String(20), nullable=False, default='default.jpg')
    password = Column(String(60), nullable=False)
    user_posts = relationship('Post', backref='author', lazy=True)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


# Create the database schema
# Drop the existing 'users' table if it exists
# Base.metadata.drop_all(engine)

# Create the database schema with the updated table structure
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add the provided credentials directly
new_user = User(username='john_doe', email='john.doe@example.com', image_file='default.jpg', password='hashed_password')

session.add(new_user)
session.commit()

print("User added successfully.")

# Close the session
session.close()
