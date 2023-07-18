#!/bin/bash
curl -X POST -H "Content-Type: application/json" -d '{
    "date": "2023-07-15",
    "cost": 1200.99,
    "item": "Laptop",
    "vendor": "Electronics Store",
    "category": "Electronics"
}' http://127.0.0.1:5555/add

curl -X POST -H "Content-Type: application/json" -d '{
    "date": "2023-07-13",
    "cost": 150.23,
    "item": "Groceries",
    "vendor": "Supermarket",
    "category": "Food"
}' http://127.0.0.1:5555/add

curl -X POST -H "Content-Type: application/json" -d '{
    "date": "2023-07-14",
    "cost": 75.45,
    "item": "Dog Food",
    "vendor": "Pet Store",
    "category": "Pets"
}' http://127.0.0.1:5555/add

curl -X POST -H "Content-Type: application/json" -d '{
    "date": "2023-07-16",
    "cost": 50.00,
    "item": "Monthly Membership",
    "vendor": "Local Gym",
    "category": "Fitness"
}' http://127.0.0.1:5555/add

curl -X POST -H "Content-Type: application/json" -d '{
    "date": "2023-07-17",
    "cost": 100.12,
    "item": "Dinner",
    "vendor": "Italian Restaurant",
    "category": "Dining"
}' http://127.0.0.1:5555/add

curl -X POST -H "Content-Type: application/json" -d '{
    "date": "2023-07-18",
    "cost": 40.30,
    "item": "Gasoline",
    "vendor": "Gas Station",
    "category": "Transportation"
}' http://127.0.0.1:5555/add

