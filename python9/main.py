import uvicorn
from fastapi import FastAPI
from pointsFastAPI.DBCreate import routerDBJob
from pointsFastAPI.DBSites import routerSitesJob

"""swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"}"""
app = FastAPI()


app.include_router(routerDBJob)
app.include_router(routerSitesJob)

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=False, access_log=True)