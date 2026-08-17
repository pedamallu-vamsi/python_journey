def take_input(n):
    sessions = []
    for i in range(n):
        subject = input(f"Enter the subject you studied in session {i+1} : ")
        hours = int(input(f"Enter the no.of hours you studied in session {i+1} : "))
        problems = int(input(f"Enter the no.of problems you studied in session {i+1} : "))
        dictionary = {
            "subject" : subject,
            "hours" : hours,
            "problems" : problems
        }
        sessions.append(dictionary)
    return sessions

def total_study(sessions):
    total = 0
    for x in sessions:
        total += x['hours']
    return total

def total_problems(sessions):
    total = 0
    for x in sessions:
        total += x['problems']
    return total

def average_study_hours(sessions):
    total = total_study(sessions)
    return total/len(sessions)

def most_productive(sessions):
    max = sessions[0]['problems']+sessions[0]['hours']
    session = 1
    count = 0

    for x in sessions:
        count+=1
        if max < x['problems']+x['hours']:
            max = x['problems']+x['hours']
            session = count
    return session

def most_study_time(sessions):
    hrs = 0
    subject = ""
    for x in sessions:
        if x['hours'] > hrs:
            hrs = x['hours']
            subject = x['subject']
    return subject

n = int(input("Enter the no.of study sessions : "))
sessions = take_input(n)
print(f"The total no.of hours studied was {total_study(sessions)}")
print(f"The total no.of problems solved was {total_problems(sessions)}")
print(f"The total average study hours per session was {average_study_hours(sessions)}")
print(f"The total most productive session was {most_productive(sessions)}")
print(f"The subject that was given the most study time was {most_study_time(sessions)} session")