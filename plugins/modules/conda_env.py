#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: conda_env
short_description: Manage Conda environments using a YAML specification file
version_added: "1.0.0"
description:
  - Create or update Conda environments from a YAML specification on the target host.
  - Handles both named and prefix-based environments.
  - Returns command output and change status.
  - In check mode, the module will report whether and what changes would be made, without actually modifying the environment.
options:
  spec:
    description:
      - Nested dictionary describing the Conda environment specification.
      - This should be a valid YAML structure that can be converted to a YAML file.
    required: false
    type: dict
  prefix:
    description:
      - The full path to the environment location (mutually exclusive with C(name)).
    required: false
    type: str
  name:
    description:
      - The name of the Conda environment to manage (mutually exclusive with C(prefix)).
    required: false
    type: str
  conda_exe:
    description:
      - The path to the conda executable to use.
    required: false
    type: str
    default: conda
author:
  - Florian R. Hölzlwimmer (@hoeze)
"""

EXAMPLES = r"""
- name: Determine if a Conda environment exists and get its package list
  conda_env:
    name: myenv
  register: conda_env_result
    
- name: Create or update a Conda environment from a YAML file
  conda_env:
    spec: "{{ lookup('file', 'environment.yml') | from_yaml }}"
    name: myenv

- name: Use a prefix instead of a name
  conda_env:
    spec: "{{ lookup('file', 'environment.yml') | from_yaml }}"
    prefix: /opt/conda/envs/myenv

- name: Check if creating a Conda environment would result in changes
  conda_env:
    spec: "{{ lookup('file', 'environment.yml') | from_yaml }}"
    name: mynewenv
  check_mode: yes
"""

RETURN = r"""
changed:
  description: Whether the environment was created or updated.
  type: bool
  returned: always
is_valid_env:
  description: Whether the environment existed before the operation.
  type: bool
  returned: always
conda_env_spec_file:
  description: Path to the temporary YAML file used for the environment specification.
  type: str
  returned: when spec is provided
cmd:
  description: The last conda command that was executed. This will be the check command if spec is not provided, otherwise it will be the create/update command.
  type: list
  returned: always
package_list:
  description: The list of packages in the environment before any changes were made.
  type: list
  returned: always
actions:
  description: The actions Conda performed (if any; may be omitted if no actions were needed or reported).
  type: dict
  returned: when available
prefix:
  description: The prefix of the Conda environment, which is the full path to the environment location.
  type: str
  returned: always
returncode:
  description: The return code of the last executed conda command.
  type: int
  returned: always
msg:
  description: Any error message or additional information.
  type: str
  returned: when available
