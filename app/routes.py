def register_routes(app):

    @app.route("/health")
    def health():
        return {"status": "ok"}, 200

    @app.route("/items")
    def get_items():
        items = ["item1", "item2", "item3"]
        return {"items": items}, 200
