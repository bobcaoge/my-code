/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2019/5/21 21:16:02                           */
/*==============================================================*/


drop table if exists user;

drop table if exists book;

drop table if exists borrow;

drop table if exists reader;

/*==============================================================*/
/* Table: User                                                  */
/*==============================================================*/
create table user
(
   id                   int not null,
   name                 varchar(50),
   pass                 varchar(50),
   is_admin             smallint,
   primary key (id)
);

/*==============================================================*/
/* Table: book                                                  */
/*==============================================================*/
create table book
(
   id                   varchar(50) not null,
   name                 varchar(50),
   type                 varchar(50),
   author               varchar(50),
   translator           varchar(50),
   publisher            varchar(50),
   publishi_time        varchar(50),
   stock                int,
   price                double,
   primary key (id)
);

/*==============================================================*/
/* Table: borrow                                                */
/*==============================================================*/
create table borrow
(
   id                   int,
   book_id              varchar(50),
   reader_id            varchar(50),
   borrow_date          date,
   back_date            date,
   is_back              boolean
);

/*==============================================================*/
/* Table: reader                                                */
/*==============================================================*/
create table reader
(
   id                   varchar(50) not null,
   name                 varchar(50),
   type                 varchar(50),
   sex                  varchar(50),
   max_num              int,
   days_num             int,
   primary key (id)
);

