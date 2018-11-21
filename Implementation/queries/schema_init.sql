create table if not exists customer (
full_name varchar(20) not null,
username varchar(20) not null,
address varchar(20) not null,
phone varchar(20) not null,
e_mail varchar(256) not null,

primary key (username)
);

create table if not exists customer_uses_car (
customer varchar(20) not null,
car varchar(20) not null,

primary key (car, customer),
foreign key (customer) references customer(username),
foreign key (car) references car(plate)
);

create table if not exists car (
plate varchar(20) not null,
battery_charge varchar(20) not null,
gps_location varchar(20) not null,
type date not null,
e_mail varchar(256),
uses varchar(20) not null,
closest_charging_station varchar(20) not null,

primary key (plate),
foreign key (closest_charging_station) references charging_station(uid)
);

create table if not exists customer_orders_car (
customer varchar(20) not null,
car varchar(20) not null,

primary key (car, customer),
foreign key (customer) references customer(username),
foreign key (car) references driving_history(car)
);

create table if not exists customer_drives_car (
customer varchar(20) not null,
car varchar(20) not null,

primary key (car, customer),
foreign key (car) references car(plate),
foreign key (customer) references driving_history(car)
);

create table if not exists driving_history (
type varchar(20) not null,
cost int not null,
end_time varchar(20) not null,
start_time varchar(20) not null,
distance varchar(20) not null,
customer varchar(20) not null,
car varchar(20) not null,

primary key (car, customer),
foreign key (car) references driving_history(car),
foreign key (car) references car(plate)
);

CREATE TABLE charging_station (
uid int not null,
gps_location varchar(20) not null,
shape varchar(20) not null,
size varchar(20) not null,
cost int not null,
charging_time varchar(20) not null,
number_of_available_sockets varchar(20) not null,
primary key (uid)
);

CREATE TABLE charging_history (
car varchar(20) not null,
charging_station int not null,

primary key (car, charging_station),
foreign key (car) references car(plate),
foreign key (charging_station) references charging_station(uid)
);

CREATE TABLE car_part_used_in_car (
car_part varchar(20) not null,
car varchar(20) not null,

primary key(car, car_part),
foreign key (car) references car(plate),
foreign key (car_part) references car_part(name)
);

CREATE TABLE car_part (
name varchar(20) not null,
price varchar(20) not null,
type varchar(20) not null,

used_in varchar(20) not null,
provided_by int not null,
available_in int not null,

primary key (name),
foreign key (provided_by) references car_parts_provider(id),
foreign key (available_in) references workshop(wid)
);

CREATE TABLE car_part_provided_in (
car_part varchar(20) not null,
provider int not null,

primary key(provider, car_part),
foreign key (provider) references car_parts_provider(id),
foreign key (car_part) references car_part(name)
);


CREATE TABLE car_parts_provider (
id int not null,
name varchar(20) not null,
phone varchar(20) not null,
address varchar(20) not null,

used_in varchar(20) not null,

primary key (id)
);

CREATE TABLE car_part_available_in_workshop (
car_part varchar(20) not null,
workshop int not null,

primary key(workshop, car_part),
foreign key (workshop) references workshop(wid),
foreign key (car_part) references car_part(name)
);

CREATE TABLE workshop (
wid int not null,
availiability varchar(20) not null,
gps_location varchar(20) not null,

primary key (wid)
);

CREATE TABLE car_part_used_in_repair (
car_part varchar(20) not null,
repairing_history int not null,

primary key(repairing_history, car_part),
foreign key (repairing_history) references repairing_history(car),
foreign key (car_part) references car_part(name)
);

CREATE TABLE repairing_history (
car varchar(20) not null,
car_part varchar(20) not null,
workshop int not null,
start_time varchar(20) not null,
end_time varchar(20) not null,
count varchar(20) not null,

primary key (car, car_part, workshop),
foreign key (car) references car(plate)
foreign key (workshop) references workshop(wid)
);