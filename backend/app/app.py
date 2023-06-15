import uvicorn

from app.server import AppCreator


app_creator = AppCreator()
app = app_creator.get_app()


# if __name__ == '__main__':
#     uvicorn.run(app='app:app', host='127.0.0.1', port=8080, reload=True)
