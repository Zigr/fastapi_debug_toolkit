# fastapi_debug_toolkit

---

Debug and diagnostics toolkit for FastAPI apps based on [full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template/tree/master)
Provided as editable installable Python module. The is packaged with [uv](https://docs.astral.sh/uv/) package and project manager.

## Installation

---
⚠️ If installed **as is** from the **current repo**, Dockerfile **changes** should be made as well.

---

### Using GNU make tool and Git with fastapi_debug_toolkit in place

Assume, we have a project root folder with $PROJECT_BASE in **./ai-agent**

```bash
export PROJECT_BASE="$(pwd)/ai-agent" && cd $PROJECT_BASE;
<!-- # We do not have repo installed in a local path
#  make --makefile=./backend/app/packages/fastapi_debug_toolkit/Makefile -I $(pwd)/backend/app/packages/fastapi_debug_toolkit help
# make \
# --makefile=./backend/app/packages/fastapi_debug_toolkit/Makefile  \
# -I $(pwd)/backend/app/packages/fastapi_debug_toolkit \
#  submodule-add --force \
#  PACKAGE_REPO=https://github.com/Zigr/fastapi_debug_toolkit/ \
#  PACKAGE_PATH=./backend/packages/fastapi-debug-toolkit -->

```

### Instal from Git repo

Assuming we did the steps above and we are in PROJECT_BASE directory:

#### With defaults

```bash
make submodule-add;
make install;

```

#### Install as editable package with user defined variables

⚠️ The best way to install deps with customizations is to examine $(PROJECT_BASE)/Makefile file. Or use:

```bash
make help
# OR which is equivalnent to
make
# OR
make list-user-variables
# OR
make debug-vvv

```

See available user defined variables:

```bash
make list-user-variables
# OR debug-verbose
make debug-vvv

```

And then define required variables.
Example:

```bash
make list-user-variables;
make submodule-add PACKAGE_REPO=https://github.com/Zigr/fastapi_debug_toolkit   PACKAGE_PATH=./backend/packages/fastapi-debug-toolkit;
make install PACKAGE_PATH="./packages/fastapi-debug-toolkit";
docker compose watch;

```

## Testing

```bash
pytest backend/packages/fastapi-debug-toolkit/tests/

```

## Use: debug some configuration

Let us assume we have backend service running after previous step.

```bash
docker compose ps;
docker compose logs backend;

```

Then we may ckeckdebug endpoints:

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

```python(main script)
... # your imports

try:
    from fastapi_debug_toolkit import debug_router
    # Code that uses desired_package can go here
except ImportError:
    # Code to execute if desired_package is not found
    print("desired_package not found. Functionality may be limited.")
    debug_router = None  # Or provide a mock object/alternative implementation


... # your code

if debug_router:
    if settings.DEBUG_ROUTES_ENABLED:
        include_debug_docs = settings.ENVIRONMENT == "local"
        app.include_router(
            debug_router, prefix="/debug", include_in_schema=include_debug_docs
        )
```

---
