from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "nickname" VARCHAR(20) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password_hash" VARCHAR(255) NOT NULL,
    "is_active" BOOL NOT NULL DEFAULT True,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "token_blacklist" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "token" VARCHAR(512) NOT NULL UNIQUE,
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
    "eJztmF1v2jAUhv8K4opJXVWy0la7g5apTAWmNt2mVlVkEpNYOHYaO21RxX+vj8mn+RBMq1"
    "ok7sJ73pOc88QcG17rIfcwFYe3Asf177XXOkMhVhcV/aBWR1FUqCBINKLamCiHVtBIyBi5"
    "UoljRAVWkoeFG5NIEs6UyhJKQeSuMhLmF1LCyGOCHcl9LANdyP2Dkgnz8AsW2cdo4owJpl"
    "6lTuLBs7XuyGmktR6TP7QRnjZyXE6TkBXmaCoDznI3YRJUHzMcI4nh9jJOoHyoLm0z62he"
    "aWGZl1jK8fAYJVSW2t2QgcsZ8FPVCN2gD0/5ajWPT4/Pvp0cnymLriRXTmfz9ore54mawM"
    "Cuz3QcSTR3aIwFN0bcib5eoHceoHg5vnKOAVGVbkLMkH0oxRC9OBQzXwaA7mgNst/t6/PL"
    "9nXDOvoCnXC1lOcLfJBGLB0CqgVFHCJCt0GYJ+wkv1ZrE4Ct1mqCEKsijJAQzzz2nACJYB"
    "uUC4n/B2kmFEyLabYzUIlw1CQmT0u+3h3OKUZsxYAs5xk8RyrxvYDmy/afgK7h1xkOr6Do"
    "UIhHqoWebXC87Xe6142mxqtMROLyBC2YujGGrh0kF6FeqIgkIV5OtZppYPXS1MPs4pMuWt"
    "WDN2R0mr6tNcztXr97Y7f7vyrgL9p2FyKWVqeG2jgxlnd+k9qfnn1Zg4+1u+GgqwlyIf1Y"
    "P7Hw2Xd1qAklkjuMPzvIK83DTM3AzOA8MZ6UdkYQRsidPCM1URYi3OKrvIuh0ApNBTHk69"
    "cCcKHM9Hhl8wlmHaruRYmQyw5ghmPtUUyC1xlVzPtD2Q4dyvQL3GYPzBN28TjRalob7HzK"
    "tXLn07H9lN5P6fed0m0cEzdYNp3TyNqpjArPfhjv0DB+wrGAkrYYx6WU/Y+RHCR8NbaAmN"
    "p3E2DzaJP/GJRrJUAdM/Y0ziRmSza0nzfDwYrNrEgxQN4y1eC9R1x5UINT4sPnxLqGInRd"
    "2bQyeI1++6/J9fxq2DF3I7hBRzH+0O1l9gZyT9t0"
)
