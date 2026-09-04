# Micromamba Ansible Role

This Ansible role installs and configures micromamba, a lightweight and fast package manager for conda environments.

## Requirements

* ansible-core >= 2.19 (see `meta/runtime.yml` of this collection)
* Root privileges on the target host: the role writes to `/etc/profile.d`, `/etc/conda` and the configured install path.

## Role Variables

The following variables are available to customize the role:

* `micromamba_destination`: The path where the micromamba binary is installed. <br>
    Default: `/usr/local/bin/micromamba`
* `micromamba_root_prefix`: Root directory for micromamba, exported as `MAMBA_ROOT_PREFIX`. <br>
    Default: `/opt/micromamba`
* `micromamba_default_channels`: Channels written to `/etc/conda/condarc`. <br>
    Default: `[conda-forge, bioconda]`
* `micromamba_envs_dirs`: Directories where environments are created. Written to `/etc/conda/condarc` and created on the host. <br>
    Default: `[/opt/conda_env]`
* `micromamba_version`: Currently has no effect. The role always installs the latest release from
    [micromamba-releases](https://github.com/mamba-org/micromamba-releases) and verifies it against the
    published SHA256 checksum. <br>
    Default: `latest`

## Exported facts

The role sets `mamba_exe` to `micromamba_destination`, unless `mamba_exe` is already defined by a
higher-precedence variable (for example a group or host variable). Pass it straight to the
`conda_env` module:

```yaml
- name: Create an environment
  hoeze.conda.conda_env:
    name: myenv
    mamba_exe: "{{ mamba_exe }}"
    spec: "{{ lookup('file', 'environment.yml') | from_yaml }}"
```

## Example

### In a playbook

```yaml
---
- name: Install micromamba
  hosts: all
  become: true
  roles:
    - hoeze.conda.micromamba
  vars:
    micromamba_destination: "/usr/local/bin/micromamba"
```

### As a dependency

This role can be used as a dependency in other roles:

```yaml
---
dependencies:
  - role: hoeze.conda.micromamba
    when: install_micromamba | default(false)
```
