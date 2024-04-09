name = {'lastname':'Harvey', 'firstname':'Steve'}
student = {'name':name, 'phone': '416-555-1212', 'student_no':'1126804'}

print(student['name']['lastname'])

address = {'steet': '123 Sesame St','city':'Toronto', 'Province':'ON', 'Postal':'M3B3H7'}
print(address['steet'])
address = {'street': '123 Sesame St','city':'Toronto', 'Province':'ON', 'Postal':'M3B3H7'}
print(address['street'])
print(address['city'])
print(f'{address['Province']}, {address['Postal']}')

      