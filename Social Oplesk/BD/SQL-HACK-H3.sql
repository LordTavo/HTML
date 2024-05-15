
CREATE TABLE public.countries (
                id_country INTEGER NOT NULL,
                name VARCHAR NOT NULL,
                CONSTRAINT id_country PRIMARY KEY (id_country)
);


CREATE TABLE public.priorities (
                id_priority INTEGER NOT NULL,
                type_name VARCHAR NOT NULL,
                CONSTRAINT id_priority PRIMARY KEY (id_priority)
);


CREATE SEQUENCE public.contact_request_id_email_seq;

CREATE TABLE public.contact_request (
                id_email INTEGER NOT NULL DEFAULT nextval('public.contact_request_id_email_seq'),
                id_priority INTEGER NOT NULL,
                id_country INTEGER NOT NULL,
                name VARCHAR NOT NULL,
                physical_address VARCHAR NOT NULL,
                detail VARCHAR NOT NULL,
                CONSTRAINT id_email PRIMARY KEY (id_email, id_priority, id_country)
);


ALTER SEQUENCE public.contact_request_id_email_seq OWNED BY public.contact_request.id_email;

ALTER TABLE public.contact_request ADD CONSTRAINT countries_contact_request_fk
FOREIGN KEY (id_country)
REFERENCES public.countries (id_country)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.contact_request ADD CONSTRAINT priorities_contact_request_fk
FOREIGN KEY (id_priority)
REFERENCES public.priorities (id_priority)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
