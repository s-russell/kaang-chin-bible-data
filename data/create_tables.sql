create table language
(
    name text primary key
);

insert into language(name)
values ('English'),
       ('Kaang Chin');

create table book
(
    id   integer primary key autoincrement,
    name text not null,
    ordinal
         language text,
    foreign key (language) references language (name)
);

create table chapter
(
    id      integer primary key autoincrement,
    number  integer check (number > 0),
    title   text,
    book_id integer,
    foreign key (book_id) references book (id)
);

create table verse
(
    number     integer not null check (number > 0),
    title      text,
    text       text    not null,
    chapter_id integer,
    primary key (number, chapter_id),
    foreign key (chapter_id) references chapter (id)
);

