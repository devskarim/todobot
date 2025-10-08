from psycopg2 import connect


def get_connect(): 
	return connect(
		user = "postgres",
		database = "todolist",
		password = "hcnma_$", 
		host = "localhost", 
		port = 5432 
	)


