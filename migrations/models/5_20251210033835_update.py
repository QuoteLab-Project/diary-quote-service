from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "token_blacklist" ALTER COLUMN "expired_at" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "token_blacklist" ALTER COLUMN "expired_at" SET NOT NULL;"""


MODELS_STATE = (
    "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"
    "OPx9WTcIWn8QcMXvqOy/Y/z6/5zA=="
)
