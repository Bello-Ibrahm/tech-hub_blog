from models.post import Post
from models import storage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Mapped

# Database connection details
db_type = "mysql"
username = "tech_hub_blog_dev"
password = "tech_hub_blog_dev_pwd"
hostname = "localhost"
port = "3306"
database_name = "tech_hub_blog_db"
echo_status = False

# Constructing the database URL
db_url = f"{db_type}://{username}:{password}@{hostname}:{port}/{database_name}"
engine = create_engine(db_url, echo=echo_status)

# Creating a new post instance
new_post = Post(
    title='1st post',
    date_posted='2024-02-28',
    content='this is my 1st blog post'
)

# Creating a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
session.add(new_post)

print( new_post, "successfully added new post")
