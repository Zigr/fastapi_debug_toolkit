# Submodule repository.
# Make sure repo name and package name are the same
PACKAGE_REPO=https://github.com/your-org/fastapi-debug-toolkit

# Project paths, relative to project folder
PACKAGE_PATH=./backend/packages/fastapi-debug-toolkit

# Package manager executable (customize if needed)
PKG_MANAGER=uv

.PHONY: help-scm submodule-add dev-clean

help-scm:
	@printf "$${BOLD}SCM: Available targets:$${RESET}\n"
	@printf "${CYAN}$(LINE)${RESET}\n"
	@echo "  submodule-add         - Add Git submodule if not already added from PACKAGE_REPO to PACKAGE_PATH"
	@echo "  dev-clean             - Clean up .pyc, __pycache__, .mypy_cache, etc."
	@echo

# Add submodule if not already added
submodule-add:
	@if [ ! -d "$(PACKAGE_PATH)" ]; then \
		echo "$(YELLOW)Adding submodule $(PACKAGE_REPO) to $(PACKAGE_PATH)...$(RESET)"; \
		git submodule add $(PACKAGE_REPO) $(PACKAGE_PATH); \
		git submodule update --init --recursive; \
	else \
		echo "$(GREEN)Submodule $(PACKAGE_PATH) already exists. Skipping...$(RESET)"; \
	fi

dev-clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '.mypy_cache' -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
