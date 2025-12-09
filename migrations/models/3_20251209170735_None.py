from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "questions" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "text" VARCHAR(30) NOT NULL,
    "category" VARCHAR(15) NOT NULL
);
CREATE TABLE IF NOT EXISTS "quotes" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "content" TEXT NOT NULL,
    "author" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "nickname" VARCHAR(20) NOT NULL UNIQUE,
    "hashed_password" VARCHAR(45) NOT NULL,
    "is_active" BOOL NOT NULL DEFAULT True,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "bookmarks" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "bookmarks_has_quotes" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "bookmark_id" INT NOT NULL REFERENCES "bookmarks" ("id") ON DELETE CASCADE,
    "quote_id" INT NOT NULL REFERENCES "quotes" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "diaries" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(50) NOT NULL,
    "text" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "token_blacklist" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "token" VARCHAR(255) NOT NULL,
    "expired_at" TIMESTAMPTZ NOT NULL,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
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
    "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"
    "fxBwxf+obL9l9H1vmB"
)
