#!/bin/bash

# Build the documentation site
echo "Building UIM Protocol documentation site..."
mkdocs build

# Check if the build was successful
if [ $? -eq 0 ]; then
    echo "Documentation built successfully!"
    echo "The site is available in the 'site' directory."
    echo "To serve the site locally, run: mkdocs serve"
    echo "To deploy the site to GitHub Pages, run: mkdocs gh-deploy"
else
    echo "Error building documentation."
    exit 1
fi
