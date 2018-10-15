
CREATE EXTENSION hstore;

CREATE SCHEMA myschema;

CREATE TABLE myschema.mytable (
    id    BIGSERIAL PRIMARY KEY,
    lali  VARCHAR(123) NOT NULL,
    hiha  NUMERIC(5,2),
    nono  hstore  
);

INSERT INTO myschema.mytable (lali) VALUES 
('cool stuff');

INSERT INTO myschema.mytable (lali, hiha) VALUES
('with a number (check the rounding)', 123.456);

INSERT INTO myschema.mytable (lali, nono) VALUES
('some unstructured nosql-ish hstore', '
    "thisis" => "key-value item", 
    "beaware" => "hstore does not allow sub-arrays like json",
    "mymoney" => "987.65" 
');
