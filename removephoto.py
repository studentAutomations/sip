from github import Github

# Replace with your GitHub access token
access_token = 'YOUR_GITHUB_ACCESS_TOKEN'
repo_name = 'studentAutomations/sip'  # Your repository name
file_path = 'sip-nova-obavestenja.png'  # Path of the file in the repo

# Authenticate with GitHub
g = Github(access_token)

# Get the repository
repo = g.get_repo(repo_name)

# Get the file and delete it
try:
    # Get the file content
    contents = repo.get_contents(file_path)

    # Delete the file
    repo.delete_file(contents.path, "Deleting photo", contents.sha)
    print(f"Deleted: {file_path} from {repo_name}")
except Exception as e:
    print(f"Error: {str(e)}")
