# Dev's Logbook

## Repository Ruleset for this project

### Branching Strategy

#### Main Branch Protection

- The `main` branch is protected and read-only. No direct commits are allowed.
- This branch is reserved for milestone releases and stable versions only.

#### Development Branch

- A `dev` branch is used for ongoing development and integration.
- All feature branches are merged into `dev` after review and testing.

#### Creating New Branches

- All work should be done on separate branches.
- Branch names should follow the format: `{type}_{short-description}`
  - **Types**:
    - `feature`: New features or enhancements (e.g., `feature_add-login`)
    - `bugfix`: Fixes for bugs (e.g., `bugfix_fix-login-error`)
    - `hotfix`: Critical fixes that need to be released immediately (e.g., `hotfix_security-vulnerability`)
    - `chore`: Routine tasks and maintenance (e.g., `chore_update-dependencies`)
    - `refactor`: Code improvements without changing functionality (e.g., `refactor_cleanup-auth-module`)

### Commit Message Guidelines

#### Structure

- Commit messages should be concise and follow this format:

```txt
{Type}: Short Description

Detailed explanation of the changes, if necessary.
```

- **Types**:
  - `feat`: A new feature
  - `fix`: A bug fix
  - `docs`: Documentation changes
  - `style`: Code style changes (formatting, missing semi-colons, etc.)
  - `refactor`: Code refactoring
  - `perf`: Performance improvements
  - `test`: Adding or updating tests
  - `chore`: Maintenance or minor updates
- Example:

  ```txt
  feat: add user authentication

  Implemented login, logout, and signup functionalities using JWT.
  ```

#### Best Practices

- Use the imperative mood (e.g., "Add", "Fix", "Update").
- Keep the subject line (first line) under 50 characters.
- Use the body to explain "what" and "why" instead of "how" if the change is not trivial.
