'''
In-memory efficient DS for 100 million users
Support basic in, upd, del, search (crud)
'''


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('User Created!')

    def intro_user(self, guest_name):
        print(f'Hi {guest_name}, I am {self.name}! You can contact me at {self.email}')

    ## repr and str are used to create string representation of an object
    def __repr__(self):
        return f'User(username={self.username}, name={self.name}, email={self.email}'

    def __str__(self):
       # return self.__repr__()

        return f'User(username={self.username}, name={self.name}, email={self.email}'


# user1 = User('john', 'John Doe', 'john@doe.com')
# user1.intro_user('David')

# user2 = User('jane', 'Jane Doe', 'jane@doe.com')
# user2.intro_user('Amy')
# print(user2)

## Create 7 user profiles
jake = User('jake', 'Jake Sully', 'jake@ex.com')
novak = User('novak', 'Novak Djoko', 'novak@ex.com')
rafa = User('rafa', 'Rafa Nadal', 'rafa@ex.com')
roger = User('roger', 'Roger Federer', 'roger@ex.com')
andy = User('andy', 'Andy Murray', 'andy@ex.com')
carlos = User('carlos', 'Carlos Alcaraz', 'carlos@ex.com')
pete = User('pete', 'Pete Sampras', 'pete@ex.com')

users = [jake, novak, rafa, roger, andy, carlos, pete]
# can also access a user's details with dot notation --> jake.name etc..
''''
A. Insert
    into empty db
    insert when user already exists
    insert when doesnt exist
    
    Simple:  loop through the list and add the new user at a pos that keeps the list sorted

B. Find
    loop through the list and find the user object with username matching the query

C. Update
    loop through the list and find the user object matching the query and update the details
    
D. List
    Return the list of user objects
'''


class UserDatabase():

    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


database = UserDatabase()

database.insert(jake)
database.insert(novak)
database.insert(carlos)

user = database.find('novak')
print(user)

database.update(User(username='novak', name='Novak Dj', email='novakdj@ex.com'))
user = database.find('novak')
print(user)

print(database.list_all())

database.insert(andy)

print(database.list_all())

'''
Insert = O(n)
Find = O(n)
Update = O(n)
List = O(1)

Not efficient
'''
