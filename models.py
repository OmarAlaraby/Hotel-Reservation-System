
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
        