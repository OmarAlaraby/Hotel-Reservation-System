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
    print('3- view Rooms')
    print('6- show all customers')
    print('7- show all available rooms')
    print('8- show all reserved rooms')
    print('10- show hotel data')
    
    operation = input('which operation you want to do ? \n')
    
    if operation == '1':
        add_new_customer()
    elif operation == '2':
        print(Get_Customer())
    elif operation == '3':
        View_All_rooms()
    elif operation == '6':
        show_all_customers()
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