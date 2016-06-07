def app(environ, start_response):
	start_response("200 OK", [("Content-Type", "text/plain")])
	queryString = environ["QUERY_STRING"]
	responseBody = queryString.replace("&", "\n")
	return responseBody
