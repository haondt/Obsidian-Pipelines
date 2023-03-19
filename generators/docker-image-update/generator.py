import sys, json
data = json.loads(sys.stdin.read())
template = """
$HOST:$CONTAINER:
  stage: deploy
  when: manual
  script:
    - cd ansible
    - ansible-playbook playbooks/update_docker_container.yml --limit $HOST -e "container_name=$CONTAINER"
"""

output = """
stages:
  - deploy
"""
for host in data:
    for ctr in data[host]:
        output += template.replace("$HOST", host).replace("$CONTAINER", ctr)

print(output)