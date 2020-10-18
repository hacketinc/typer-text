from fastapi import FastAPI
from faker import Faker

app = FastAPI()

@app.get('/type-text/')
async def type_text():
    fake = Faker()
    sentence = fake.paragraph(nb_sentences=20)
    return {"message": sentence}