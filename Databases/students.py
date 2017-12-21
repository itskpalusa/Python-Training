# import everything from peewee
from peewee import *
#The class from Peewee that lets us connect to an SQLite database
# make a database connection
# db is the variable and students is the name of the SqliteDatabase
db = SqliteDatabase('students.db')
#The Peewee class that we extend to make a model
class Student(Model):
    # attributes to hold on to
    username = CharField(max_length=255, unique=True)
    #CharField - A Peewee field that holds onto characters. It's a varchar in SQL terms
        #max_length - The maximum number of characters in a CharField
    points = IntegerField(default=0)
    #An IntegerField is a Peewee field that holds an integer

    #add a meta class
    class Meta:
        # set the database attribute equal to db.
        database = db

#list of dictionaries for database w/ two keys and values
students = [
    {'username': 'karthikpalusa',
    'points': 97000},
    {'username': 'keneth',
    'points': 6000},
    {'username': 'josh',
    'points': 7200},
    {'username': 'jake',
    'points': 9000},
]

# functions to add to SqliteDatabase

def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                            points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()

# function to find top students
def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student

# using the code
# this is a common pattern for making code only run when the script is run and not when it's imported
if __name__ == '__main__':
    # connect to the database
    db.connect()
    # create a table
    # safe=True so to keep peewee stable
    db.create_tables([Student], safe=True)
    # call in dictionaries function
    add_students()
    print("Our top student right now is: {0.username}.".format(top_student()))
