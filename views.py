from models import Customer , Room

# ['name', 'age' ,'address' , 'phone', 'checkin_date' , 'checkout_date', 'nationality', 'payment' , 'room_id' , 'national_id' , 'email' , 'reservation_status']
# --------------- add new Customer ----------------- #

def Get_Available_Room():
    with open('data_files/Rooms.txt' , 'r') as RoomsData:
        rooms = RoomsData.readlines()
    
    room_id = 0
    for i ,room in enumerate(rooms):
        data = list(eval(room))
        
        room_id = -1
        if data[1] == 'available':
            room_id = data[0]
            data[1] = 'unavailable'
            rooms[i] = str(data) + '\n'
            
            with open('data_files/Rooms.txt' , 'w') as RoomsData:
                for room in rooms:
                    RoomsData.write(room)
            break
    return room_id


def get_ID():
    with open('data_files/Id.txt' , 'r') as IdFile:
        id = IdFile.readline()
    
    new_id = id
    id = int(id) + 1
    
    with open('data_files/Id.txt' , 'w') as IdFile:
        IdFile.write(str(id))
    
    return new_id

def add_new_customer():
    data = []
    data.append(get_ID())
    data.append(input('name : '))
    data.append(input('age : '))
    data.append(input('address : '))
    data.append(input('phone : '))
    data.append(input('checkin_date : '))
    data.append(input('checkout_date : '))
    data.append(input('nationality : '))
    data.append(input('payment : '))
    data.append(Get_Available_Room())
    data.append(input('national_id : '))
    data.append(input('email : '))
    data.append(input('reservation_status : '))
    
    with open('data_files/Customers.txt' , 'a', newline='') as file:
        file.write(str(data) + '\n')



# ------------------ search ------------------ %

def search_with(id):
    with open('data_files/Customers.txt' , 'r') as Customers:
        data = Customers.readlines()
        
        for customer in data:
            check = list(eval(customer))
            if check[0] == id:
                return check
            
    return 'Not Found'
    
            


def Get_Customer():
    id = input('ID : ')
    return search_with(id)


# ----------------- update cutsomer ------------ $


def save_data(customer):
    with open('data_files/Customers.txt' , 'r') as Customers_file:
        data = Customers_file.readlines()
        for i , line in enumerate(data):
            line = list(eval(line))
            
            if line[0] == str(customer[0]):
                line[1] = customer[1]
                line[2] = customer[2]
                data[i] = line
                print('Data Saved')
                break
            
    with open('data_files/Customers.txt' , 'w') as Customers_file:
        for line in data:
            Customers_file.write('\n' + str(line) + '\n')


def update_customer():
    
    customer = 'Not Found'
    first_loop = True
    
    while customer == 'Not Found':
        if not first_loop:
            print(f'Customer with id = {customer_id} NOT FOUND ! ')
            
        customer_id = input('Customer Id : ')
        customer = search_with(customer_id)
        first_loop = False
    
    print(customer)

    new_name = input('New Name : ')
    customer[1] = new_name
    new_age = input('New Age : ')
    customer[2] = new_age
        
    save_data(customer)
    

# ----------------- Delete Customer ---------- #

def delete_Customer():
    customer = 'Not Found'
    first_loop = True
    
    while customer == 'Not Found':
        if not first_loop:
            print(f'Customer with id = {customer_id} NOT FOUND ! ')
            
        customer_id = input('Customer Id : ')
        customer = search_with(customer_id)
        first_loop = False
        
    with open('data_files/Customers.txt' , 'r') as Customers_file:
        data = Customers_file.readlines()
        for i , line in enumerate(data):
            line = list(eval(line))
            
            if line[0] == str(customer[0]):
                data.pop(i)
                print('Customer Deleted')
                break
            
    with open('data_files/Customers.txt' , 'w') as Customers_file:
        for line in data:
            Customers_file.write(str(line))


# ---------------- view customers ------------- #

def view_all_customers():
    with open('data_files/Customers.txt', 'r') as Customers_file:
        data = Customers_file.readlines()
        for line in data:
            print(line)

# ----------------- view rooms --------------- #

def View_All_rooms():
    with open('data_files/Rooms.txt' , 'r') as RoomsData:
        rooms = RoomsData.readlines()
    
    for room in rooms:
        print(room)

# ----------------- show all customers --------------- #

def Print_Single_Customer(C):
    All_Date = []
    curr = ""
    for idx in range(1, len(C) - 1):
        if (C[idx] == ',' or C[idx] == ' '):
            continue
        elif (C[idx] == "'"):
            if (len(curr) > 0):
                All_Date.append(curr)
                curr = ""
            else:
                continue
        else:
            curr+= C[idx]

    newC = Customer(All_Date[0], All_Date[1], All_Date[2], All_Date[3], All_Date[4], All_Date[5], All_Date[6], All_Date[7], All_Date[8], All_Date[9], All_Date[10], All_Date[11], All_Date[12])

    newC.Print()

def show_all_customers():
    Customers_File = open("data_files/Customers.txt", "r")
    All_Customers = Customers_File.readlines()
    for idx in range(len(All_Customers)):
        print(f"                   Customer {idx+1} To Be Printed")
        Print_Single_Customer(All_Customers[idx])
        print("=====================================================================\n")

    Customers_File.close()


# ------------------ main -------------------- #

def main():
    
    # choose the operation type
    print('1- Add new customer')
    print('2- search for customer')
    print('3- update customer')
    print('4- delete customer')
    print('5- show all customers')
    print('6- view Rooms')
  
    print('7- show all available rooms')
    print('8- show all reserved rooms')
    print('10- show hotel data')
    
    operation = input('which operation you want to do ? \n')
    
    if operation == '1':
        add_new_customer()
    elif operation == '2':
        print(Get_Customer())
    elif operation == '3':
        update_customer()
    elif operation == '4':
        delete_Customer()
    elif operation == '5':
        show_all_customers()
    elif operation == '6':
        View_All_rooms()
    # elif operation == '7':
    #     show_all_available_rooms()
    # elif operation == '8':
    #     show_all_reserved_rooms()
    # elif operation == '10':
    #     show_hotel_data()
    else:
        raise KeyError('Invalid Type')


if __name__ == '__main__':
    main()