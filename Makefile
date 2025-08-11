-include ./Makefile.scm
-include ./Makefile.setup

# Formatting
BOLD=\033[1m
GREEN=\033[32m
BLUE=\033[34m
YELLOW=\033[0;33m
RED=\033[31m
CYAN=\033[36m
MAGENTA=\033[35m
RESET=\033[0m
LINE=-----------------------------

.PHONY: help help-main help-scm help-setup
help: help-main help-scm help-setup

#
help-main:
	@echo "FASTAPI_DEBUG_TOOLKIT: Available targets:"
	@echo "  None"
