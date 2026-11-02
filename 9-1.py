class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and the cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open.")
        
    def set_number_served(self, number_served):
        self.number_served = number_served
        
    def increment_number_served(self, additional_served):
        self.number_served += additional_served
        
my_restaurant = Restaurant("Sang", "VietNam")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
# my_restaurant.number_served = 10
my_restaurant.set_number_served(11)
my_restaurant.increment_number_served(100)
print(my_restaurant.number_served)

your_restaurant = Restaurant("Ludvig's Bistro", "Seafood")
your_restaurant.describe_restaurant()
Restaurant("Mango Thai", "Thai Food").describe_restaurant()
Restaurant("Korean BBQ", "Korean Food").describe_restaurant()

class User:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user's name is {self.first_name} {self.last_name}, age is {self.age}, sex is {self.sex}.")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, welcome to the restaurant.")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("John", "Doe", 25, "Male")
user1.describe_user()
user1.greet_user()

user2 = User("Jane", "Smith", 30, "Female")
user2.increment_login_attempts()
print(user2.login_attempts)
user2.increment_login_attempts()
print(user2.login_attempts)
user2.reset_login_attempts()
print(user2.login_attempts)
user2.describe_user()
user2.greet_user()