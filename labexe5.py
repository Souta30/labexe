import queue

def register_patient(patient_queue):
    patient_name = input("Enter the patient's name to register: ")
    patient_queue.put(patient_name)
    print(f"Patient '{patient_name}' registered successfully.")

def remove_patient(patient_queue):
    if patient_queue.empty():
        print("No patients in the queue.")
    else:
        patient_name = patient_queue.get()
        print(f"Patient '{patient_name}' has met the doctor and is removed from the queue.")

def display_patient_queue(patient_queue):
    if patient_queue.empty():
        print("No patients in the queue.")
    else:
        print("Current patient queue:")
        for i, patient in enumerate(list(patient_queue.queue)):
            print(f"{i+1}. {patient}")

def main():
    patient_queue = queue.Queue()
    
    while True:
        print("\nMenu:")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            register_patient(patient_queue)
        elif choice == 2:
            remove_patient(patient_queue)
        elif choice == 3:
            display_patient_queue(patient_queue)
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
