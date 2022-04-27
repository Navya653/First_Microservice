from config import app

@app.get('/home')
def greetnow():
    return "this is home page"

@app.get('/sample')
def fun():
    return "this is a sample page"