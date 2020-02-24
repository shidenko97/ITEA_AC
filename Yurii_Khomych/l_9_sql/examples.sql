create database my_shop;
-- \c my_shop
create table customers
(
    id            serial primary key,
    customer_name varchar(100),
    contact_name  varchar(100),
    address       varchar(200),
    city          varchar(50),
    postal_code   varchar(50),
    country       varchar(50)
);
create table products
(
    id           serial primary key,
    product_name text,
    unit         varchar,
    price        int
);
alter table products alter column price type float;
create table orders
(
    id          serial primary key,
    customer_id int references customers (id) on delete cascade,
    order_date  date
--     primary key (id, customer_id, employee_id)
);
alter table orders
    add column products_id int references products (id);

create table employees
(
    id         serial primary key,
    last_name  varchar(100),
    first_name varchar(50),
    birth_date date,
    photo      varchar,
    notes      text
);
alter table orders
    add column employee_id int references employees (id) on delete cascade;


-- continue from that...
insert into customers
values (1, 'Alfreds Futterkiste ', 'Maria Anders',
        'Obere Str. 57', 'Berlin', '12209',
        'Germany');
insert into customers (customer_name,
                       contact_name,
                       address,
                       city,
                       postal_code,
                       country)
values ('Ana Trujillo Emparedados', ' Ana Trujillo',
        'Avda. de la Constitución 2222 ', 'México', 'D.F. 05021', 'Mexico');
insert into customers (customer_name,
                       contact_name,
                       address,
                       city,
                       postal_code,
                       country)
values ('Antonio Moreno Taquería', 'Antonio Moreno', 'Mataderos 2312',
        'México', 'D.F. 05023 	', 'Mexico');
insert into customers (customer_name,
                       contact_name,
                       address,
                       city,
                       postal_code,
                       country)
values ('Around the Horn', 'Thomas Hardy', '120 Hanover Sq.', 'London',
        'WA1 1DP', 'UK');
insert into customers (customer_name,
                       contact_name,
                       address,
                       city,
                       postal_code,
                       country)
values ('Berglunds snabbköp', 'Christina Berglund', 'Berguvsvägen 8', 'Luleå',
        'S-958 22', 'Sweden');

insert into products (product_name, unit, price)
values ('Apple', 'kg', 10);
insert into products (product_name, unit, price)
values ('Banana', 'kg', 20);
insert into products (product_name, unit, price)
values ('Peach', 'kg', 5);
insert into products (product_name, unit, price)
values ('M&M', 'pcg', 100500);

insert into employees (last_name, first_name, birth_date, photo, notes)
values ('Davolio', 'Nancy', '1992-01-01', 'EmpID1.pic',
        'Education includes a BA in psychology from Colorado State University. She also completed (The Art of the Cold Call). Nancy is a member of Toastmasters International.');
insert into employees (last_name, first_name, birth_date, photo, notes)
values ('Fuller', 'Andrew', '1890-01-02', 'EmpID2.pic',
        'Andrew received his BTS commercial and a Ph.D. in international marketing from the University of Dallas. He is fluent in French and Italian and reads German. He joined the company as a sales representative, was promoted to sales manager and was then named vice president of sales. Andrew is a member of the Sales Management Roundtable, the Seattle Chamber of Commerce, and the Pacific Rim Importers Association.');
insert into employees (last_name, first_name, birth_date, photo, notes)
values ('Leverling', 'Janet', '1953-01-05', 'EmpID3.pic',
        'Janet has a BS degree in chemistry from Boston College). She has also completed a certificate program in food retailing management. Janet was hired as a sales associate and was promoted to sales representative.');


insert into orders (customer_id, order_date)
values (1, '2019-09-08');

alter table orders alter column products_id set not null;

alter table orders
    add column additional_info text;


-- joins