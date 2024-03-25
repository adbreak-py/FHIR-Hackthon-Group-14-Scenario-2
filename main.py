from fastapi import FastAPI
import io
from BarChart import run, plot_age_distribution_by_gender

app = FastAPI()

def create_plot():
    run()
    img_buf = io.BytesIO()
    
    

@app.get("/")
async def root():
    
    ctx = {
        
    }
    return {"message": "Hello World"}