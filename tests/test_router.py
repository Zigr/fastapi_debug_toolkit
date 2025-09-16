from fastapi.testclient import TestClient

from app.main import app

# if get_env_setting("DEBUG_ROUTES_ENABLED") == "true":
#     include_debug_docs = get_env_setting("ENVIRONMENT") == "local"
#     app.include_router(
#         debug_router, prefix="/debug", include_in_schema=include_debug_docs
#     )

client = TestClient(app)


def test_debug_routes():
    response = client.get("/routes")
    data = response.json()
    print(data)
    print(client.base_url)
    routes = data.get("routes")
    assert len(routes) > 0
    # assert "/api/v1/openapi.json" in data
