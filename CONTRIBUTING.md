# Contributing

Refer to the [Ansible community guide](https://docs.ansible.com/ansible/devel/community/index.html).

## Commit and pull request titles

Releases are automated with [release-please](https://github.com/googleapis/release-please), which
derives the next version and the `CHANGELOG.md` entries from commit messages. Pull requests are
squash-merged, so the **pull request title** becomes the commit message and must follow
[Conventional Commits](https://www.conventionalcommits.org/):

```
<type>[optional scope]: <description>
```

`.github/workflows/check-pr.yml` enforces this. Accepted types are `feat`, `fix`, `chore`, `docs`,
`refactor`, `test`, `ci`, `build`, `perf`, `style` and `revert`. `feat` bumps the minor version,
`fix` bumps the patch version, and a `!` after the type (or a `BREAKING CHANGE:` footer) bumps the
major version. Only `feat` and `fix` appear in the changelog by default.

## Releasing

Merging to `main` makes release-please open or update a release pull request that bumps
`version` in `galaxy.yml` and `.release-please-manifest.json` and updates `CHANGELOG.md`. Merging
that pull request tags the release and publishes the collection to Ansible Galaxy via
`.github/workflows/publish.yml`.
