
class Room :
    def __init__(self, room_id, capicity,status,room_type,rent):
        self.room_id = room_id
        self.capicity = capicity
        self.status = status
        self.room_type = room_type
        self.rent = rent
        
class Customer :
    def __init__(self, id, fullname,age,address,phonenumber,checkin_date,checkout_date,nationality,payment,room_id,national_id,email,reservation_status):
        self.id = id
        self.fullname = fullname
        self.age = age
        self.address = address
        self.phonenumber = phonenumber
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.nationality = nationality
        self.payment = payment
        self.room_id = room_id
        self.national_id = national_id
        self.email = email
        self.reservation_status = reservation_status
        
    def Print(self):
        print(f"Id : {self.id}")
        print(f"Name : {self.fullname}")
        print(f"Age : {self.age}")
        print(f"Address : {self.address}")
        print(f"Phonenumber : {self.phonenumber}")
        print(f"Checkin_date : {self.checkin_date}")
        print(f"checkout_date : {self.checkout_date}")
        print(f"Nationality : {self.nationality}")
        print(f"Payment : {self.payment}")
        print(f"Room Id : {self.room_id}")
        print(f"National Id : {self.national_id}")
        print(f"Email : {self.email}")
        print(f"Reservation Status : {self.reservation_status}")

