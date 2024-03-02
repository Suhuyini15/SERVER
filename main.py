from fastapi import FastAPI
app = FastAPI()

# @app.get('/')
# # def result():
# #      return ans ,word
@app.get('/ans')
def add():
     ans =5+9
     return ans

@app.get('/new')
def see():
    word ='nope' + 'go'
    return word