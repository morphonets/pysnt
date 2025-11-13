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

# Generate enhanced API documentation with method index
enhanced-api:
	@echo "Generating enhanced API documentation with method index..."
	python ../dev/scripts/generate_enhanced_api_docs.py

# Integrated build process (standard + enhanced)
integrated-api:
	@echo "Running integrated API documentation build..."
	python ../dev/scripts/build_integration.py

# Clean build directory
clean:
	@echo "Cleaning build directory..."
	rm -rf $(BUILDDIR)
	rm -rf api_auto

# Build HTML documentation
html: api
	@echo "Building HTML documentation..."
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Build HTML documentation with method index
html-enhanced: enhanced-api
	@echo "Building HTML documentation with method index..."
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Build HTML documentation with integrated process (recommended)
html-integrated: integrated-api
	@echo "Building HTML documentation with integrated API generation..."
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Build HTML and open in browser
html-open: html
	@echo "Opening documentation in browser..."
	@python -c "import webbrowser; webbrowser.open('file://$(PWD)/$(BUILDDIR)/html/index.html')"

# Build HTML and open in browser
html-enhanced-open: html-enhanced
	@echo "Opening enhanced documentation in browser..."
	@python -c "import webbrowser; webbrowser.open('file://$(PWD)/$(BUILDDIR)/html/index.html')"

# Build integrated HTML and open in browser (recommended)
html-integrated-open: html-integrated
	@echo "Opening integrated documentation in browser..."
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
