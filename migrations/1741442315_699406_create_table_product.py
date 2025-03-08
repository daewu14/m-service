# 1741442315_699406_create_table_product.py
# Description: Create Table Product
# Generated by: dw_migrations
# Created on: 08.03.2025

# !!! Don't modify this variable !!!
timestamp = 1741442315.699406

# Migration up, modify here
sql_up = """
create table products
(
    id          int auto_increment,
    uuid        varchar(128)            null,
    name        varchar(128)            null,
    slug        varchar(128)            null,
    description varchar(128)            null,
    created_at timestamp default now() not null,
    updated_at timestamp default now() not null on update now(),
    constraint users_pk primary key (id)
);
"""

# Migration down, modify here
sql_down = """
drop table if exists products;
"""
