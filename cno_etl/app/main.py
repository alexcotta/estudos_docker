from fastapi import FastAPI
from app.etl import extract_cno_data, transform_data, load_data
from fastapi.responses import JSONResponse

app = FastAPI(title="CNO ETL API")

@app.post("/etl/run")
def run_etl():
    try:
        df = extract_cno_data()
        df_transformed = transform_data(df)
        load_data(df_transformed)
        return {"status": "ETL concluído", "registros": len(df_transformed)}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/obras")
def get_obras(limit: int = 100):
    engine = create_engine("sqlite:///cno.db")
    df = pd.read_sql("SELECT * FROM obras LIMIT ?", engine, params=[limit])
    return df.to_dict(orient="records")
