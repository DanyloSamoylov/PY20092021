from app import app, Config


if __name__ == '__main__':
    app.run(debug=True, host=Config.APP_URL)
