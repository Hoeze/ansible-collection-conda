# Conda role collection for Ansible
[![CI](https://github.com/Hoeze/ansible-collection-conda/actions/workflows/ansible-test.yml/badge.svg)](https://github.com/Hoeze/ansible-collection-conda/actions/workflows/ansible-test.yml) [![Codecov](https://img.shields.io/codecov/c/github/Hoeze/ansible-collection-conda)](https://codecov.io/gh/Hoeze/ansible-collection-conda)

<!-- Describe the collection and why a user would want to use it. What does the collection do? -->

## Our mission

<!-- Put your collection's mission statement in here. Example follows. -->

This collection provides Ansible modules and plugins for managing Conda environments, enabling users to automate the setup and maintenance of Conda-based environments.

## Code of Conduct

We follow the [Ansible Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html) in all our interactions within this project.

If you encounter abusive behavior, please refer to the [policy violations](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html#policy-violations) section of the Code for information on how to raise a complaint.

## Communication

<!--
If your collection is not present on the Ansible forum yet, please check out the existing [tags](https://forum.ansible.com/tags) and [groups](https://forum.ansible.com/g) - use what suits your collection. If there is no appropriate tag and group yet, please [request one](https://forum.ansible.com/t/requesting-a-forum-group/503/17).
-->

* Join the Ansible forum:
  * [Get Help](https://forum.ansible.com/c/help/6): get help or help others. Please add appropriate tags if you start new discussions, for example the `YOUR TAG` tag.
  * [Posts tagged with 'your tag'](https://forum.ansible.com/tag/YOUR_TAG): subscribe to participate in collection/technology-related conversations.
  * [Refer to your forum group here if exists](https://forum.ansible.com/g/): by joining the team you will automatically get subscribed to the posts tagged with [your group forum tag here](https://forum.ansible.com/tags).
  * [Social Spaces](https://forum.ansible.com/c/chat/4): gather and interact with fellow enthusiasts.
  * [News & Announcements](https://forum.ansible.com/c/news/5): track project-wide announcements including social events. The [Bullhorn newsletter](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn), which is used to announce releases and important changes, can also be found here.

For more information about communication, see the [Ansible communication guide](https://docs.ansible.com/ansible/devel/community/communication.html).

## Contributing to this collection

<!--Describe how the community can contribute to your collection. At a minimum, fill up and include the CONTRIBUTING.md file containing how and where users can create issues to report problems or request features for this collection. List contribution requirements, including preferred workflows and necessary testing, so you can benefit from community PRs. If you are following general Ansible contributor guidelines, you can link to - [Ansible Community Guide](https://docs.ansible.com/ansible/devel/community/index.html). List the current maintainers (contributors with write or higher access to the repository). The following can be included:-->

The content of this collection is made by people like you, a community of individuals collaborating on making the world better through developing automation software.

New contributors are actively accepted and all types of contributions are very welcome.

Don't know how to start? Refer to the [Ansible community guide](https://docs.ansible.com/ansible/devel/community/index.html)!

Want to submit code changes? Take a look at the [Quick-start development guide](https://docs.ansible.com/ansible/devel/community/create_pr_quick_start.html).

We also use the following guidelines:

* [Collection review checklist](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_reviewing.html)
* [Ansible development guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
* [Ansible collection development guide](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html#contributing-to-collections)

## Collection maintenance

The current maintainers are listed in the [MAINTAINERS](MAINTAINERS) file. If you have questions or need help, feel free to mention them in the proposals.

To learn how to maintain/become a maintainer of this collection, refer to the [Maintainer guidelines](https://docs.ansible.com/ansible/devel/community/maintainers.html).

It is necessary for maintainers of this collection to be subscribed to:

* The collection itself (the `Watch` button -> `All Activity` in the upper right corner of the repository's homepage).
* The [news-for-maintainers repository](https://github.com/ansible-collections/news-for-maintainers).

They also should be subscribed to Ansible's [The Bullhorn newsletter](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn).

## Governance

<!--Describe how the collection is governed. Here can be the following text:-->

The process of decision making in this collection is based on discussing and finding consensus among participants.

Every voice is important. If you have something on your mind, create an issue or dedicated discussion and let's discuss it!

## Tested with Ansible

<!-- List the versions of Ansible the collection has been tested with. Must match what is in galaxy.yml. -->

This collection has been tested with Ansible Core >= 2.16 and is expected to work with all currently supported versions of Ansible.

## External requirements

<!-- List any external resources the collection depends on, for example minimum versions of an OS, libraries, or utilities. Do not list other Ansible collections here. -->

This collection requires either **mamba** or **micromamba** to be installed on the target systems:

- **Mamba**: A faster drop-in replacement for conda. Install via conda-forge: `conda install mamba -n base -c conda-forge`
- **Micromamba**: A lightweight, standalone conda package manager. Can be installed using the included `micromamba` role

The collection includes a `micromamba` role that can automatically install and configure micromamba for you. See the [Micromamba Role Usage](#micromamba-role-usage) section below for details.

## Included content

<!-- Galaxy now usually displays full module and plugin docs within the UI. If you don't use Galaxy for your collection, you may need to either describe your plugins etc here, or point to an external docsite to cover that information. -->

This collection includes the following content:

### Modules

| Name | Description |
| ---- | ----------- |
| [hoeze.conda.conda_env](https://github.com/Hoeze/ansible-collection-conda/blob/main/plugins/modules/conda_env.py) | Manage Conda environments using YAML specifications |

### Roles

| Name | Description |
| ---- | ----------- |
| [hoeze.conda.micromamba](https://github.com/Hoeze/ansible-collection-conda/blob/main/roles/micromamba/) | Install and configure micromamba package manager |

<!--Refer to the following sections for details on how to use this collection's content:-->

- See [Module Usage](#usage-of-the-conda_env-module) for examples using the `conda_env` module
- See [Micromamba Role Usage](#micromamba-role-usage) for examples using the `micromamba` role

## Using this collection

<!--Include some quick examples that cover the most common use cases for your collection content. It can include the following examples of installation and upgrade (change hoeze.conda correspondingly):-->

### Installing the Collection from Ansible Galaxy

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:
```bash
ansible-galaxy collection install hoeze.conda
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:
```yaml
---
collections:
  - name: hoeze.conda
```

Note that if you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the `ansible` package. To upgrade the collection to the latest available version, run the following command:
```bash
ansible-galaxy collection install hoeze.conda --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version `0.1.0`:

```bash
ansible-galaxy collection install hoeze.conda:==0.1.0
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

## Usage of the `conda_env` module

This collection provides the `conda_env` module for managing Conda environments. Below are some common usage examples.

### Basic Examples

#### Check if an environment exists
```yaml
- name: Check if a Conda environment exists
  hoeze.conda.conda_env:
    name: myenv
  register: env_result

- name: Display environment status
  debug:
    msg: "Environment exists: {{ env_result.is_valid_env }}"
```

#### Create a new environment from a specification
```yaml
- name: Create environment from inline specification
  hoeze.conda.conda_env:
    name: myproject
    spec:
      name: myproject
      channels:
        - conda-forge
        - defaults
      dependencies:
        - python=3.12
        - numpy
        - pandas
        - pip
        - pip:
            - requests
            - flask
```

#### Create environment from a YAML file
```yaml
- name: Create environment from environment.yml file
  hoeze.conda.conda_env:
    name: myproject
    spec: "{{ lookup('file', 'environment.yml') | from_yaml }}"
```

#### Use a custom prefix instead of a name
```yaml
- name: Create environment in a specific location
  hoeze.conda.conda_env:
    prefix: /opt/myapp/env
    spec:
      channels:
        - conda-forge
      dependencies:
        - python=3.11
        - scikit-learn
```

### Advanced Examples

#### Update an existing environment
```yaml
- name: Update environment with new packages
  hoeze.conda.conda_env:
    name: myproject
    spec:
      name: myproject
      channels:
        - conda-forge
      dependencies:
        - python=3.12
        - numpy
        - pandas
        - matplotlib  # New package
        - pip:
            - requests
            - plotly      # New pip package
```

#### Explicitly specify the mamba executable
```yaml
- name: Create environment using mamba
  hoeze.conda.conda_env:
    name: myproject
    mamba_exe: mamba  # or micromamba
    spec:
      name: myproject
      channels:
        - conda-forge
      dependencies:
        - python=3.12
        - tensorflow
        - pytorch
```

#### Check mode (dry run)
```yaml
- name: Check what changes would be made
  hoeze.conda.conda_env:
    name: myproject
    spec:
      name: myproject
      channels:
        - conda-forge
      dependencies:
        - python=3.12
        - numpy
        - new-package  # This will show what would be installed
  check_mode: yes
  register: dry_run_result

- name: Show planned changes
  debug:
    var: dry_run_result.actions
```

### Complete Playbook Example

```yaml
---
- name: Manage Conda environments
  hosts: localhost
  tasks:
    - name: Ensure conda environment exists with specific packages
      hoeze.conda.conda_env:
        name: data-science
        mamba_exe: mamba
        spec:
          name: data-science
          channels:
            - conda-forge
            - defaults
          dependencies:
            - python=3.11
            - jupyter
            - numpy
            - pandas
            - matplotlib
            - scikit-learn
            - pip
            - pip:
                - seaborn
                - plotly
      register: env_result

    - name: Display result
      debug:
        msg: |
          Environment {{ 'created' if env_result.changed else 'already exists' }}
          Location: {{ env_result.prefix }}
          Packages: {{ env_result.package_list | length }} installed
```

### Module Parameters

The `conda_env` module supports the following parameters:

- `name`: Name of the environment (mutually exclusive with `prefix`)
- `prefix`: Full path to environment location (mutually exclusive with `name`)
- `spec`: Dictionary containing the environment specification (YAML structure)
- `mamba_exe`: Path to mamba/micromamba executable (default: "mamba")

### Return Values

The module returns information about the environment operation:

- `changed`: Whether the environment was modified
- `is_valid_env`: Whether the environment exists
- `prefix`: Full path to the environment
- `package_list`: List of packages in the environment
- `actions`: Actions performed by conda/mamba (if any)
- `cmd`: The actual command that was executed

## Micromamba Role Usage

This collection includes a `micromamba` role that automatically installs and configures micromamba on your target systems. This is especially useful when you don't have mamba or micromamba pre-installed.

### Basic Micromamba Role Usage

#### Install micromamba with default settings
```yaml
---
- name: Install micromamba
  hosts: all
  become: true
  roles:
    - hoeze.conda.micromamba
```

#### Install micromamba with custom settings
```yaml
---
- name: Install micromamba with custom configuration
  hosts: all
  become: true
  roles:
    - hoeze.conda.micromamba
  vars:
    micromamba_destination: '/usr/local/bin/micromamba'
    micromamba_version: 'latest'
    micromamba_root_prefix: '/opt/micromamba'
    micromamba_default_channels:
      - conda-forge
      - bioconda
    micromamba_envs_dirs:
      - "/opt/conda_env"
      - "/home/user/envs"
```

### Complete Example with Environment Creation

```yaml
---
- name: Setup micromamba and create environments
  hosts: all
  become: true
  tasks:
    - name: Install and configure micromamba
      include_role:
        name: hoeze.conda.micromamba
      vars:
        micromamba_destination: '/usr/local/bin/micromamba'
        micromamba_root_prefix: '/opt/micromamba'

    - name: Create a data science environment using micromamba
      hoeze.conda.conda_env:
        name: datascience
        mamba_exe: "{{ mamba_exe }}" # Automatically set by the micromamba role
        spec:
          name: datascience
          channels:
            - conda-forge
          dependencies:
            - python=3.11
            - jupyter
            - pandas
            - numpy
            - matplotlib
```

### Micromamba Role Variables

The micromamba role supports the following variables:

- `micromamba_destination`: Installation path for micromamba binary (default: `/usr/local/bin/micromamba`)
- `micromamba_version`: Version to install (default: `latest`)
- `micromamba_root_prefix`: Root directory for micromamba (default: `/opt/micromamba`)
- `micromamba_default_channels`: List of default conda channels (default: `[conda-forge, bioconda]`)
- `micromamba_envs_dirs`: List of directories where environments will be created (default: `[/opt/conda_env]`)

### Using as a Dependency

You can use the micromamba role as a dependency in other roles:

```yaml
---
# meta/main.yml in your custom role
dependencies:
  - role: hoeze.conda.micromamba
    when: install_micromamba | default(false)
```

The role automatically exports the `mamba_exe` variable pointing to the micromamba installation, which can be used by the `conda_env` module.

## Release notes

See the [changelog](https://github.com/Hoeze/ansible-collection-conda/tree/main/CHANGELOG.rst).

## More information

<!-- List out where the user can find additional information, such as working group meeting times, slack/IRC channels, or documentation for the product this collection automates. At a minimum, link to: -->

- [Ansible user guide](https://docs.ansible.com/ansible/devel/user_guide/index.html)
- [Ansible developer guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
- [Ansible collections requirements](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_requirements.html)
- [Ansible community Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html)
- [The Bullhorn (the Ansible contributor newsletter)](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn)
- [Important announcements for maintainers](https://github.com/ansible-collections/news-for-maintainers)

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
