create table project(
    id int primary key auto_increment,
    name varchar(200) not null ,
    dateAdd datetime default now()
);


create table individual(
    id int primary key auto_increment,
    email varchar(50) not null,
    name varchar(200) not null,
    caddress varchar(50) default '',
    haddress varchar(50) default '',
    phone varchar(14),
    sex  varchar(20),
    school  varchar(20)
);

create table comment(
    id int primary key auto_increment,
    email varchar(200) not null,
    content varchar(200) not null,
    dateAdd datetime default now()
);