import os
import subprocess

os.environ['GIT_INDEX_FILE'] = '.git/temp_index'
subprocess.run(['git', 'read-tree', 'origin/main'])

result = subprocess.run(['git', 'ls-tree', '-r', '-z', 'origin/main'], capture_output=True)
items = result.stdout.split(b'\x00')

for item in items:
    if not item: continue
    meta, path = item.split(b'\t', 1)
    if b':' in path:
        mode, type_, sha1 = meta.split(b' ')
        new_path = path.replace(b':', b'-')
        
        # Remove old path
        p1 = subprocess.run(['git', 'update-index', '--remove', '-z', '--index-info'], input=b'0 0000000000000000000000000000000000000000\t' + path + b'\x00')
        # Add new path
        p2 = subprocess.run(['git', 'update-index', '--add', '--cacheinfo', f'{mode.decode()},{sha1.decode()},{new_path.decode()}'])

# Write tree
tree_result = subprocess.run(['git', 'write-tree'], capture_output=True, text=True)
tree_sha = tree_result.stdout.strip()

# Commit
commit_msg = "Fix invalid filenames with colons for Windows compatibility"
commit_result = subprocess.run(['git', 'commit-tree', tree_sha, '-p', 'origin/main', '-m', commit_msg], capture_output=True, text=True)
commit_sha = commit_result.stdout.strip()

# Print the new commit SHA
print("New commit SHA:", commit_sha)

# Update a temporary branch
subprocess.run(['git', 'branch', '-f', 'fix-colons', commit_sha])
