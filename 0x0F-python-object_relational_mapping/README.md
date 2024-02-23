# Project Name
0x0F. Python - Object-relational mapping
## Description
This project is a collection of Python scripts that interact with a MySQL database using the SQLAlchemy library. The scripts perform various tasks such as querying and modifying data in the database.

## Requirements
- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- pycodestyle version 2.8.*

## Installation
1. Clone the repository:  `git clone https://github.com/username/repo.git` 
2. Install the required packages:  `pip install -r requirements.txt` 
3. Set up the MySQL database and configure the connection settings in the scripts.

## Usage
1. Execute the scripts using the command:  `python script_name.py [mysql_username] [mysql_password] [database_name] [additional_arguments]` 

## Scripts
1. **0-select_states.py**: Lists all states from the database hbtn_0e_0_usa.
2. **1-filter_states.py**: Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.
3. **2-my_filter_states.py**: Lists all states from the database hbtn_0e_0_usa where the name matches the provided argument.
4. **3-my_safe_filter_states.py**: Lists all states from the database hbtn_0e_0_usa where the name matches the provided argument. This script is safe from SQL injections.
5. **4-cities_by_state.py**: Lists all cities from the database hbtn_0e_4_usa.
6. **5-filter_cities.py**: Lists all cities of a specific state from the database hbtn_0e_4_usa.
7. **6-model_state.py**: Defines the State class and creates the states table in the database hbtn_0e_6_usa.
8. **7-model_state_fetch_all.py**: Lists all State objects from the database hbtn_0e_6_usa.
9. **8-model_state_fetch_first.py**: Prints the first State object from the database hbtn_0e_6_usa.
10. **9-model_state_filter_a.py**: Lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa.
11. **10-model_state_my_get.py**: Prints the State object with the provided name from the database hbtn_0e_6_usa.
12. **11-model_state_insert.py**: Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
13. **12-model_state_update_id_2.py**: Changes the name of the State object with id 2 to "New Mexico" in the database hbtn_0e_6_usa.
14. **13-model_state_delete_a.py**: Deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
15. **model_city.py**: Defines the City class.
16. **14-model_city_fetch_by_state.py**: Prints all City objects from the database hbtn_0e_14_usa, grouped by state.

## Credits
This project was created by Marcia 
