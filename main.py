contacts = []

person_name = input('Name: ')
person_surname = input('Surname: ')
person_phone = input('Phone: ')
person_email = input('Email: ')

person_contact = {
    'Name': person_name,
    'Surname': person_surname,
    'Phone': person_phone,
    'Email': person_email
}

contacts.append(person_contact)
print(contacts)
