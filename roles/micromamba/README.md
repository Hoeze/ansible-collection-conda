# Micromamba Ansible Role

This Ansible role installs and configures micromamba, a lightweight and fast package manager for conda environments.

## Requirements

* Ansible 2.9 or later

## Role Variables

The following variables are available to customize the role:

* `micromamba_destination`: The path where micromamba will be installed. <br>
    Default: `conda_exe` if defined, otherwide `/usr/local/bin/micromamba`
* `micromamba_version`: The version of micromamba to be installed. <br>
    Default: "latest"


## Example


### In playbook

Here is an example playbook that uses this role:
```yaml
---
- name: Install micromamba
  hosts: all
  become: true
  roles:
    - micromamba
  vars:
    conda_exe: "/usr/local/bin/micromamba"
```

### As dependency
This role can be used as dependency in other roles:
```yaml
---
dependencies:
 - role: 'micromamba'
   when: install_micromamba
```
This role will conveniently export `conda_exe` to the `micromamba_destination` if it was not specified by higher priority variables (e.g. group or host variables).
