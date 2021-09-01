# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 17:58:58 2021

@author: jt108
"""

def print_goals():
    print('1. Print list of names')
    print('2. Enter a name')
    print('3. Quit')
    print()


names = ['Craig', 'Danh', 'David', 'Evan', 'Gideon', 'Grant', 'Jackson', 'JacobH', 'JacobT', 'Josue', 'Madeline', 'Morgan', 'Nick']
numbers = {}
menu_choice = 0
print_goals()


while menu_choice != 3:
    menu_choice = int(input("\n\nType in a number (1-3): "))
    if menu_choice == 1:
        print("\nList of names: ", names)

    elif menu_choice == 2:
        print("Enter a name from the list")
        name = input("Name: ")
        
        if(name != "Craig" or "Danh"):
            print("Name not in list, try again")
        
        if(name == 'Gideon'):
            print("As far as this class is concerned, success for me will be to successfully achieve the goals of this class, which are to be conversant with software development concepts and practically being able to apply what I have learned in the real world, and of course, to pass with flying colors ")
    
    
        elif(name == 'JacobH'):
            print("In this class, I would like to become more confident with the software development process. I want to gain proficiency in timing my tasks and better judging how to divide up my work. I want to develop good actionable tasks with clear success criteria. Additionally, I want to increase my teamwork and communication skills. I would also like to get better at testing my programs. In the end, I would like to just be overall better and more confident in my work")
    
    
        elif(name == 'JacobT'):
            print('I hope to learn a bunch of new skills and information and apply that knowledge into future circumstances. Also, I wish to not stress out over the class if I am confused on something I don’t know.')
    
    
        elif(name == 'Grant'):
            print('By the end of the semester, I hope to understand all the topics that were covered in the class and expand my knowledge and skills in software development and coding so I can be prepared to be successful as I go on in my major and onto a career.')
            
    
        elif(name == 'Craig'):
            print('I want to learn more about the software development process and gain more confidence in my programming abilities. I would also like to continue to work on my problem-solving and time management skills. After this course, I want to be able to create, maintain, and improve personal projects that I will feel proud of.')
    
    
        elif(name == 'Morgan'):
            print('I want to gain a basic understanding of what Sofware development is, how softwares differ from each other and when to use a certain software and be able to compare it to Data Science. I learned this summer that as a Data Scientist it is important to know a little about each role on your team so this class will help me in the future when teamwork is needed!  ')
    
    
        elif(name == 'Evan'):
            print('I want to gain a broad understanding of software development, learn how it is implemented in the real world, and learn how it can be applied in the field of data analytics. In addition to this, I aim to gain programming experience and improve upon soft skills such as communication and working as a member of a team.')
    
    
        elif(name == 'David'):
            print('I am auditing this course to learn something I may not know, expand on, or enhance, some things I think I may know and get new perspectives by looking at things from other points of view.')
    
    
        elif(name == 'Madeline'):
            print('I want to build up my team working and communication skills. I also want to be able to use what I have learned from this class in interviews and future careers')
    
    
        elif(name == 'Jackson'):
            print('to be able to write the most basic software, not giving up when solving problems especially when it come to writing code, improve teamwork and communication between each other and be able to define and breaking down tasks into subtasks to help me understand it better, to do it better.')
    
    
        elif(name == 'Danh'):
            print('I expect to learn about SDLC and the frameworks that support it and its phases and to improve my soft skills for software development process')
    
    
        elif(name == 'Josue'):
            print('I want to be able to write software at the end of this semester. I also want to learn new things about software that I do not currently know, like what languages are easy to use to write software. This semester, there are some classes that I am taking because I have to take them or to bring up my credits to full time. This class will help me decide what I want to do with my computer science major after graduation. In some other classes I see success as getting passing grades but in this class success expanding my knowledge and helping decide what I want to do in the future.')
    
    
        elif(name == 'Nick'):
            print('Learn to independently develop a basic program, apply myself, and meet one other person')
        
             
    elif menu_choice == 3:
        break