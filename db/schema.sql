CREATE TABLE `book`
(
    `code`          text PRIMARY KEY,
    `chapter_count` integer,
    `testament`     text check (testament in ('old', 'new'))
);

CREATE TABLE `bible_version`
(
    `id`   integer PRIMARY KEY AUTOINCREMENT,
    `name` string UNIQUE
);

CREATE TABLE `book_name`
(
    `book_code`  text references book (code),
    `version_id` integer references bible_version (id),
    `name`       text
);

CREATE TABLE `verse_count`
(
    `book_code`   text UNIQUE references book (code),
    `chapter`     integer NOT NULL,
    `verse_count` integer NOT NULL
);

CREATE TABLE `verse`
(
    `id`             integer PRIMARY KEY AUTOINCREMENT,
    `version`        integer references bible_version (id),
    `book_code`      text references book (code),
    `chapter_number` integer NOT NULL,
    `verse_number`   integer NOT NULL,
    `verse_text`     text    NOT NULL,
    `title`          text
);

CREATE UNIQUE INDEX `book_name_index_0` ON `book_name`
    (`book_code`, `version_id`, `name`);

CREATE INDEX `reference` ON `verse`
    (`book_code`, `chapter_number`, `verse_number`);
