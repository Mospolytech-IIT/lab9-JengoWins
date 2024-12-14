from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from starlette.responses import JSONResponse

from models.StackModel import Users, Posts

routerDBJob = APIRouter()

engine = create_async_engine(
    "mysql+asyncmy://root:SaraParker206@127.0.0.1:3306/testalchymia?charset=utf8mb4"
)


@routerDBJob.get("/DBCreateTable", tags=["Creating"])
async def write_DBCreateTable():
    async with engine.connect() as connections:
        await connections.execute(text("CREATE TABLE `users` ("
                                       "`id` int NOT NULL AUTO_INCREMENT,"
                                       "`username` varchar(145) DEFAULT NULL,"
                                       "`email` varchar(145) DEFAULT NULL,"
                                       "`password` varchar(45) DEFAULT NULL,"
                                       "PRIMARY KEY (`id`),"
                                       "UNIQUE KEY `username_UNIQUE` (`username`),"
                                       "UNIQUE KEY `email_UNIQUE` (`email`)"
                                       ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"))
        await connections.execute(text("CREATE TABLE `posts` ("
                                       "`id` int NOT NULL AUTO_INCREMENT,"
                                       "`title` varchar(145) DEFAULT NULL,"
                                       "`content` varchar(145) DEFAULT NULL,"
                                       "`user_id` int NOT NULL,"
                                       "PRIMARY KEY (`id`),"
                                       "KEY `id_user_idx` (`user_id`),"
                                       "CONSTRAINT `id_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)"
                                       ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"))
        return "Creates Tables"


@routerDBJob.post("/DBCreateUser", tags=["Main CRUD"])
async def write_users(users: list[Users]):
    async with engine.connect() as conn:
        for user in users:
            await conn.execute(text(
                f"INSERT INTO Users (id, username, email, password) values('{user.id}', '{user.username}', '{user.email}', '{user.password}')"))
            await conn.commit()


@routerDBJob.post("/DBCreatePost", tags=["Main CRUD"])
async def write_posts(users: list[Posts]):
    async with engine.connect() as conn:
        for user in users:
            await conn.execute(text(f"INSERT INTO Posts (id, title, content, user_id) "
                                    f"values('{user.id}', '{user.title}', '{user.content}', '{user.user_id}')"))
            await conn.commit()


@routerDBJob.get("/DBSelectUser", tags=["Main CRUD"])
async def read_users():
    async with engine.connect() as conn:
        listData = await conn.execute(text(f"SELECT * FROM users"))
        listting = [dict(r._mapping) for r in listData]
        json_data = jsonable_encoder(listting)
        return JSONResponse(json_data)


@routerDBJob.get("/DBSelectPosts", tags=["Main CRUD"])
async def read_posts():
    async with engine.connect() as conn:
        listData = await conn.execute(text(f"SELECT * FROM Posts join Users on Posts.user_id = Users.id"))
        listting = [dict(r._mapping) for r in listData]
        json_data = jsonable_encoder(listting)
        return JSONResponse(json_data)


@routerDBJob.get("/DBSelectPostsOneUsers/{username}", tags=["Main CRUD"])
async def read_posts(username: str):
    async with engine.connect() as conn:
        listData = await conn.execute(text(f"SELECT * FROM Posts join Users on Posts.user_id = Users.id where username='{username}'"))
        listting = [dict(r._mapping) for r in listData]
        json_data = jsonable_encoder(listting)
        return JSONResponse(json_data)


@routerDBJob.put("/DBUpdateUsers/{username}&{email}", tags=["Main CRUD"])
async def put_user(username: str, email: str):
    async with engine.connect() as conn:
        await conn.execute(text(f"Update users Set email = '{email}' Where username='{username}'"))
        await conn.commit()


@routerDBJob.put("/DBUpdatePosts/{title}&{content}", tags=["Main CRUD"])
async def put_post(title: str, content: str):
    async with engine.connect() as conn:
        await conn.execute(text(f"Update posts Set content='{content}' Where title='{title}'"))
        await conn.commit()


@routerDBJob.delete("/DBDeletePost/{title}", tags=["Main CRUD"])
async def delete_posts(title: str):
    async with engine.connect() as conn:
        await conn.execute(text(f"Delete From posts Where title='{title}'"))
        await conn.commit()


@routerDBJob.delete("/DBDeleteUser/{username}", tags=["Main CRUD"])
async def delete_posts_user(username: str):
    async with engine.connect() as conn:
        await conn.execute(text(f"Delete From posts Where user_id=(Select id From users Where username='{username}')"))
        await conn.commit()
        await conn.execute(text(f"Delete From users Where username='{username}'"))
        await conn.commit()
