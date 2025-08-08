-include ./Makefile.scm
-include ./Makefile.setup

.PHONY: help
help: help-debug help-scm help-setup debug

# Print debug information about the Makefile and environment
help-debug:
	@printf "${BOLD}FASTAPI_DEBUG_TOOLKIT: Available targets:${RESET}\n"
	@printf "${CYAN}$(LINE)${RESET}\n"
	@echo "  debug            	- Print debug information about the Makefile and environment"
	@echo

debug:
	@echo SHELL = $(SHELL)
	@echo .ONESHELL = $(.ONESHELL)
	@echo CURDIR= $(CURDIR)
	@echo "Variables in Makefile:"
	@echo "PACKAGE_REPO = $(PACKAGE_REPO)"
	@echo "PACKAGE_PATH = $(PACKAGE_PATH)"
	@echo "PKG_MANAGER = $(PKG_MANAGER)"
	@echo "CUSTOM_DEPS = $(CUSTOM_DEPS)"
	# A special automatic variable in GNU Make that holds a list of all the Makefiles read so far, in order.
	# Each time a Makefile is loaded (including via include), its name is appended to this list.
	@echo MAKEFILE_LIST =  $(MAKEFILE_LIST)
