include ../Makefile.setup
include ../Makefile.scm

.PHONY: help
help: help-debug help-setup help-scm

#
help-debug:
	@echo "FASTAPI_DEBUG_TOOLKIT: Available targets:"
	@echo "  None"
