from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "plant_diseases" ADD "symptoms" JSONB NOT NULL;
        ALTER TABLE "plant_diseases" ADD "causes" JSONB NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """"""
