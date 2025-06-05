# 🚀  Time Registeration System

## The main goal of the Time Registration System is to:
- Provide a digital platform for companies to manage project-based work by tracking time,assigningemployees, and generating invoices — all in one backend system.

## This system should:
   - Help employers monitor work hours, track budgets, and bill customers efficiently.
   - Help employees log their working hours in a structured way.
   - Let customers view invoices and see project summaries.

#  Target Users:
## * Employers
-    Can manage projects, employees, customers
-    Can track and modify time blocks
-    Can view and edit invoices
-    Can assign employees and set project budgets

## * Employees
-    Can log hours per project (with notes)
-    Can see their own time entries

## * Customers
-    Can see invoices for projects
-    Can see a summary/status of projects they are involved in

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
## Time Registration System Functuional Requirement:
- Employers can register, log in.
- Employers can add customers with details.
- Employers can create and manage projects per customer (with start/end dates).
- Employers can register employees in the system.
- Employers can assign employees to specific projects.
- Employers can view and modify registered time blocks.
- Employers can generate and edit invoices per project.
- Employers can set and track project budgets.
- Employees can be added by employers.
- Employees can log time worked on projects using a calendar interface.
- Employees can add details/notes to time blocks.
- Customers can view invoices.
- Customers can see limited details about ongoing projects (e.g., current status, summary info).
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
```
## This our Folder Structure:
Time_Registration_System/
├──router/
|   └──employee.py
├──schemas/
|   ├──auth.py
|   ├──customer.py
|   ├──invoices.py
|   ├──projects.py
|   ├──timeblock.py
|   └──user.py
├──main.py
├── README.md
└──requirements.txt
```