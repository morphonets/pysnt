# Makefile for Sphinx documentation

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD  ?= sphinx-build
SOURCEDIR    = .
BUILDDIR     = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Generate API documentation
api:
	@echo "Generating API documentation..."
	python ../dev/scripts/generate_api_docs.py

# Clean build directory
clean:
	@echo "Cleaning build directory..."
	rm -rf $(BUILDDIR)
	rm -rf api_auto

# Build HTML documentation
html: api
	@echo "Building HTML documentation..."
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Build HTML and open in browser
html-open: html
	@echo "Opening documentation in browser..."
	@python -c "import webbrowser; webbrowser.open('file://$(PWD)/$(BUILDDIR)/html/index.html')"

# Live reload server for development
livehtml:
	@echo "Starting live reload server..."
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)

# Check for broken links
linkcheck:
	@$(SPHINXBUILD) -M linkcheck "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)