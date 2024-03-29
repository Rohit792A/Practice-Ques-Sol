

class Training:
    def __init__(self, name, date, completed, instructors, participants):
        self.name = name
        self.date = date
        self.completed = completed
        self.instructors = instructors 
        self.participants = participants 

    def view_details(self):
        print(f"Name: {self.name}, Date: {self.date}, Completed: {self.completed}")
        
        for instructor in self.instructors:
            print(f"Instructor Name: {instructor.name}, Website: {instructor.website}")
        for participant in self.participants:
            print(f"Participant Name: {participant.name}, Email: {participant.email}")

    
class Instructor:
    def __init__(self, name, website):
        self.name = name
        self.website = website
        

    
class Participants:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        

# Create instances of Instructors and Participants
instruc1 = Instructor("Rohan", "google meet")
instruc2 = Instructor("Rishabh", "Zoom")
part1 = Participants("Shubham", "shu@mail.com")
part2 = Participants("Ritika", "rit@mail.com")

# Create a Training instance with multiple instructors and participants

training1 = Training("Python", "April 19, 2024", True, [instruc1, instruc2], [part1, part2])
training2 = Training("Java", "April 12, 2024", True, [instruc1], [ part2])

# View the details of the training sessions
training1.view_details()
training2.view_details()
