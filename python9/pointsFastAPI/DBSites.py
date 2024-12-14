from fastapi import APIRouter, Form
from fastapi.encoders import jsonable_encoder
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from typing import Annotated
from starlette.responses import JSONResponse, FileResponse

from models.StackModel import Users, Posts

routerSitesJob = APIRouter()

engine = create_async_engine(
    "mysql+asyncmy://root:SaraParker206@127.0.0.1:3306/testalchymia?charset=utf8mb4"
)


@routerSitesJob.get("/index")
async def read_WebSites():
    return FileResponse("WebSites/index.html")


@routerSitesJob.get("/users")
async def read_WebSites():
    return FileResponse("WebSites/users.html")


@routerSitesJob.get("/posts")
async def read_WebSites():
    return FileResponse("WebSites/posts.html")


@routerSitesJob.get("/edit_users")
async def read_WebSites():
    return FileResponse("WebSites/edit_users.html")


@routerSitesJob.get("/edit_posts")
async def read_WebSites():
    return FileResponse("WebSites/edit_posts.html")


@routerSitesJob.post("/CreateUser", tags=["Main CRUD sites"])
async def write_users(username: Annotated[str, Form()], email: Annotated[str, Form()], password: Annotated[int, Form()]):
    async with engine.connect() as conn:
        await conn.execute(text(
            f"INSERT INTO Users (username, email, password) values('{username}', '{email}', '{password}')"))
        await conn.commit()
    return "Запись в бд реализована (Users)"


@routerSitesJob.post("/CreatePost", tags=["Main CRUD sites"])
async def write_posts(title: Annotated[str, Form()], content: Annotated[str, Form()], user_id: Annotated[int, Form()]):
    async with engine.connect() as conn:
        await conn.execute(text(f"INSERT INTO Posts (title, content, user_id) "
                                f"values('{title}', '{content}', '{user_id}')"))
        await conn.commit()
    return "Запись в бд реализована (Posts)"

@routerSitesJob.get("/SelectUser", tags=["Main CRUD sites"])
async def read_users():
    async with engine.connect() as conn:
        listData = await conn.execute(text(f"SELECT * FROM users"))
        listting = [dict(r._mapping) for r in listData]
        json_data = jsonable_encoder(listting)
        return JSONResponse(json_data)


@routerSitesJob.get("/SelectPosts", tags=["Main CRUD sites"])
async def read_posts():
    async with engine.connect() as conn:
        listData = await conn.execute(text(f"SELECT * FROM Posts join Users on Posts.user_id = Users.id"))
        listting = [dict(r._mapping) for r in listData]
        json_data = jsonable_encoder(listting)
        return JSONResponse(json_data)


@routerSitesJob.get("/SelectPostsOneUsers/{username}", tags=["Main CRUD sites"])
async def read_posts(username: str):
    async with engine.connect() as conn:
        listData = await conn.execute(
            text(f"SELECT * FROM Posts join Users on Posts.user_id = Users.id where username='{username}'"))
        listting = [dict(r._mapping) for r in listData]
        json_data = jsonable_encoder(listting)
        return JSONResponse(json_data)


@routerSitesJob.put("/UpdateUsers/{username}&{email}", tags=["Main CRUD sites"])
async def put_user(username: str, email: str):
    async with engine.connect() as conn:
        await conn.execute(text(f"Update users Set email = '{email}' Where username='{username}'"))
        await conn.commit()


@routerSitesJob.put("/UpdatePosts/{title}&{content}", tags=["Main CRUD sites"])
async def put_post(title: str, content: str):
    async with engine.connect() as conn:
        await conn.execute(text(f"Update posts Set content='{content}' Where title='{title}'"))
        await conn.commit()


@routerSitesJob.delete("/DeletePost", tags=["Main CRUD sites"])
async def delete_posts(title: Annotated[str, Form()]):
    async with engine.connect() as conn:
        await conn.execute(text(f"Delete From posts Where title='{title}'"))
        await conn.commit()


@routerSitesJob.delete("/DeleteUser", tags=["Main CRUD sites"])
async def delete_posts_user(user_id: Annotated[int, Form()]):
    async with engine.connect() as conn:
        await conn.execute(text(f"Delete From posts Where user_id='{user_id}'"))
        await conn.commit()
        await conn.execute(text(f"Delete From users Where id='{user_id}'"))
        await conn.commit()
