# Online Python compiler (interpreter) to run Python online
# Write Python 3 code in this online editor and run it.

devops={"skill":"DevOps", "Year":2023, "Tech":{"Cloud":"AWS", "Containers":"K8s", "CICD":"Jenkins"}}
print(devops)

devops={"skill":"DevOps", "Year":2023, "Tech":{"Cloud":"AWS", "Containers":"K8s", "CICD":"Jenkins", "GitOps":["GitLab", "ArgoCD", "Tekton"]}}
print(devops)

#JSON
{
  "devops": {
    "skill": "DevOps",
    "Year": 2023,
    "Tech": {
      "Cloud": "AWS",
      "Containers": "K8s",
      "CICD": "Jenkins",
      "GitOps": [
        "GitLab",
        "ArgoCD",
        "Tekton"
      ]
    }
  }
}

#YAML
devops:
  skill: DevOps
  Year: 2023
  Tech:
    Cloud: AWS
    Containers: K8s
    CICD: Jenkins
    GitOps:
      - GitLab
      - ArgoCD
      - Tekton
