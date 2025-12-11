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
    "eJztmm1T2zgQgP9KJp/oDNchhrTMfUtCuOYKSQvmrtNOx6PYItHEkYItFzId/vtJ8pv8ej"
    "ZNigX+lqx2be2jl12t9bO7Jha03bdDQlZr4Ky6f3Z+djFYQ/Yj03bY6YLNJm7hAgrmtlCe"
    "B1pCCuYudYBJWcMtsF3IRBZ0TQdtKCKYSbFn21xITKaI8CIWeRjdedCgZAHpEjqs4dt3Jk"
    "bYgg/QDf9uVsYtgraV6C+y+LuF3KDbjZBNMD0Xivxtc8MktrfGsfJmS5cER9oIUy5dQAwd"
    "QCF/PHU83n3eu8DV0CO/p7GK30XJxoK3wLOp5G5FBibBnB/rjSscXPC3/KH1Tt6fnB6/Oz"
    "llKqInkeT9o+9e7LtvKAhM9e6jaAcU+BoCY8zNdCB31gA0y++MtVC0hvkQk5YpmFZg+jb8"
    "kUYbgixjGwpiuPGE2hFd5oM1w/Y2GLgSlPrkcnytDy4/cU/WrntnC0QDfcxbNCHdpqQH79"
    "5wOWHLwV8o0UM6/070Dx3+t/N1Nh0LgsSlC0e8MdbTv3Z5n4BHiYHJvQEsaY6F0hAM04wH"
    "1nOhY9RaFZLF/y+NhozfDlYH31JuV7mLgxPJAjwnDkQL/BFuBccJ6xHAJszhFmyiN8Fjms"
    "fvMZwDoTSeXA64j7ZZeWow95hTkAoHR4Pr0eBs3BUQ58Bc3QPHMgpohlHCuPMIhW4W7DB4"
    "wPnHK2gD4Ush0zAwfebPUguugEU0IkFK4Ms2rbV1WgIwWIhe83fzN+VyKYnoEbgKYd1YAl"
    "catTbCN20PK4vw0bKrBTBl9ZoCghxFxaSvR042eU3YSuLoXDpF/GIslQ8kzeNYNZ6mVld+"
    "TM3Mwx3gUzBcptnJ66tuMrLPyHuGgLPNi7h+Q2mktZgKaoOresGVImrnrMvREjj57CKDFD"
    "7W6WYuSzbhHwwb4gVdsr/9oxJc/wyuRh8GVwf9o9Sxdxq0aKIpGWEpfMgpPehMWgAw0FeF"
    "X1lJYfxFT1QTQk4Hl4MvbxIVhYvZ9K9QXeI6upgNUzzbgs5LLehsrCcObNKyHdhnHdig82"
    "2hri3UNatQt8/c+LMH3cDlTHoctZVmyHeBVpsjq5cj52Z4JSmyYhleMkM+rpIhHxdnyMeZ"
    "DNlk3i6If4SsylC2UZNjr1+BY69fyJE35cSM59r/CqrxFarwbd1dzW2PvY5CXOtsK5mosm"
    "h/9/GWZdJLkpPrFW+FsYUqTJMbodavshMyrcKtULTV2gvTH0ASF3zaj7a7Dg86WUE8tNmz"
    "bOTSvDiR0igNGJTrGvOEchs5FIocYgBrZcyhwSvf4eRAAR82yHlSuSxpuYNyWTD9GhKVG1"
    "QdC91u2EW23z9eL6o89mzTXdXqmOCaE/RD3sWhnjvUHg2VC/BwDZBdJ8BHBrsJ8Hvnt//w"
    "jpG5Er9rUJRtlARZpbSoFZcWtUxpcQncJct0NsB174mTs5qLYeaYqpl99rTTKpVG7bS41M"
    "jbkmCRa7DdGP3ImZ/sEGxDgAs2SdkuxZMdwu19AY3m7a7TzeFsdpHINIeTdJXn5nI4ZoAF"
    "XqaE/JicvYvZ3mx4ER/A/Qz/ScWoHZehmjnQhRUoeS1IFwafziG6mKgoBFH2+EUG2cKaMq"
    "ebvZYkB9BB5rKbcyoJWg7LziUg1mkPJrsMAns+mPxgx8lguVTNAyUTNfO/vRxP+NKoATFQ"
    "VxNg76jKuYRpFSfQR9lLD0VfT/++nk3rfj29wczBbxYy6WGHb/Pfm4m1hCL3uvxbavqzaS"
    "pN4w8YPveFiMf/ADILwIM="
)
