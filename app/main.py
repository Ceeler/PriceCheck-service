from fastapi import FastAPI
from db.base import database
from endpoints import items, shops, categories
import uvicorn
# from prometheus_fastapi_instrumentator import Instrumentator
# from starlette_prometheus import metrics, PrometheusMiddleware

app = FastAPI()
# apm_config = {
#  'SERVICE_NAME': 'DemoFastAPI',
#  'SERVER_URL': 'http://localhost:8200',
#  'ENVIRONMENT': 'dev',
#  'GLOBAL_LABELS': 'platform=DemoPlatform, application=DemoApplication'
# }
# apm = make_apm_client(apm_config)
# app.add_middleware(ElasticAPM, client=apm)
# apm = make_apm_client(apm_config)

# app.add_middleware(ElasticAPM, client=apm)
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(shops.router, prefix="/shops", tags=["shops"])
app.include_router(categories.router, prefix="/categories", tags=["categories"])

@app.on_event("startup")
async def startup():
    await database.connect()

async def shutdown():
    await database.disconnnect()

if __name__ == "__main__":
     uvicorn.run("main:app", port=8200, host="0.0.0.0")