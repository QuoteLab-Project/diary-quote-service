from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ALTER COLUMN "hashed_password" TYPE VARCHAR(128) USING "hashed_password"::VARCHAR(128);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ALTER COLUMN "hashed_password" TYPE VARCHAR(45) USING "hashed_password"::VARCHAR(45);"""


MODELS_STATE = (
    "eJztm21z2jgQgP8Kw6d0JtcJTmgz9w0IuXIN4Zo41047HY+wFdBgJGLLTZgO//0k+U2WX2"
    "oHuODGXzpktWtrH0va1Ur92V4SC9ru2z4hiyVwFu0/Wz/bGCwh+5FqO261wWoVt3ABBVNb"
    "KE8DLSEFU5c6wKSs4R7YLmQiC7qmg1YUEcyk2LNtLiQmU0R4Fos8jB48aFAyg3QOHdbw7T"
    "sTI2zBJ+iGf64Wxj2CtpXoL7L4u4XcoOuVkI0wvRSK/G1TwyS2t8Sx8mpN5wRH2ghTLp1B"
    "DB1AIX88dTzefd67wNXQI7+nsYrfRcnGgvfAs6nkbkkGJsGcH+uNKxyc8bf8oXXO3p+dn7"
    "47O2cqoieR5P3Gdy/23TcUBK719ka0Awp8DYEx5mY6kDtrAJrmd8FaKFrCbIhJSwWmFZi+"
    "DX+oaEOQRWxDQQw3HlA7ost8sCbYXgcfrgClPhoPb/Xe+B/uydJ1H2yBqKcPeYsmpGtFev"
    "TuDZcTNh38iRI9pPV5pH9o8T9bXyfXQ0GQuHTmiDfGevrXNu8T8CgxMHk0gCWNsVAagmGa"
    "8Yf1XOgYlWaFZPHrqXEg328Hs4MvKfeLzMnBiaQBXhIHohn+CNeC44j1CGATZnALFtG74D"
    "GHx28TjoFQGg8uBzxGy6w8NJh7zClIhYOD3u2gdzFsC4hTYC4egWMZOTTDKGE8eIRCNw22"
    "Hzzg8uMNtIHwJZdpGJg+8WfVC66ARTQiQUrgSzcttWUm0TyQY4DXOuH/lhyhz6a47/BXME"
    "BF1w0lX4kccfgIYtFJHXw+LeII0gu4jjAGwzv6CkFbZBe007lDvNk82TQHrjSoM2cIkxsp"
    "uGIkLAEGMyHjCDbHOUO8IDmLnC6RoSl9bZK1QwtHRclatIJWAqhYvabYLidE8iwvSU42eU"
    "3YClKiqbQh3DItkveWh8exbGqkzK7s9Cg1DneAr4aZj8pOnl9V88otk6jCyHuBgLPOirh+"
    "Q2GktZgKaoJr/YIrRdTOmJeDOXCy2UUGCj7W6cOclmzAPxk2xDPK89fuSQGuf3s3gw+9m6"
    "PuiVLBuA5aNNGUjLAUPmVUkXQmzQEY6NeFX1F1aPhFTxSGQk5H496XN4ni0NXk+q9QXeI6"
    "uJr0FZ5Nbe53rc2trGd+2KRl82Ff9MMGnW9qrk3N9bBqrvvMjT950A1cTqXHUVthhvwQaD"
    "U5cv1y5MwMryBFrlmGl8yQT8tkyKf5GfJpKkM2mbcz4m8hyzKUberJsdMtwbHTzeXImzJi"
    "xkutfznV+BJV+KbuXs9lj72OQlxpbyuZ1GXS/t/bW5ZJz0lGrpe/FMYWdWGaXAi1bpmVkG"
    "nlLoWirdJaqB6AJA9Cm/P3bc7fC1hWPoLf5jTk0E7hZV/Ug3jpzkLyFF49aVdP4uXDgl2d"
    "wkfDITfc62QBcd9mfbGRS7PivqJRmABQrmtME8pNJlCjTEB8wEo7oNDglUcsOfDDpxVynl"
    "X+TFrWs/xZk3Jn6HZzybQpeL7qgqcAmxH3Q+D50Z471Oz2axfj4RIgu0qMjwx2E+P3zm//"
    "ER4jcyF+V6Ao29QSZJlqsZZfLdZS1WK2oZmzZGcFXPeROBmzOR9mhmk9E9COdl6meKyd51"
    "ePeVsSLHINthqjHxnjk21dbQhwziIp2yk82T7U3hfQaNzuOuHsTyZXiVyzP1ILd3fj/pAB"
    "FniZEvJjcvp6bXNZ5be40xD/v4TK9cUdVxYP80PnFhXluSDdAX0+h+iuaU0hiMrHlgzStb"
    "UawdjnpqQHHWTO2xnbkqDluGhjAmKdZmeyyyiw553JD7afDOZL2URQMqlnAriX/QmfGhUg"
    "Bur1BNg5KbMxYVr5GfRJ+iJL3on437eT66on4neYOfjNQiY9bvF1/vthYi2gyL0uPh9Xj8"
    "KVPI0/oP/Sl1w2/wEhD/oX"
)
