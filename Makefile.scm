# Submodule repository. 
# Make sure repo name and package name are the same
PACKAGE_REPO=https://github.com/your-org/fastapi-debug-toolkit

# Project paths, relative to ./backend folder
PACKAGE_PATH=./backend/packages/fastapi-debug-toolkit

# Package manager executable (customize if needed)
PKG_MANAGER=uv

.PHONY: help-scm submodule-add submodule-init dev-clean

help-scm:
	@printf "$${BOLD}SCM: Available targets:$${RESET}\n"
	@printf "${CYAN}$(LINE)${RESET}\n"
	@echo "  submodule-add         - Add Git submodule(s) from PACKAGE_REPO to PACKAGE_PATH"
	@echo "  submodule-init        - Initialize Git submodules recursively"
	@echo "  dev-clean             - Clean up .pyc, __pycache__, .mypy_cache, etc."
	@echo

submodule-add:
	git submodule add $(PACKAGE_REPO) $(PACKAGE_PATH)

submodule-init:
	git submodule update --init --recursive


dev-clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '.mypy_cache' -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
