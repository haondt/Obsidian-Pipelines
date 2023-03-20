import sys, json
data = json.loads(sys.stdin.read())
gid = sys.argv[1]
output = [
    "ansible-playbook playbooks/set_up_docker_lxc.yml",
    f"-e \"container_suffix={data['container_suffix']}\"",
    f"-e \"container_ip={data['ip']}\"",
    f"-e \"container_gid={gid}\"",
    f"-e \"container_id={data['cid']}\""
]
print(' '.join(output))