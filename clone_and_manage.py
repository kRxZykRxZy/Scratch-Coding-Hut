import os
import requests
import git
from pathlib import Path
import shutil

# Your GitHub repository URL and token
repo_url = "https://github.com/Scratch-Coding-Hut/Scratch-Coding-Hut"
token = os.environ["MY_GITHUB_TOKEN"]  # This is your PAT stored as a secret in GitHub

# Function to clone the repo using GitHub API
def clone_repo():
    # Clone the repo using GitPython (it can also clone using git command internally)
    repo_dir = Path("./Scratch-Coding-Hut")
    if repo_dir.exists():
        shutil.rmtree(repo_dir)  # Remove the old repo if it exists, but not the Python script
    git.Repo.clone_from(repo_url, repo_dir, depth=1)
    return repo_dir

# Function to copy files excluding the .github folder
def copy_files(src_dir, dest_dir):
    # Iterate over the source directory and copy files, skipping .github
    for item in os.listdir(src_dir):
        if item != ".github":  # Skip the .github folder
            src_path = src_dir / item
            dest_path = dest_dir / item
            if src_path.is_dir():
                shutil.copytree(src_path, dest_path)  # Copy directories
            else:
                shutil.copy2(src_path, dest_path)  # Copy files

# Main function
def main():
    # Step 1: Clone the repo
    src_repo_dir = clone_repo()

    # Step 2: Prepare the destination path (current repository)
    dest_repo_dir = Path(".")  # This is the current directory where the GitHub Action is running

    # Step 3: Copy files excluding .github folder
    copy_files(src_repo_dir, dest_repo_dir)

    # Step 4: Clean up - Remove the cloned repo directory if you don't need it anymore (excluding Python script)
    shutil.rmtree(src_repo_dir)

if __name__ == "__main__":
    main()
