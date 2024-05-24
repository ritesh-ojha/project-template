import os

def create_issue_template(serial_number):
    template = f"""### Issue Description

[Please provide a brief description of the issue or task.]

### Expected Behavior

[Describe what behavior you expect to see.]

### Actual Behavior

[Describe what behavior you are actually seeing.]

### Steps to Reproduce

[Provide steps to reproduce the issue, if applicable.]

1. Step 1
2. Step 2
3. ...

### Additional Information

[Any additional information or context that might be helpful in resolving the issue.]

### Related Files or Documentation

[Provide links or references to any relevant files or documentation.]

### Environment

- Operating System: [e.g., Windows, Linux, macOS]
- Python Version: [if applicable]
- Database: [if applicable]
- Other relevant software/tools: [if applicable]
"""
    return template

def update_all_issues_file(issue_number, issue_description):
    all_issues_file_path = "all_issues.md"
    with open(all_issues_file_path, "a") as all_issues_file:
        all_issues_file.write(f"- [ISSUE{issue_number}](ISSUE/ISSUE{issue_number}.md): {issue_description}\n")

def main():
    # Create ISSUE directory if it doesn't exist
    if not os.path.exists("ISSUE"):
        os.makedirs("ISSUE")

    # Create or open all_issues.md file
    all_issues_file_path = "all_issues.md"
    if not os.path.exists(all_issues_file_path):
        with open(all_issues_file_path, "w") as all_issues_file:
            all_issues_file.write("# All Issues\n")

    # Prompt user for information
    issue_description = input("Enter a brief description of the issue or task: ")

    # Generate issue number
    issue_number = 1
    if os.path.exists(all_issues_file_path):
        with open(all_issues_file_path, "r") as all_issues_file:
            lines = all_issues_file.readlines()
            if lines:
                last_line = lines[-1]
                if "[ISSUE" in last_line:
                    last_issue_number = int(last_line.split("[ISSUE")[1].split("]")[0])
                    issue_number = last_issue_number + 1

    # Generate issue template
    issue_template = create_issue_template(f"ISSUE{issue_number:02d}")

    # Fill in issue template with user input
    issue_template = issue_template.replace("[Please provide a brief description of the issue or task.]", issue_description)

    # Write issue template to file
    issue_filename = f"ISSUE{issue_number:02d}.md"
    issue_path = os.path.join("ISSUE", issue_filename)
    with open(issue_path, "w") as file:
        file.write(issue_template)

    print(f"Issue template created successfully at '{issue_path}'.")

    # Update all_issues.md file
    update_all_issues_file(issue_number, issue_description)

if __name__ == "__main__":
    main()
