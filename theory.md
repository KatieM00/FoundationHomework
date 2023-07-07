<h1 style="text-align: center; ">Task Two

### Question 1
*Fill in the blank*:

Git is an example of a _**version control**_ system.

### Question 2
*Name a code hosting service that uses Git*
- GitHub
- GitLab
- BitBucket
- SourceForge

### Question 3
*There are 3 states in Git that files can be in. What are these states?*

1. **Modified**: Indicates the filed has been modified since the last commit.
2. **Staged**: When a modified files is marked for inclusiong in the next commit, it is in the *staged* state.
3. **Committed**: Once the changes have been committed, the file is in the *committed state*. This means the changes are permanently saved in the Git repository.

### Question 4
*PR and repo are common abbreviations in the world of Git. What do they mean?*

1. **PR**: *Pull Request* is a way fr developers to propose changes, provide feedback, and eventually merge the proposed changes into the main codebase.
2. **Repo**: *Repo* is short for *repository* and is a central location where the codebase and its version history are stored in Git.

### Question 5
*What is the git command that updates the local repository with changes from the
remote repository?*

`git pull` 

### Question 6
*What is the git command that gets the changes from the remote repository but
doesn’t update your local repository?*

`git fetch`

### Question 7
*What is the git command that updates the remote repository with local repository
code?*

`git push`

### Question 8
*What does the git commit command need to work?*

The `git commit` command requires two key components to work:
1. **Staged Changes**:
   Before committing, you must stage the changes you want to include in the commit. You use `git add` to add specific files or, to add all modified files,`git add --all` or `git add _`.
2. **Commit Message**:
    
    A brief description that summarises the changes made in the commit. It is important to provide a meaningful and descriptive commit message to document the purpose or intention behind the changes. The *commit* message is entered along with the `git commit` command using the `-m` option.








