# fastapi_debug_toolkit

---

Debug and diagnostics toolkit for FastAPI apps based on [full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template/tree/master)
Provided as editable installable Python module. The is packaged with [uv](https://docs.astral.sh/uv/) package and project manager.

---
⚠️ If installed **as is** from the **current repo**, Dockerfile **changes** should be made as well.

---

## Debug some configuration

```bash
curl http://127.0.0.1:8000/debug/routes         # List all registered routes and tags
curl http://127.0.0.1:8000/debug/config         # Expose current app settings (DEV ONLY)
curl http://127.0.0.1:8000/debug/middlewares    # List all middleware classes (DEV ONLY)
curl http://127.0.0.1:8000/debug/events         # List startup and shutdown event handlers (DEV ONLY)
curl http://127.0.0.1:8000/debug/mounts         # LList all mounted sub-apps (DEV ONLY)

```

 ---

## Enable / disable routes debug in production

```bash
debugctl status
debugcti enable
debugcti disable

```

## Init in the application

```python
... # your imports

from fastapi_debug_toolkit.fastapi_debug_toolkit import debug_router

... # your code

if settings.DEBUG_ROUTES_ENABLED:
    include_debug_docs = settings.ENVIRONMENT == "local"
    app.include_router(
        debug_router, prefix="/debug", include_in_schema=include_debug_docs
    )
```

---
