from app import create_app


app = create_app()

class MyClass():
    def __init__(self, param):
        self.param = param

if __name__ == "__main__":
    c = MyClass(5)
    app.run(host='0.0.0.0', port=8000, debug=True)
