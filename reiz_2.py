class Branch:
    def __init__(self):
        self.branches = []

def compute_depth(branch):
    # Depth 1 if no sub branches
    if not branch.branches:
        return 1

    # Return the max depth
    return max(calculate_depth(sub_branch) for sub_branch in branch.branches) + 1

# Create structure
root = Branch()
for i in range(3):
    branch1 = Branch()
    for j in range(2):
        branch2 = Branch()
        for k in range(4):
            branch3 = Branch()
            branch2.branches.append(branch3)
        branch1.branches.append(branch2)
    root.branches.append(branch1)

depth = compute_depth(root)
print("Depth of structure:", depth)