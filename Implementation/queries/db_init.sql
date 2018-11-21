CREATE TABLE IF NOT EXISTS `workshop_repaired_car` (
	`wid`	INTEGER NOT NULL,
	`plate`	VARCHAR ( 10 ) NOT NULL,
	`pname`	VARCHAR ( 50 ) NOT NULL,
	`start_time`	DATE NOT NULL,
	`duration`	INTEGER NOT NULL,
	`pcount`	INTEGER NOT NULL,
	PRIMARY KEY(`wid`),
	FOREIGN KEY(`plate`) REFERENCES `car`(`plate`),
	FOREIGN KEY(`pname`) REFERENCES `car_part`(`name`)
);
CREATE TABLE IF NOT EXISTS `workshop` (
	`wid`	int NOT NULL,
	`availability` VARCHAR( 50 ) NOT NULL,
	`location`	VARCHAR ( 50 ) NOT NULL,
	PRIMARY KEY(`wid`)
);
CREATE TABLE IF NOT EXISTS `customer_uses_car` (
	`uid`	INTEGER NOT NULL,
	`type`	INTEGER NOT NULL,
	`customer`	VARCHAR ( 20 ) NOT NULL,
	`car`	VARCHAR ( 20 ) NOT NULL,
	`destination`	INTEGER,
	`distance`	INTEGER NOT NULL,
	`start_time`	DATE NOT NULL,
	`duration`	INTEGER NOT NULL,
	`cost`	INTEGER,
	PRIMARY KEY(`uid`),
	FOREIGN KEY(`car`) REFERENCES `car`(`plate`),
	FOREIGN KEY(`customer`) REFERENCES `customer`(`username`)
);
CREATE TABLE IF NOT EXISTS `customer` (
	`fullname`	VARCHAR ( 50 ) NOT NULL,
	`username`	VARCHAR ( 50 ) NOT NULL,
	`address`	VARCHAR ( 256 ) NOT NULL,
	`phone`	VARCHAR ( 20 ) NOT NULL,
	`email`	VARCHAR ( 256 ) NOT NULL,
	PRIMARY KEY(`username`)
);
CREATE TABLE IF NOT EXISTS `charging_station` (
	`sid`	int NOT NULL,
	`location`	VARCHAR ( 20 ) NOT NULL,
	`soc_shape`	VARCHAR ( 20 ) NOT NULL,
	`soc_size`	VARCHAR ( 20 ) NOT NULL,
	`soc_count`	INTEGER NOT NULL,
	`cost`	int NOT NULL,
	`charging_time`	INTEGER NOT NULL,
	PRIMARY KEY(`sid`)
);
CREATE TABLE IF NOT EXISTS `car_uses_charging_station` (
	`plate`	VARCHAR ( 20 ) NOT NULL,
	`sid`	INTEGER NOT NULL,
	`start_time`	DATE NOT NULL,
	PRIMARY KEY(`plate`,`sid`,`start_time`),
	FOREIGN KEY(`plate`) REFERENCES `car`(`plate`),
	FOREIGN KEY(`sid`) REFERENCES `charging_station`(`sid`)
);
CREATE TABLE IF NOT EXISTS `car_parts_provider` (
	`pid`	int NOT NULL,
	`name`	VARCHAR ( 20 ) NOT NULL,
	`phone`	VARCHAR ( 20 ) NOT NULL,
	`address`	VARCHAR ( 20 ) NOT NULL,
	PRIMARY KEY(`pid`)
);
CREATE TABLE IF NOT EXISTS `car_part_used_in_car` (
	`pname`	VARCHAR ( 50 ) NOT NULL,
	`plate`	VARCHAR ( 10 ) NOT NULL,
	FOREIGN KEY(`pname`) REFERENCES `car_part`(`name`),
	FOREIGN KEY(`plate`) REFERENCES `car`(`plate`),
	PRIMARY KEY(`plate`,`pname`)
);
CREATE TABLE IF NOT EXISTS `car_part_provided_by` (
	`pname`	VARCHAR ( 50 ) NOT NULL,
	`prid`	int NOT NULL,
	FOREIGN KEY(`pname`) REFERENCES `car_part`(`name`),
	FOREIGN KEY(`prid`) REFERENCES `car_parts_provider`(`pid`),
	PRIMARY KEY(`prid`,`pname`)
);
CREATE TABLE IF NOT EXISTS `car_part_available_in_workshop` (
	`pname`	VARCHAR ( 50 ) NOT NULL,
	`wid`	int NOT NULL,
	FOREIGN KEY(`pname`) REFERENCES `car_part`(`name`),
	FOREIGN KEY(`wid`) REFERENCES `workshop`(`wid`),
	PRIMARY KEY(`wid`,`pname`)
);
CREATE TABLE IF NOT EXISTS `car_part` (
	`name`	VARCHAR ( 50 ) NOT NULL,
	`price`	MONEY NOT NULL,
	`ptype`	VARCHAR ( 50 ) NOT NULL,
	PRIMARY KEY(`name`)
);
CREATE TABLE IF NOT EXISTS `car` (
	`plate`	VARCHAR ( 20 ) NOT NULL,
	`battery_charge`	INTEGER NOT NULL,
	`location`	VARCHAR ( 100 ) NOT NULL,
	`type`	DATE NOT NULL,
	`color`	VARCHAR ( 10 ),
	PRIMARY KEY(`plate`)
);