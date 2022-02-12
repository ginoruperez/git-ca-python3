# This python file contains two classes namely Patient class and Procedure class

# The class Patient holds the personal information of a patient
# Information includes the following 
# First Name, Middle Name and Last Name
# Address, City, ZIP Code
# Phone Number
# Name and Phone Number of Emergency contact

class Patient:

    # The __init__ initializes the class attributes

    def __init__(self,first_name, middle_name, last_name, address, city, zip_code, 
                 phone_number, name_econtact, phone_econtact):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__zip_code = zip_code
        self.__phone_number = phone_number
        self.__name_econtact = name_econtact
        self.__phone_econtact = phone_econtact

    # Create the Mutators

    # The set_first_name method accepts an argument for Patient's first name
    def set_first_name(self, first_name):
        self.__first_name = first_name

    # # The set_middle_name method accepts an argument for Patient's middle name
    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    # The set_last_name method accepts an argument for Patient's last name
    def set_last_name(self, last_name):
        self.__last_name = last_name

    # The set_address method accepts an argument for Patient's address
    def set_address(self, address):
        self.__address = address

    # The set_city method accepts an argument for Patient's city 
    def set_city(self, city):
        self.__city = city

    # The set_zip_code method accepts an argument for Patient's zip code
    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    # The set_phone_number method accepts an argument for Patient's phone number
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    # The set_name_econtact method accepts an argument for Patient's Emergency contact person name
    def set_name_econtact(self, name_econtact):
        self.__name_econtact = name_econtact

    # The set_phone_econtact method accepts an argument for Patient's Emergency contact person phone number
    def set_phone_econtact(self, phone_econtact):
        self.__phone_econtact = phone_econtact

    
    # Create the Accessors

    # The get_first_name method returns the patient's first name
    def get_first_name(self):
        return self.__first_name

    # The get_middle_name method returns the patient's middle name
    def get_middle_name(self):
        return self.__middle_name

    # The get_last_name method returns the patient's last name
    def get_last_name(self):
        return self.__last_name

    # The get_address method returns the patient's address
    def get_address(self):
        return self.__address

    # The get_city method returns the patient's city 
    def get_city(self):
        return self.__city

    # The get_zip_code method returns the patient's zip code
    def get_zip_code(self):
        return self.__zip_code

    # The get_phone_number method returns the patient's phone number
    def get_phone_number(self):
        return self.__phone_number

    # The get_name_econtact method returns the patient's emergency contact person name
    def get_name_econtact(self):
        return self.__name_econtact

    # The get_phone_econtact method returns the patient's emergency contact person phone number
    def get_phone_econtact(self):
        return self.__phone_econtact

    # The __str__ method returns a string 
    # indicating the object's state 
    # The __str__ method is defined in a way that is easy to read 
    # and outputs all the members of the class

    def __str__(self):
        
        result = ' First Name : '+ self.get_first_name() + \
            '\n Middle Name : '+ self.get_middle_name() + \
            '\n Last Name : '+ self.get_last_name() + \
            '\n Address : '+ self.get_address() + \
            '\n City : '+ self.get_city() + \
            '\n ZIP Code : '+ self.get_zip_code() + \
            '\n Phone Number : '+ self.get_phone_number() + \
            '\n Name of Emergency contact : '+ self.get_name_econtact() + \
            '\n Phone No. of Emergency contact : '+ self.get_phone_econtact() \
        
        return result


# The class Procedure, it holds the procedure information undergone by patient
# Information are as follows
# Name of Procedure
# Date of procedure
# Name of the Doctor who performed the procedure
# Charges for the procedure

class Procedure:

    # The __init__ initializes the class attributes

    def __init__(self, procedure_name, procedure_date, doctor_name, charge_fee):
        self.__procedure_name = procedure_name
        self.__procedure_date = procedure_date
        self.__doctor_name = doctor_name
        self.__charge_fee = charge_fee

    # Create the mutators

    # The set_procedure_name method accepts an argument for the name of procedure
    def set_procedure_name(self, procedure_name):
        self.__procedure_name = procedure_name

    # The set_procedure_date method accepts an argument for the date of procedure
    def set_procedure_date(self, procedure_date):
        self.__procedure_date = procedure_date

    # The set_doctor_name method accepts an argument for the name
    # of Doctor who performed the procedure
    def set_doctor_name(self, doctor_name):
        self.__doctor_name = doctor_name

    # The set_charge_fee method accepts an argument for the charges of the procedure
    def set_charge_fee(self, charge_fee):
        self.__charge_fee


    # Create Accessors

    # The get_procedure_name method returns the name of the procedure
    def get_procedure_name(self):
        return self.__procedure_name

    # The get_procedure_date method returns the date of the procedure
    def get_procedure_date(self):
        return self.__procedure_date

    # The get_doctor_name method returns the name of the Doctor 
    # who performed the procedure
    def get_doctor_name(self):
        return self.__doctor_name

    # The get_charge_fee method returns the charges for the procedure
    def get_charge_fee(self):
        return self.__charge_fee

    # The __str__ method returns a string 
    # indicating the object's state 
    # The __str__ method is defined in a way that is easy to read 
    # and outputs all the members of the class

    def __str__(self):

        result = ' Procedure Name : '+ self.get_procedure_name() + \
            '\n Date : '+ self.get_procedure_date() + \
            '\n Doctor : '+ self.get_doctor_name() + \
            '\n Charge : €'+ str(format(self.get_charge_fee(),'.2f') )

        return result
    





