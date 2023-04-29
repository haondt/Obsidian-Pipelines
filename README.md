# Obsidian-Pipelines

This repository is mirrored on GitHub at https://github.com/haondt/Obsidian-Pipelines and the upstream source is on GitLab at https://gitlab.com/burghardtnoah/obsidian-pipelines/.

This is a companion repo to my homelab configuration, [haondt/Obsidian](https://github.com/haondt/Obsidian).

The general premise is to manually start a GitLab pipeline to run ad-hoc tasks. The pipeline will call a mix of python scripts and Ansible playbooks to generate child pipelines. Finally, the child pipelines will run Ansible playbooks with pre-set variables to perform the actual task on host machines.

The Ansible playbooks rely on the hostnames in my homelab configuration, so the pipeline is executed on a GitLab runner that lives inside of my home network, where it can take advantage of my dns server for hostname routing.

# Rundown of pipelines

### Plex Update

- Description
    - Updates plex server
- Variables
    - `TASK`: `plex_update`
    - `PLEX_VERSION`: anything from dropdown
- Usage
    - Simply run the pipeline

### Update/Update Apt Packages

- Description
    - Runs `apt update && apt upgrade` on machine
- Variables
    - `TASK`: `apt_upgrade`
- Usage
    - Run pipeline, it will generate a manual job to update each available machine

### Update Docker Image

- Description
    - Updates the image for and recreates a container
- Variables
    - `TASK`: `docker_image_update`
- Usage
    - Run pipeline, it will generate a manual job to update each available docker container

### Create a docker lxc

- Description
    - Creates a new docker lxc (TODO: ansible script incomplete, doesn't yet install docker & docker compose)
- Variables
    - `TASK`: `create_docker_lxc`
    - `DOCKER_LXC_SUFFIX`: hostname will be `docker-${DOCKER_LXC_SUFFIX}`
    - `DOCKER_LXC_GID`: Part of the setup will create a group for files and whatnot on the new host. This is the id that will be used for the group.
- Usage
    - Run pipeline, it will create the lxc. It will also create an artifact, called `report.txt` which contains details about the new container.