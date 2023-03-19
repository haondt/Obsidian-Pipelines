# Obsidian-Pipelines

This repository is mirrored on GitHub at https://github.com/haondt/Obsidian-Pipelines and the upstream source is on GitLab at https://gitlab.com/burghardtnoah/obsidian-pipelines/.

This is a companion repo to my homelab configuration, [haondt/Obsidian](https://github.com/haondt/Obsidian).

The general premise is to manually start a GitLab pipeline to run ad-hoc tasks. The pipeline will call a mix of python scripts and Ansible playbooks to generate child pipelines. Finally, the child pipelines will run Ansible playbooks with pre-set variables to perform the actual task on host machines.

The Ansible playbooks rely on the hostnames in my homelab configuration, so the pipeline is executed on a GitLab runner that lives inside of my home network, where it can take advantage of my dns server for hostname routing.
