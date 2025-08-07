-include ./Makefile.scm ./Makefile.setup

.PHONY: help
help: help-debug help-scm help-setup

#
help-debug:
	@echo "FASTAPI_DEBUG_TOOLKIT: Available targets:"
	@echo "  None"
