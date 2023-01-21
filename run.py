from app import app

if __name__ == "__main__":
    ssl_context = ("openssl/server.crt", "openssl/private.key")
    app.run(debug=True, ssl_context=ssl_context)
