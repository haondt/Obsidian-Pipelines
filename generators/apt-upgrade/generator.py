import sys, re
data = sys.stdin.read()
m = re.search(r'hosts \([0-9]+\):\n((?:\s+[A-Za-z-]+\n)+)[\n\s]*$', data)

if not m:
    raise Exception(f"Unable to parse input {data}")
hosts = [i.strip() for i in m.group(1).split('\n') if len(i.strip()) > 0]
if len(hosts) <= 0:
    raise Exception(f"Could not find any hosts {data}")

output = """stages:
  - deploy
"""
template = """
$HOST:
  stage: deploy
  when: manual
  needs:
    - pipeline: $ROOT_PIPELINE_ID
      job: get-ansible-scripts
  script:
    - cd ansible
    - ansible-playbook playbooks/upgrade.yml --limit $HOST
"""
for host in hosts:
    output += template.replace("$HOST", host)

print(output)