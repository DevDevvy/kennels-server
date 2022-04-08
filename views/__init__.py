# this file is the bridge between the views requests and the request_handler
from .animal_requests import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal, get_animals_by_location, get_animals_by_status
from .location_requests import get_single_location, get_all_locations, create_location, update_location
from .employee_requests import  get_single_employee, get_all_employees, create_employee, delete_employee, update_employee, get_employees_by_location
from .customer_requests import get_single_customer, get_all_customers, create_customer, delete_customer, update_customer, get_customers_by_email