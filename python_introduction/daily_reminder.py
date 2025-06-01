#Python Personal Daily Reminder

#Prompt user for a single task, priority, and time_bound
task = input("Enter your task: ").capitalize()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

#Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        priority = "high"
    case "medium":
        priority = "medium"
    case "low":
        priority = "low"
        
#Provide a Customized Reminder:
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
elif time_bound == "no":
    print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
else:
    print("Invalid time bound value")