#University class
class University:
  student:list = []
  department:list=[]

  def __init__(self,uni_name,uni_location):
    self.uni_name=uni_name
    self.uni_location=uni_location
    print(f"""___The University of {self.uni_name} has been established in {self.uni_location}___""")

#method to add student
  def add_student(self,studentinfo):
    self.studentinfo = studentinfo
    University.student.append(self.studentinfo)
    print(f"""A new student with name {studentinfo} has been enrolled""")

#method to add department
  def add_department(self,departmentinfo):
    self.departmentinfo = departmentinfo
    University.department.append(self.departmentinfo)
    print(f"""A new department {self.departmentinfo} has been established in {self.uni_name} in {self.uni_location} main campus""")

#create uni
u1=University("Applied AI university","Faisalabad")

#add student
u1.add_student("Ali")
u1.add_student("bilal")

#add department
u1.add_department("BI")
u1.add_department("Agri")

#list of student
print(University.student)

#list of departments
print(University.department)


#parent class
class Human:
  def __init__(self,name,age,gender):
    self.name=name
    self.age=age
    self.gender=gender

#student child class
class Student(Human):
  student_list:list=[]
  def __init__(self,name,age,gender,reg_no,degree):
    super().__init__(name,age,gender)
    self.reg_no=reg_no
    self.degree=degree
    self.student_list.append(self.name)
    self.student_list.append(self.age)
    self.student_list.append(self.gender)
    self.student_list.append(self.reg_no)
    self.student_list.append(self.degree)
    print(f"""the name of student is {self.name}, he is {self.age} years old. He is student of {self.degree} and his registration number is {self.reg_no}""")

#child class teacher
class Teacher(Human):
  teacher_list:list =[]
  def __init__(self,name,age,gender,emp_id,major):
    super().__init__(name,age,gender)
    self.emp_id = emp_id
    self.major = major
    self.teacher_list.append(self.name)
    self.teacher_list.append(self.age)
    self.teacher_list.append(self.gender)
    self.teacher_list.append(self.emp_id)
    self.teacher_list.append(self.major)
    print(f""" The name of teacher is{self.name},he is {self.age}years old his employee id{emp_id} and he is teacher of {self.major}""")

#student class obj
s1=Student("Noor",26,"male","ag5657","IT")
#teacher class obj
t1=Teacher("Mr Akbar",45,"male","emp98898","cs")
print(s1.student_list)
print(t1.teacher_list)

