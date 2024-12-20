from fastapi import FastAPI, HTTPException, Request
import csv
import os
import requests

app = FastAPI()


# Endpoint do pobierania historii zamówień
@app.get("/orders/{user}")
async def get_order_history(user: str):
    response = requests.get("http://api:8000/orders",
                            params=dict(user=user)).json()
    if not response:
        raise HTTPException(status_code=404, detail="Orders not found")

    for order in response:
        cart_items = [
            item
            for item in requests.get(f"http://api:8000/carts/{order['cart_id']-1}/items").json()
        ]
        order['products'] = [
            requests.get(
                f"http://api:8000/products/{item['product_id']}").json() | dict(quantity=item['quantity'])
            for item in cart_items
        ]
    return response


# Endpoint do przyjmowania opinii o produktach
@ app.post("/review")
async def submit_review(request: Request):
    review = await request.json()
    username = review.get("username")
    order_id = review.get("order_id")
    product = review.get("product")
    review_text = review.get("review")

    if not username or not order_id or not product or not review_text:
        raise HTTPException(status_code=400, detail="Incomplete review data")

    review_filename = "reviews.csv"
    review_exists = os.path.isfile(review_filename)

    with open(review_filename, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        if not review_exists:
            writer.writerow(["username", "order_id", "product", "review"])
        writer.writerow([username, order_id, product, review_text])

    return {"message": "Review submitted successfully"}
