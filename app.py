print("Employee Leave Managment System")

leaveBalance = 2

def applyLeave():
    if leaveBalance <= 0:
        print("Leave Balance: 0")
        print("Cannot apply for leave")
    else:
        print(f"Leave Balance: {leaveBalance}")
        print("Application for leave submitted")
