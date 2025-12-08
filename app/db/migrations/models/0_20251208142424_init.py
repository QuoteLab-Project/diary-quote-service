from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "diary" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(200) NOT NULL,
    "content" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztll1v2jAUhv9KlCsmdVVh0Fa7y4CtTAWmNtuqVlVkYhMsHJs6Tguq+O/zcRLyQYlAmr"
    "Qi7S55z2v7nCeOj1/tUGDCotMeRXJlf7ZebY5Coh/KgRPLRotFLoOg0IQZJ95YJpGSyFda"
    "nCIWES1hEvmSLhQVXKs8ZgxE4Wsj5UEuxZw+xcRTIiBqRqQOPDxqmXJMliTKXhdzb0oJw6"
    "VEKYa1je6p1cJoA66+GiOsNvF8weKQ5+bFSs0E37gpV6AGhBOJFIHplYwhfcguLTOrKMk0"
    "tyQpFsZgMkUxU4Vy92TgCw78dDaRKTCAVT62mu2L9uWn8/altphMNsrFOikvrz0ZaAiMXH"
    "tt4kihxGEw5twUVXq6LXTdGZJvs9sMqODTSVfxZbDq+GVCDjDfNH+JYIiWHiM8UDPAdnZW"
    "w+uXc9O9cm4a2vUBqhF6Iyfbe5SGWkkMoOYQ9YqKJNunjNElyx1bsDDkWEDWcHP7dy4kHU"
    "bREyviagydO0MyXKWR6/HoW2Yv4O1ej79UqUoC9XvoDbA9HVE0JDvglkZW+OJ06Gn28D5p"
    "27oGPOZslZ4pdfQHw/6t6wx/lD5Bz3H7EGmV8Gdq47yywTeTWL8H7pUFr9b9eNQ3BEWkAm"
    "lWzH3uvQ05oVgJj4sXD+HC8ZepGZg1HNzTeeEIAmGC/PkLktjbioiW2OXdDoWtsKogjgLz"
    "WQAupJk2ModI6s/eanFppLbHodzzv8kdUZN7JjKClA5oc4Uhx3I+Vxpdp7NPo+t0djc6iJ"
    "WPZPg1DoCY2o8TYHOvm0Kz5qbQPOCm8P12PDr0pvCT6wIfMPXVicVopB7fJ9YailB1/b2h"
    "ekWodCOYAO4N/7S9rP8AWGg4Ag=="
)
