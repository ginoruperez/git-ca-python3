# This program uses class Patient and Procedure.  
# It display the patient's person information and 3 procedures made for the patient

import patient 

# The main function 
def main():

    # Create an instance of class Patient
    patient_data = patient.Patient('Felipe', 'Morales', 'Rodriguez',
                                   '145 Park Square, Castleknock', 'Dublin 15', 'W12E34',
                                   '+353826587241', 'Mary Joy Morales', '+353895243591')

    # Create 3 instances of class Procedure

    procedure1 = patient.Procedure('Physical Exam', '15/09/2021', 'Dr. Jones', 300)

    procedure2 = patient.Procedure('X-Ray', '15/09/2021', 'Dr. Ryan', 600)

    procedure3 = patient.Procedure('Blood Test', '15/09/2021', 'Dr. Smith', 100)

    # Print the patient info
    print('Patient Information : ')
    print('----------------------')
    print(patient_data)
    print()

    # Print patient's operation procedures 
    print('Patient undergone the following procedures : ')
    print('---------------------------------------------')
    print('Procedure #1')
    print(procedure1)
    print()

    print('Procedure #2')
    print(procedure2)
    print()

    print('Procedure #3')
    print(procedure3)
    print()

    # Print the total charges of 3 procedures made
    # Format the number with comma when total charges is >= to 1000 Euro and format with 2 decimal places
    print('TOTAL CHARGES : €', '{:,.2f}'.format(procedure1.get_charge_fee() + 
                                        procedure2.get_charge_fee() +
                                        procedure3.get_charge_fee()))

      
# Call the main function
main()



                                   