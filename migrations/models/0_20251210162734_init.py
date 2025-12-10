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
    "hashed_password" VARCHAR(128) NOT NULL,
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
    "expired_at" TIMESTAMPTZ,
    "user_id" INT REFERENCES "users" ("id") ON DELETE CASCADE
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
    "eJztW21z2jgQ/isMn9KZXCeQ0GbuGxBy5RqgTZy2007HI2wFNBiJ2HITpsN/P0n4RZZfzg"
    "7Q2Im/dMhq19Y+WmmfXbm/m0tiQst52yNksQT2ovl343cTgyVkP2Jjx40mWK3CES6gYGoJ"
    "5amnJaRg6lAbGJQN3AHLgUxkQsew0YoigpkUu5bFhcRgigjPQpGL0b0LdUpmkM6hzQZ+/G"
    "RihE34CB3/z9VCv0PQMiPzRSZ/t5DrdL0SsiGml0KRv22qG8RylzhUXq3pnOBAG2HKpTOI"
    "oQ0o5I+ntsunz2fnuep7tJ1pqLKdomRjwjvgWlRyNycGBsEcPzYbRzg442/5q906e392fv"
    "ru7JypiJkEkvebrXuh71tDgcBYa27EOKBgqyFgDHEzbMid1QGN43fBRihawmQQo5YKmKZn"
    "+tb/oULrA5mFrS8IwQ0Dak/oMh/MCbbW3sJlQKkNR4MbrTv6xD1ZOs69JSDqagM+0hbStS"
    "I9eveGywnbDtuNEjyk8XWofWjwPxvfJ+OBQJA4dGaLN4Z62vcmnxNwKdExedCBKcWYL/WB"
    "YZrhwroOtPVCu0Ky+P+tUZL128Pu4EfK3SJxc3BE4gBeEhuiGf4I1wLHIZsRwAZMwM07RG"
    "+9x5QPv40fA740DC4bPATHrBwazD3mFKTCwX73pt+9GDQFiFNgLB6AbeopaPpZQr93CYVO"
    "HNie94DLj9fQAsKXVEz9xPSZP6ta4AqwSJtIIEXgiw8t28tERNOAHAG81gj/N2eEPhnFQ6"
    "e/jAAVU9cVvhI4YvMIYtlJDb4tWsQWSC/gOoDRC+9gFbyxwM4bp3ObuLN5dGgOHCmoE3cI"
    "k+sxcEUkLAEGMyHjEGyOU0I8g5wFTudgaMpca7JWtnSURdaCE7QQgIrVa8rtMiGSd3lO5G"
    "ST1wRbBiWaSgXhjrRIri3Lh2NeaqTsrmR6FIvDPcBXQeajYifvr6K8ckcSlZl5LxCw10kZ"
    "dzuQmWlNpoLq5Fq95EoRtRL2ZX8O7GTsAgMFPjbpcm5LFvCPugXxjHL+2jnJgOtL97r/oX"
    "t91DlROhhjb6QthqIZlsLHhC6SxqQpAHr6VcEvqzs0+KZFGkM+Tkej7rc3kebQ1WT8j68u"
    "4dq/mvQUPOve3Evtza3MJy5s1LJe2GddWG/ydc+17rmWq+d6SG782YWO53KMHgdjmQz53t"
    "OqOXL1OHIiw8ugyBVjeFGGfJqHIZ+mM+TTGEM2mLczsi0h82Io21QTx1YnB46tTiqOfCgh"
    "ZzzX+ZfSjc/Rha/77tU89tjrKMSFalvJpCqb9k+Xt4xJz0kC10s/CkOLqmAaPQjbnTwnId"
    "NKPQrFWKGzUL0AiV6E1vfvu9y/Z2BZ+Ap+l9uQst3Cy76oF/HSNwvRW3j1pl29iZcvC/Z1"
    "Cx+EQ2q618gC4p7F5mIhhyblfUUjkwBQrqtPI8o1E6gQExALWKgC8g1eecaSEz98XCH7Se"
    "3PqOUe2p9e+JWEZZWo2+m7XbJvTP/8er2oduezhXtVu50C14Sk7+Odnuq5Q3WpX7kED5cA"
    "WUUSfGCwnwR/cPwOn94xMhbidwEUZZtKApmnVdxObxW3Y61iVs3MGdNZAcd5IHbCbk4HM8"
    "G0muyz1T7P0zlun6e3jvlYFFjk6Ow0Rr8S4pPVrRYEOOWQlO0UPFkRah0K0CBu9003e5PJ"
    "VYRp9oZq1+521BswgAW8TAltc3L829r6S5UX8UFD+J8SCjcX99xWLOdCp3YU5b0gfQD6dB"
    "yCD00rCoJoe+yIQbyxVpnqZtcWc2ZN0oU2MubNhKrEGznOqktAqFMXJvtMAgcuTH6xctLb"
    "Lnl5oGRSTf53kPKEb40CIHrq1QSwdZKnLmFa6QT6JP4RS9pt+L83k3HR2/BbzBz8YSKDHj"
    "f4Mf+znLBmoMi9zr4bV6/BFZrGH9B77g9cNv8BS1j46w=="
)
