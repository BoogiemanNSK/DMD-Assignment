BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `workshop_repaired_car` (
	`wid`	INTEGER NOT NULL,
	`plate`	VARCHAR ( 10 ) NOT NULL,
	`pname`	VARCHAR ( 50 ) NOT NULL,
	`start_time`	DATETIME NOT NULL,
	`duration`	INTEGER NOT NULL,
	FOREIGN KEY(`plate`) REFERENCES `car`(`plate`),
	PRIMARY KEY(`wid`,`plate`,`pname`,`start_time`),
	FOREIGN KEY(`pname`) REFERENCES `car_part`(`name`)
);
CREATE TABLE IF NOT EXISTS `workshop` (
	`wid`	INTEGER NOT NULL,
	`availability`	VARCHAR ( 50 ) NOT NULL,
	`location`	VARCHAR ( 50 ) NOT NULL,
	PRIMARY KEY(`wid`)
);
CREATE TABLE IF NOT EXISTS `customer_uses_car` (
	`uid`	INTEGER NOT NULL,
	`type`	VARCHAR ( 50 ) NOT NULL,
	`customer`	VARCHAR ( 50 ) NOT NULL,
	`car`	VARCHAR ( 50 ) NOT NULL,
	`destination`	VARCHAR ( 50 ),
	`distance`	INTEGER NOT NULL,
	`start_time`	DATETIME NOT NULL,
	`duration`	INTEGER NOT NULL,
	`cost`	INTEGER,
	PRIMARY KEY(`uid`),
	FOREIGN KEY(`car`) REFERENCES `car`(`plate`),
	FOREIGN KEY(`customer`) REFERENCES `customer`(`username`)
);
CREATE TABLE IF NOT EXISTS `customer` (
	`username`	VARCHAR ( 50 ) NOT NULL,
	`fullname`	VARCHAR ( 50 ) NOT NULL,
	`address`	VARCHAR ( 256 ) NOT NULL,
	`phone`	VARCHAR ( 20 ) NOT NULL,
	`email`	VARCHAR ( 256 ) NOT NULL,
	PRIMARY KEY(`username`)
);
CREATE TABLE IF NOT EXISTS `charging_station` (
	`sid`	INTEGER NOT NULL,
	`location`	VARCHAR ( 20 ) NOT NULL,
	`soc_shape`	VARCHAR ( 20 ) NOT NULL,
	`soc_size`	VARCHAR ( 20 ) NOT NULL,
	`soc_count`	INTEGER NOT NULL,
	`cost`	INTEGER NOT NULL,
	`charging_time`	INTEGER NOT NULL,
	PRIMARY KEY(`sid`)
);
CREATE TABLE IF NOT EXISTS `car_uses_charging_station` (
	`plate`	VARCHAR ( 20 ) NOT NULL,
	`sid`	INTEGER NOT NULL,
	`start_time`	DATETIME NOT NULL,
	`end_time`	DATETIME NOT NULL,
	FOREIGN KEY(`sid`) REFERENCES `charging_station`(`sid`),
	PRIMARY KEY(`plate`,`sid`,`start_time`,`end_time`),
	FOREIGN KEY(`plate`) REFERENCES `car`(`plate`)
);
CREATE TABLE IF NOT EXISTS `car_parts_provider` (
	`pid`	INTEGER NOT NULL,
	`name`	VARCHAR ( 20 ) NOT NULL,
	`phone`	VARCHAR ( 20 ) NOT NULL,
	`address`	VARCHAR ( 20 ) NOT NULL,
	PRIMARY KEY(`pid`)
);
CREATE TABLE IF NOT EXISTS `car_part_used_in_car` (
	`pname`	VARCHAR ( 50 ) NOT NULL,
	`plate`	VARCHAR ( 10 ) NOT NULL,
	PRIMARY KEY(`plate`,`pname`),
	FOREIGN KEY(`plate`) REFERENCES `car`(`plate`),
	FOREIGN KEY(`pname`) REFERENCES `car_part`(`name`)
);
CREATE TABLE IF NOT EXISTS `car_part_provided_by` (
	`pname`	VARCHAR ( 50 ) NOT NULL,
	`prid`	INTEGER NOT NULL,
	FOREIGN KEY(`prid`) REFERENCES `car_parts_provider`(`pid`),
	PRIMARY KEY(`prid`,`pname`),
	FOREIGN KEY(`pname`) REFERENCES `car_part`(`name`)
);
CREATE TABLE IF NOT EXISTS `car_part_available_in_workshop` (
	`pname`	VARCHAR ( 50 ) NOT NULL,
	`wid`	INTEGER NOT NULL,
	FOREIGN KEY(`pname`) REFERENCES `car_part`(`name`),
	PRIMARY KEY(`wid`,`pname`),
	FOREIGN KEY(`wid`) REFERENCES `workshop`(`wid`)
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
	`type`	VARCHAR ( 20 ) NOT NULL,
	`color`	VARCHAR ( 10 ) NOT NULL,
	PRIMARY KEY(`plate`)
);
COMMIT;
