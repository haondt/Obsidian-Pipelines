import sys, json
data = json.loads(sys.stdin.read())
template = """
$HOST:$CONTAINER:
  stage: deploy
  when: manual
  script:
    - echo "I am deploying to $HOST -> $CONTAINER"
"""

output = """
stages:
  - deploy
"""
for host in data:
    for ctr in data[host]:
        output += template.replace("$HOST", host).replace("$CONTAINER", ctr)

print(output)