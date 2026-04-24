text = "We are learning Python for DevOps."
new_text = text.split()
print("Words:", new_text)
print("") 
print(text.split()[3])
print("")
arn= "arn:partition:service:region:account-id:resource-type/resource-id"
new_arn = arn.split("/")
print("ARN parts:", new_arn)
print("")
print(arn.split("/")[1])