# djangoblog
django project on Blog

# versions
Django version=1.11
Python=3.6
Channels-redis=2.1.2

# setting up virtual environment
sudo pip3.6 install virtualenv
virtualenv venv -p python3.6
source venv/bin/activate

# to run
~/newblog/chatroom/mysite$ python manage.py runserver 1234

# Blog
(1)login page ,regiter page
(You need to register first and then login with the same)

(2)Home page:
HOME: View Post,Add Post
MY Profile :Profile of the logged in user
Edit Profile:to edit firstnam,lastname and email id
Logout: To logout redirects to (1)
Chat: for chat two seperate users has to be created, and chat room is opened ,text typed ,refreshed on the other page
message will be received
