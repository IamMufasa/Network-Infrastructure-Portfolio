# GitHub Upload Preparation

This document provides instructions for initializing a Git repository and preparing the network infrastructure portfolio for GitHub upload.

## Prerequisites

Before uploading to GitHub, ensure you have:

1. A GitHub account
2. Git installed on your local machine
3. The network infrastructure portfolio files on your local machine

## Git Repository Setup

Follow these steps to initialize a Git repository and prepare for upload:

```bash
# Navigate to the project directory
cd /path/to/network-infrastructure-portfolio

# Initialize a new Git repository
git init

# Add all files to the staging area
git add .

# Create an initial commit
git commit -m "Initial commit: Network Infrastructure Portfolio"
```

## GitHub Repository Creation

1. Log in to your GitHub account
2. Click on the "+" icon in the top-right corner and select "New repository"
3. Enter "network-infrastructure-portfolio" as the repository name
4. Add a description: "A comprehensive portfolio demonstrating network engineering skills for the Network Engineer I position"
5. Choose "Public" visibility (or Private if preferred)
6. Do NOT initialize the repository with a README, .gitignore, or license
7. Click "Create repository"

## Connecting Local Repository to GitHub

After creating the GitHub repository, you'll see instructions to push an existing repository. Use the following commands:

```bash
# Add the remote GitHub repository
git remote add origin https://github.com/yourusername/network-infrastructure-portfolio.git

# Push your local repository to GitHub
git push -u origin main
# Note: If your default branch is "master" instead of "main", use:
# git push -u origin master
```

## Verifying the Upload

1. Refresh your GitHub repository page
2. Ensure all files and directories are visible
3. Check that the README.md is displayed on the repository homepage
4. Verify that the directory structure matches your local project

## GitHub Pages Setup (Optional)

To showcase your portfolio website using GitHub Pages:

1. Go to your repository on GitHub
2. Click on "Settings"
3. Scroll down to the "GitHub Pages" section
4. Under "Source", select "main" branch and "/src" folder
5. Click "Save"
6. After a few minutes, your site will be available at https://yourusername.github.io/network-infrastructure-portfolio/

## Best Practices for Maintaining the Repository

1. Keep your repository up-to-date with regular commits
2. Use meaningful commit messages
3. Create branches for new features or significant changes
4. Use pull requests for code reviews
5. Add a LICENSE file if you want to specify how others can use your code
6. Update the README.md as your project evolves

## Troubleshooting Common Issues

- **Authentication issues**: Ensure you've configured your GitHub credentials correctly
- **Push rejected**: Pull the latest changes before pushing (`git pull origin main`)
- **Large files**: Avoid committing large binary files; consider using Git LFS if necessary
- **Sensitive information**: Ensure no sensitive information (passwords, API keys) is included in your repository
