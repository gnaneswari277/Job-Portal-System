# Job Portal System

jobs = []
applications = []


def post_job():
    print("\n===== POST A JOB =====")

    company = input("Enter company name: ")
    title = input("Enter job title: ")
    location = input("Enter job location: ")
    salary = input("Enter salary: ")
    skills = input("Enter required skills: ")

    job = {
        "Company": company,
        "Title": title,
        "Location": location,
        "Salary": salary,
        "Skills": skills
    }

    jobs.append(job)

    print("\nJob posted successfully! ✅")


def view_jobs():
    print("\n===== AVAILABLE JOBS =====")

    if not jobs:
        print("No jobs available.")
        return

    for i, job in enumerate(jobs, start=1):
        print(f"\nJob {i}")
        print("Company  :", job["Company"])
        print("Title    :", job["Title"])
        print("Location :", job["Location"])
        print("Salary   :", job["Salary"])
        print("Skills   :", job["Skills"])


def search_jobs():
    print("\n===== SEARCH JOBS =====")

    keyword = input("Enter job title or skill: ").lower()

    found = False

    for job in jobs:
        if (keyword in job["Title"].lower()
                or keyword in job["Skills"].lower()):
            print("\nJob Found ✅")
            print("Company  :", job["Company"])
            print("Title    :", job["Title"])
            print("Location :", job["Location"])
            print("Salary   :", job["Salary"])
            print("Skills   :", job["Skills"])
            found = True

    if not found:
        print("No matching jobs found.")


def apply_job():
    print("\n===== APPLY FOR A JOB =====")

    if not jobs:
        print("No jobs available.")
        return

    view_jobs()

    try:
        job_number = int(input("\nEnter job number: "))

        if job_number < 1 or job_number > len(jobs):
            print("Invalid job number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    name = input("Enter applicant name: ")
    email = input("Enter email: ")

    application = {
        "Applicant": name,
        "Email": email,
        "Job": jobs[job_number - 1]["Title"],
        "Company": jobs[job_number - 1]["Company"]
    }

    applications.append(application)

    print("\nApplication submitted successfully! ✅")


def view_applications():
    print("\n===== JOB APPLICATIONS =====")

    if not applications:
        print("No applications found.")
        return

    for i, application in enumerate(applications, start=1):
        print(f"\nApplication {i}")
        print("Applicant :", application["Applicant"])
        print("Email     :", application["Email"])
        print("Job       :", application["Job"])
        print("Company   :", application["Company"])


def main():
    while True:
        print("\n==============================")
        print("       JOB PORTAL SYSTEM")
        print("==============================")
        print("1. Post Job")
        print("2. View Jobs")
        print("3. Search Jobs")
        print("4. Apply for Job")
        print("5. View Applications")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            post_job()

        elif choice == "2":
            view_jobs()

        elif choice == "3":
            search_jobs()

        elif choice == "4":
            apply_job()

        elif choice == "5":
            view_applications()

        elif choice == "6":
            print("\nThank you for using the Job Portal System!")
            break

        else:
            print("Invalid choice. Please try again.")


main();
