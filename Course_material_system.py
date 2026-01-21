materials = []

def add_material():
    course = input("Enter course name: ")
    title = input("Enter material title: ")
    materials.append({"course": course, "title": title})
    print("Material added successfully")

def view_materials():
    if not materials:
        print("No materials available")
    else:
        for material in materials:
            print(material["course"], "-", material["title"])

def main():
    while True:
        print("1. Add Material")
        print("2. View Materials")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_material()
        elif choice == "2":
            view_materials()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
