# new_middleware is a callable which takes a get_response callable and returns a middleware
class BlogMiddleware(object):
    def process_request(self, request):
        print("Middleware Executed!")
