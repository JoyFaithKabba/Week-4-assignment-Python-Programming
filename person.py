# Define the Person class
class Person:
    # Initialize the attributes for the Person class
    def __init__(self, name, age, gender):
        self.name = name  
        self.age = age    
        self.gender = gender  

    # Method to introduce the person
    def introduce(self):
        # Print a message introducing the person with their details
        print(f"Hello There! My name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Code to create an instance and call the introduce method
if __name__ == "__main__":
    # Create an instance of the Person class with specific details
    person = Person("Joy Faith Kabba", 24, "Female")
    # Call the introduce method to display the person's information
    person.introduce()