"""

from ansible.module_utils.basic import AnsibleModule
import os
import json
import yaml
import tempfile
import subprocess


def check_conda_env(conda_exe, prefix, name):
    cmd = [conda_exe, "list", "--json"]
    if prefix:
        cmd.extend(["--prefix", prefix])
    if name:
        cmd.extend(["--name", name])
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        env_package_list = []
        if proc.returncode == 0:
            env_package_list = json.loads(proc.stdout)
            is_valid_env = len(env_package_list) > 0
        else:
            is_valid_env = False
        return {
            "cmd": cmd,
            "package_list": env_package_list,
            "returncode": proc.returncode,
            "is_valid_env": is_valid_env,
            "changed": False,
            "failed": False,
        }
    except Exception as e:
        raise Exception(
            f"Exception occurred while running: '{subprocess.list2cmdline(cmd)}'"
        ) from e


def conda_env_create_update(
    conda_exe, conda_env_subcommand, prefix, name, spec_file_path, dry_run=False
):
    # Update environment
    cmd = [
        conda_exe,
        "env",
        conda_env_subcommand,
        "-y",
        "--json",
        "--file",
        spec_file_path,
    ]
    if prefix:
        cmd.extend(["--prefix", prefix])
    if name:
        cmd.extend(["--name", name])
    if dry_run:
        cmd.append("--dry-run")

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        env_output = {}
        if proc.stdout:
            try:
                env_output = json.loads(proc.stdout)
            except Exception:
                env_output = {}
        actions = env_output.get("actions", None)
        prefix = env_output.get("prefix", None)
        changed = actions is not None and len(actions) > 0
        success = env_output.get("success", True)
        return {
            "cmd": cmd,
            "actions": actions,
            "prefix": prefix,
            "returncode": proc.returncode,
            "changed": changed,
            "failed": not success,
        }
    except Exception as e:
        raise Exception(
            f"Exception occurred while running: '{subprocess.list2cmdline(cmd)}'"
        ) from e


def conda_create(conda_exe, prefix, name, dry_run=False):
    # Update environment
    cmd = [conda_exe, "create", "-y", "--json"]
    if prefix:
        cmd.extend(["--prefix", prefix])
    if name:
        cmd.extend(["--name", name])
    if dry_run:
        cmd.append("--dry-run")

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        env_output = {}
        if proc.stdout:
            try:
                env_output = json.loads(proc.stdout)
            except Exception:
                env_output = {}
        actions = env_output.get("actions", None)
        prefix = env_output.get("prefix", None)
        changed = actions is not None and len(actions) > 0
        success = env_output.get("success", True)
        return {
            "cmd": cmd,
            "actions": actions,
            "prefix": prefix,
            "returncode": proc.returncode,
            "changed": changed,
            "failed": not success,
        }
    except Exception as e:
        raise Exception(
            f"Exception occurred while running: '{subprocess.list2cmdline(cmd)}'"
        ) from e


def conda_run_getprefix(conda_exe, prefix, name, dry_run=False):
    # Update environment
    cmd = [conda_exe, "run"]
    if prefix:
        cmd.extend(["--prefix", prefix])
    if name:
        cmd.extend(["--name", name])

    # run the "env" command
    cmd.append("env")

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)

        parsed_env = {}
        if proc.stdout:
            for line in proc.stdout.strip().splitlines():
                if "=" in line:
                    key, value = line.split("=", 1)
                    parsed_env[key] = value

        return {
            "cmd": cmd,
            "returncode": proc.returncode,
            "failed": proc.returncode != 0,
            "changed": False,
            "prefix": parsed_env.get("CONDA_PREFIX"),
            "env": parsed_env,
        }
    except Exception as e:
        raise Exception(
            f"Exception occurred while running: '{subprocess.list2cmdline(cmd)}'"
        ) from e


def main():
    module = AnsibleModule(
        argument_spec=dict(
            spec=dict(type="dict", required=False, default=None),
            prefix=dict(type="str", required=False, default=None),
            name=dict(type="str", required=False, default=None),
            conda_exe=dict(type="str", required=False, default="conda"),
        ),
        supports_check_mode=True,
    )
    spec = module.params["spec"]
    prefix = module.params["prefix"]
    name = module.params["name"]
    conda_exe = module.params["conda_exe"]

    result = dict()

    try:
        # Check if prefix is a valid conda environment
        env_check_result = check_conda_env(conda_exe, prefix, name)
        result.update(env_check_result)

        if spec:
            # Install or update environment based on validity
            conda_env_subcommand = (
                "update" if env_check_result["is_valid_env"] else "create"
            )

            # Save spec file to a temporary file
            temp_fd, temp_spec_file_path = tempfile.mkstemp(suffix=".yaml")
            with os.fdopen(temp_fd, "w") as fp:
                yaml.dump(spec, fp)
            result["conda_env_spec_file"] = temp_spec_file_path

            # Create or update the conda environment
            conda_env_create_update_result = conda_env_create_update(
                conda_exe=conda_exe,
                conda_env_subcommand=conda_env_subcommand,
                prefix=prefix,
                name=name,
                spec_file_path=temp_spec_file_path,
                dry_run=module.check_mode,
            )
            result.update(conda_env_create_update_result)
        else:
            # If no spec is provided, just return the environment check result.
            # We also try to determine the environment's prefix.
            if prefix is None:
                if result["is_valid_env"]:
                    # If the env exists, get its prefix
                    prefix_result = conda_run_getprefix(conda_exe, prefix, name)
                    if prefix_result["failed"]:
                        module.fail_json(
                            {
                                **result,
                                "msg": f"Failed to get prefix for otherwise valid environment '{name}'! This is likely a bug in the 'conda_env' module.",
                                "cmd": prefix_result["cmd"],
                                "returncode": prefix_result["returncode"],
                            }
                        )
                    result["prefix"] = prefix_result["prefix"]
                else:
                    # If the env does not exist, do a dry-run create to find out where it would be created.
                    create_result = conda_create(conda_exe, prefix, name, dry_run=True)
                    result["prefix"] = create_result["prefix"]
            else:
                # If a prefix is provided, we assume it is a valid conda environment.
                result["prefix"] = prefix

    except Exception as e:
        module.fail_json(msg=str(e))

    if result["failed"]:
        module.fail_json(**result)
    else:
        module.exit_json(**result)


if __name__ == "__main__":
    main()
