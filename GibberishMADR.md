---
title: Identify a safe method for secret storage
status: accepted
date: 2026-02-10
decision-makers:
  - Tess
consulted:
  - '[Dr. Starr](https://www.github.com/joecstarr)'
informed:
  - ???
---

## Context and Problem Statement

The current TTS system used in the project has been deemed insufficient. We have instead decided to
use the 11labs ML TTS product. Unfortunately, this product can't be run locally and must be accessed
from a web API. Accessing the API requires authentication against a secret key. Currently we are
using a free key but intend to use a paid key in the future. With this in mind we need to store the
key securely.

## Decision Drivers

- The key needs to be secure. Meaning usable and available only to stakeholders who need it.
- Granting access to a stakeholder must be simple.
- Removing access from a stakeholder must be simple.
- Stakeholders may need access to the key while not in the office.

## Considered Options

- Raw committing the key to the repo.
- Using a password manager.
- Putting the key in a file on a network drive/sharepoint.
- Using a git compatible secret store:
    - [git crypt](https://github.com/AGWA/git-crypt)
    - [sops](https://github.com/getsops/sops)

## Decision Outcome

We have decided to use the sops toolchain for secret storage.

### Consequences

For safety we will adopt the following conventions:

- Secrets shall be added to the `.sops/*` directory.
- Secrets shall be in `yaml`.
- Encrypted secrets shall have the suffix `.enc.yaml` or `.enc.yml`.


- A pre-commit hook shall verify any `yaml` file being committed is encrypted
- The `.sops/*` directory shall be added to `.gitignore` with positive filter for encrypted `yaml`
  as `!.sops/*.enc.yaml` and `!.sops/*.enc.yml`.
- Files shall be encrypted with [age](https://github.com/FiloSottile/age) and GitHub listed public
  keys.
- Access to secrets shall follow the
  [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege).
- When revoking access to the secret a new key shall be generated and the old key revoked.

## Pros and Cons of the Options

### Raw committing the key to the repo.

- Good, the simplest solution.
- Good, very easy to pass the secret.
- Good, easy to access off campus.
- Bad, can never make the project code public.
- Bad, extremely likely we will make a mistake.

### Using a password manager.

- Good, very secure storage.
- Good, easy to pass secrets.
- Good, can store multiple secrets.
- Bad, may be challenging to integrate in the project safely.
- Bad, new developers are likely to copy the key into the project raw.
- Bad, may be difficult to access off campus.

### Putting the key in a file on a network drive/sharepoint.

- Good, easy to grant access to secrets.
- Bad, difficult to make sure only the right people have access.
- Bad, versioning of the key is very hard.
- Bad, may be difficult to access off campus.

### Using the git compatible secret store:

- Good, easy to pass the secret.
- Good, easy to access off campus.
- Good, easy to add new users.
- Good, commonly used solution so community support is available.
- Bad, may be difficult to set up the tooling.
- Bad, some risk that secret gets put into the repository accidentally.
- Bad, challenging to revoke access from users. Requires generation of new key.

#### [git crypt](https://github.com/AGWA/git-crypt)

- Good, application simple to install.
- Bad, uses gpg which is hard to set up.
- Bad, doesn't have a stable long term support release.
- Bad, use is not as popular so support isn't great.

#### [sops](https://github.com/getsops/sops)

- Good, supports age which allows use of ssh keys.
- Good, developed by The Linux Foundation so long term maintenance is likely.
- Good, a popular solution so support is available.
- Bad, setting up requires multiple tools and multiple files.
