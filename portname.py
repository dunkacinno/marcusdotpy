import re

def cust_port():
	pass

def transit_port():
	pass

def peering_port():
	pass

def core_port():
	pass
    
def server_port():
	pass

def main():
	print('''
Observium will recognise the usage of ports as customer ports, transit, etc for display purposes using a standardised interface description format.

Cust: Acme CO [1Mb] (RR001RU36 DC3924) {DIA\999-999-9999}
 ^     ^      ^       ^                   ^
 |Serv |Cust  |Speed  |Note               |WW Circuit
The identifier before the colon defines the type of service, recognised types are :
Identifier :	Description
Cust :	Customer
Transit :	Transit link
Peering :	Peering link
Core :	Infrastructure link (non-customer)
Server : 	Server link (non-customer)

	   ''')
	#service_type = input("Delare Service Type:")
	service_speed = input("Declare Windwave Service Speed:")
	customer = input("Declare Customer:")
	note = input("Declare Note:")
	circuit = input("Declare Windwave Circuit:")
	cust_output = f"Cust:{customer} [{service_speed}] ({note}) {{{circuit}}}"
	print(cust_output)
	
main()