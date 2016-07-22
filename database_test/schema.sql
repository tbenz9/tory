DROP TABLE IF EXISTS entries;


CREATE TABLE entries (
    id integer primary key autoincrement,
    info_type text not null,
    json text not null
);

