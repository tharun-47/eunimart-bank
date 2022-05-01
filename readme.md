[Main.py](https://github.com/tharun-47/eunimart-bank/blob/main/main.py) is the python rest API file made using flask framework 
[index.html](https://github.com/tharun-47/eunimart-bank/blob/main/index.html) is the signup up page and [createaccount.html](https://github.com/tharun-47/eunimart-bank/blob/main/create%20account.html) is to create new bank account , 
I have used postgres for database and I created a relational database with the schema given below



CREATE TABLE account_holder (
	country_code VARCHAR(10) NOT NULL,
	mobile_num VARCHAR(10) PRIMARY KEY NOT NULL,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20),
	father_name VARCHAR(40) NOT NULL,
	dob DATE NOT NULL,
	permanent_address VARCHAR(100) NOT NULL,
	current_address VARCHAR(100) NOT NULL,
	account_num VARCHAR(15) NOT NULL,
	pin VARCHAR(6) NOT NULL
);
