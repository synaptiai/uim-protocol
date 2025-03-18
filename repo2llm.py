import os
from pathlib import Path
import datetime
import argparse

# Default ignore patterns
DEFAULT_IGNORE_PATTERNS = {
    # System and IDE files/folders
    '.git',
    '.gitignore',
    '.dockerignore',
    '.flake8',
    '__pycache__',
    '.pytest_cache',
    '.pyproject.toml',
    '.env',
    'venv',
    'node_modules',
    'LICENSE',
    '.idea',
    '.vscode',
    '.DS_Store',

    # Custom ignores
    'run.sh',
    'repo2llm.py',
    'data/',
    'src/cache',
    'scripts/',
    'utils/',
    'tests/',
    'input/',
    'output/'
}

# Documentation file extensions
DOC_EXTENSIONS = {
    '.md',
    '.rst',
    '.txt',
    '.doc',
    '.docx',
    '.pdf',
    '.wiki',
    '.adoc',  # AsciiDoc
    '.org',   # Org mode
    '.rtf'
}

def should_ignore(path, ignore_patterns, ignore_docs=False):
    """Check if a path should be ignored"""
    path_str = str(path)

    # Check if it's a documentation file
    if ignore_docs and Path(path_str).suffix.lower() in DOC_EXTENSIONS:
        return True

    for pattern in ignore_patterns:
        # Handle directory patterns (ending with /)
        if pattern.endswith('/'):
            if pattern[:-1] in path_str.split(os.sep):
                return True
        # Handle file patterns
        elif pattern in path_str:
            return True
    return False

def create_file_structure(path, prefix="", ignore_patterns=None, ignore_docs=False):
    """Creates a tree-like structure of the directory"""
    if ignore_patterns is None:
        ignore_patterns = DEFAULT_IGNORE_PATTERNS

    output = []

    try:
        # Get and sort directory contents
        entries = sorted(list(os.scandir(path)), key=lambda x: (not x.is_dir(), x.name))
        filtered_entries = [
            entry for entry in entries
            if not should_ignore(entry.path, ignore_patterns, ignore_docs)
        ]

        for idx, entry in enumerate(filtered_entries):
            is_last = idx == len(filtered_entries) - 1
            connector = "└── " if is_last else "├── "

            output.append(f"{prefix}{connector}{entry.name}")

            if entry.is_dir():
                # Extend prefix for subdirectories
                extension = "    " if is_last else "│   "
                output.extend(create_file_structure(
                    entry.path,
                    prefix + extension,
                    ignore_patterns,
                    ignore_docs
                ))

    except PermissionError:
        output.append(f"{prefix}!── Access Denied")

    return output

def process_directory(directory_path, output_file, ignore_patterns=None, ignore_docs=False):
    """Process directory and create consolidated file"""
    directory_path = Path(directory_path)

    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write(f"# Project Directory Analysis\n")
        f.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        # Write ignore patterns
        f.write("## Ignored Patterns\n")
        f.write("```\n")
        for pattern in sorted(ignore_patterns):
            f.write(f"- {pattern}\n")
        if ignore_docs:
            f.write("\nDocumentation files ignored (extensions):\n")
            for ext in sorted(DOC_EXTENSIONS):
                f.write(f"- *{ext}\n")
        f.write("```\n\n")

        # Write file structure
        f.write("## Directory Structure\n")
        f.write("```\n")
        f.write(f"./{directory_path.name}\n")
        structure = create_file_structure(
            directory_path,
            ignore_patterns=ignore_patterns,
            ignore_docs=ignore_docs
        )
        f.write("\n".join(structure))
        f.write("\n```\n\n")

        # Process all files
        f.write("## File Contents\n\n")

        for root, _, files in os.walk(directory_path):
            # Skip ignored directories
            if should_ignore(root, ignore_patterns, ignore_docs):
                continue

            for file_name in sorted(files):
                file_path = Path(root) / file_name

                # Skip ignored files
                if should_ignore(file_path, ignore_patterns, ignore_docs):
                    continue

                try:
                    # Get relative path for display
                    rel_path = file_path.relative_to(directory_path)

                    # Get file info
                    file_stats = file_path.stat()
                    file_size = file_stats.st_size / 1024  # Convert to KB
                    mod_time = datetime.datetime.fromtimestamp(file_stats.st_mtime)

                    # Write file header
                    f.write(f"### File: {rel_path}\n")
                    f.write("```\n")
                    f.write(f"Path: {rel_path}\n")
                    f.write(f"Size: {file_size:.2f} KB\n")
                    f.write(f"Last Modified: {mod_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("```\n\n")

                    # Write file contents
                    f.write("**Contents:**\n")
                    f.write("```\n")
                    try:
                        with open(file_path, 'r', encoding='utf-8') as source_file:
                            f.write(source_file.read())
                    except UnicodeDecodeError:
                        f.write("[Binary file or non-UTF-8 encoding]\n")
                    except Exception as e:
                        f.write(f"[Error reading file: {str(e)}]\n")
                    f.write("```\n\n")

                except Exception as e:
                    f.write(f"[Error processing {file_name}: {str(e)}]\n\n")

                f.write("-" * 80 + "\n\n")

def load_ignore_patterns(ignore_file=".llmignore"):
    """Load custom ignore patterns from file"""
    patterns = set(DEFAULT_IGNORE_PATTERNS)

    if os.path.exists(ignore_file):
        with open(ignore_file, 'r') as f:
            custom_patterns = {line.strip() for line in f if line.strip() and not line.startswith('#')}
            patterns.update(custom_patterns)

    return patterns

def main():
    parser = argparse.ArgumentParser(description='Convert directory contents to LLM-friendly format')
    parser.add_argument('-d', '--directory', default='.', help='Directory to process (default: current directory)')
    parser.add_argument('-o', '--output', default='llm_context.md', help='Output file (default: llm_context.md)')
    parser.add_argument('--ignore-docs', action='store_true', help='Ignore documentation files (.md, .rst, etc.)')

    args = parser.parse_args()

    # Load ignore patterns
    ignore_patterns = load_ignore_patterns()

    try:
        process_directory(
            args.directory,
            args.output,
            ignore_patterns=ignore_patterns,
            ignore_docs=args.ignore_docs
        )
        print(f"\nSuccessfully created {args.output}")
        if args.ignore_docs:
            print("Documentation files were ignored")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
