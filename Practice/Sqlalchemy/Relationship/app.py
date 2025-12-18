from models import Address, User, session

user1 = User(name="Sumer", age=30)
user2 = User(name="Prabhakar",age=28)

address1 = Address(city="Kalaburagi", state="KT", zip_code=585102)
address2 = Address(city="Mumbai", state="MH", zip_code=400001)
address3 = Address(city="Chennai", state="TN", zip_code=600001)

# define associations
user1.addresses.extend([address1, address2])
user2.addresses.append(address3)

session.add(user1)
session.add(user2)
session.commit()

print("User1: ", user1.addresses)
print("User2: ", user2.addresses)
print("Address1: ", address1.user)