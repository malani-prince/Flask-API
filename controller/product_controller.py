from app import app

@app.route('/product/<int:cap>')
def Product_count(cap):
    return f"Total Product capacity {str(cap)}"
