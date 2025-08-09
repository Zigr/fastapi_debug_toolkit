from typing import Any

from fastapi import APIRouter, HTTPException, Request

# from app.core.config import settings
from fastapi_debug_toolkit.debugctl.util import get_env_settings

settings = get_env_settings()

router = APIRouter(tags=["debug"])

# Enable debug docs only in local environment
# This is useful for local development and testing
# but should be disabled in production for security reasons
# and to avoid exposing sensitive information
# to the public.
# In production, the debug routes will still be available
# but without the documentation in the OpenAPI schema.
# This is to prevent exposing sensitive information
# to the public and to avoid cluttering the API documentation.
include_debug_docs = settings["ENVIRONMENT"] == "local"


def dev_only():
    if settings["ENVIRONMENT"] != "local":
        raise HTTPException(status_code=403, detail="Access denied in production")


@router.get(
    "/config",
    summary="Expose current app settings (DEV ONLY)",
    include_in_schema=include_debug_docs,
)
def get_full_settings():
    dev_only()
    return settings


@router.get(
    "/routes",
    summary="List all registered routes and tags",
    include_in_schema=include_debug_docs,
)
def list_routes(request: Request):
    # dev_only()
    app = request.app
    routes_info: list[dict[str, Any]] = []

    for route in app.routes:
        if hasattr(route, "methods"):
            route_tags = getattr(route, "tags", [])
            routes_info.append(
                {
                    "path": route.path,
                    "name": route.name,
                    "methods": list(route.methods),
                    "endpoint": route.endpoint.__name__,
                    "include_in_schema": route.include_in_schema,
                    "tags": route_tags,
                }
            )

    return {"routes": routes_info}


@router.get(
    "/middlewares",
    summary="List all middleware classes (DEV ONLY)",
    include_in_schema=include_debug_docs,
)
def list_middlewares(request: Request):
    dev_only()
    app = request.app
    middlewares_info: list[dict[str, Any]] = []

    for middleware in app.user_middleware:
        middlewares_info.append(
            {
                "class": middleware.cls.__name__,
                "options": middleware.options,
            }
        )

    return {"middlewares": middlewares_info}


@router.get(
    "/events",
    summary="List startup and shutdown event handlers (DEV ONLY)",
    include_in_schema=include_debug_docs,
)
def list_event_handlers(request: Request):
    dev_only()
    app = request.app

    startup_handlers = [f.__name__ for f in app.router.on_startup]
    shutdown_handlers = [f.__name__ for f in app.router.on_shutdown]

    return {
        "on_startup": startup_handlers,
        "on_shutdown": shutdown_handlers,
    }


@router.get(
    "/mounts",
    summary="List all mounted sub-apps (DEV ONLY)",
    include_in_schema=include_debug_docs,
)
def list_mounted_apps(request: Request):
    dev_only()
    app = request.app
    mounts = []

    for route in app.routes:
        if hasattr(route, "app") and hasattr(route.app, "routes"):
            mounts.append(
                {
                    "mount_path": route.path,
                    "app_name": type(route.app).__name__,
                    "routes_count": len(route.app.routes),
                }
            )

    return {"mounted_apps": mounts}
