begin;
-- Our Application Users
create table appuser (
   id serial primary key,
   fullname varchar not null check (length(fullname) > 2)
);

-- Persistence of any messages sent
create table message (
   id       serial  primary key,
   sender   integer not null references appuser,
   channel  varchar not null,
   content  text    not null
);

-- Trigger function - send notification of any saved message
create or replace function notify_message() returns trigger
as $$
BEGIN
   perform pg_notify(NEW.channel, to_json(NEW)::text);
   return null;
END;
$$ LANGUAGE plpgsql;

-- Add it as a trigger on INSERT
CREATE OR REPLACE TRIGGER t_notify_message AFTER INSERT ON message
    FOR EACH ROW EXECUTE FUNCTION notify_message();

-- Add some users
insert into appuser (fullname) VALUES ('Abe'), ('Bob'), ('Charlie');

commit;
