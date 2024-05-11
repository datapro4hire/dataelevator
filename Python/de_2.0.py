endpoint = "couchbases://cb.y3sx75xkz3nthuss.cloud.couchbase.com" # Replace this with Connection String
username = "foo" # Replace this with  username from database access credentials
password = "p@ssw0rd" # Replace this with password from database access credentials
# User Input ends here.

# Connect options - authentication
auth = PasswordAuthenticator(username, password)

# Get a reference to our cluster
options = ClusterOptions(auth)

# Use the pre-configured profile below to avoid latency issues with your connection.
options.apply_profile("wan_development")
try:
	cluster = Cluster(endpoint, options)
	# Wait until the cluster is ready for use.
	cluster.wait_until_ready(timedelta(seconds=5))
except Exception as e:
	traceback.print_exc()
