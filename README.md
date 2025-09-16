# fastapi_debug_toolkit

Debug and diagnostics toolkit for FastAPI apps based on [full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template/tree/master)
Provided as editable installable Python module. The project is packaged with [uv](https://docs.astral.sh/uv/) package and project manager. And uses git submodule system.

![Debuctl animated demo](../assets/debugctl-demo.gif?raw=true "Debuctl demo")

---

## Installation

### The first step

If you have GNU Make >= 4.0, then download and execute <https://raw.githubusercontent.com/Zigr/fastapi_debug_toolkit/refs/heads/master/scripts/download.sh> or:

```bash
cd $PROJECT_BASE directory
curl -LO https://raw.githubusercontent.com/Zigr/fastapi_debug_toolkit/refs/heads/master/scripts/download.sh

```

This will download package makefile(Makefile.fastapi_debug_toolkit) and makefile config  variables file(fastapi_debug_toolkit.config.mk)

### The second step

Download makefile(s)

```bash
chmod a+x ./download.sh
./download

```

This will download **fastapi_debug_toolkit** package makefile(**Makefile.fastapi_debug_toolkit**) and makefile config  variables file(**fastapi_debug_toolkit.config.mk**)

### The third step

- Review makefile config  variables file(**fastapi_debug_toolkit.config.mk**)
- Run makefile help:

```bash
make --file=Makefile.fastapi_debug_toolkit help

```

- Adjust variables in the variables file(**fastapi_debug_toolkit.config.mk**) according to your needs

### The forth step

Add repo as a git submodule and install **fastapi_debug_toolkit** package

```bash
make --file=Makefile.fastapi_debug_toolkit submodule-add
make --file=Makefile.fastapi_debug_toolkit install

```

### The fifth step

Add new environment variable to your main .env file as well as to PydanticSettings, if you used Pydantic.

```text
DEBUG_ROUTES_ENABLED=false

```

Then you may switch DEBUG_ROUTES_ENABLED variable by means of **debugctl** CLI locally(not in the Docker) for **EVVIRONMENT=local**.

### The seventh step: init package in the main application

```python(main script)
... # your own imports

try:
    from fastapi_debug_toolkit import debug_router

    if debug_router:
    if settings.DEBUG_ROUTES_ENABLED:
        include_debug_docs = settings.ENVIRONMENT == "local"
        app.include_router(
            debug_router, prefix="/debug", include_in_schema=include_debug_docs
        )
except ImportError:
    # Code to execute if desired_package is not found
    print("desired_package not found. Functionality may be limited.")
    debug_router = None  # Or provide a mock object/alternative implementation

... # another your code

```

## Notes

- ⚠️ You may rename **Makefile.fastapi_debug_toolkit** to **Makefile** simply to get rid of additional make parameters and long filename. Or put it in another folder(see: **make --help**)

- ⚠️ After package installation is done Dockerfile **changes** should be made as well to copy installed files in a container. This may be done by two ways:

- via volume bind moun FOR THE PACKAGE + copying to container, if you install packages folder as a app/ subling folder(default in the makefile example)
- or simply by copying extra folder in container, if you choose an app/ folder as a package parent.

## Testing

```bash
pytest backend/packages/fastapi-debug-toolkit/tests/

```

## Use: debug some configuration

```bash
docker compose wath # if you do not start it yet
# Then in another terminal window:
docker compose ps;
docker compose logs backend;

```

## Enable / disable routes debug in local environment

```bash
cd $PROJECT_BASE/YOUR_BACKEND_BASE # the folder with your .venv
debugctl status
debugcti enable
debugcti disable

```

Then we may ckeck debug endpoints:

```bash
curl http://127.0.0.1:8000/debug/routes         # List all registered routes and tags
curl http://127.0.0.1:8000/debug/config         # Expose current app settings (DEV ONLY)
curl http://127.0.0.1:8000/debug/middlewares    # List all middleware classes (DEV ONLY)
curl http://127.0.0.1:8000/debug/events         # List startup and shutdown event handlers (DEV ONLY)
curl http://127.0.0.1:8000/debug/mounts         # LList all mounted sub-apps (DEV ONLY)

```

 ---
