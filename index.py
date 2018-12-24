import web

urls = (
  '/', 'index'
)

class index:
    def GET(self):
        return "<h1>Fucking awesome. It's work</h1>"

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run() 
