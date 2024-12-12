package poc.access

default allow = false

# Allow delete operation for high sensitivity resources by admin users
allow {
    input.resource.sensitivity == "high"
    input.action.operation == "delete"
    input.user.role == "admin"
}

# Allow resource access if the user is the owner
allow {
    input.resource.owner == input.user.id
}
