data = [
    {
        "organic": [{
            "id": 1,
            "name": "Fabula Organic Coffee",
            "img": "data:image/jpeg;base64,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",
            "price": 45.3
        },
        {
            "id": 2,
            "name": "Valhalla Java Ground Coffee",
            "img": "",
            "price": 45.3
        },
        {
            "id": 3,
            "name": "Tiny Footprint Coffee Organic",
            "img": "",
            "price": 45.3
        },
        {
            "id": 4,
            "name": "Cameron's Specialty Coffee",
            "img": "",
            "price": 45.3
        },
        {
            "id": 5,
            "name": "flower",
            "img": "",
            "price": 45.3
        },
        {
            "id": 6,
            "name": "flower",
            "img": "",
            "price": 45.3
        }
        ]
    },
    {
        "inorganic": [{
            "id": 1,
            "name": "Inorganic",
            "img": "",
            "price": 45.3
        },
        {
            "id": 2,
            "name": "flower",
            "img": "",
            "price": 45.3
        },
        {
            "id": 3,
            "name": "flower",
            "img": "",
            "price": 45.3
        },
        {
            "id": 4,
            "name": "flower",
            "img": "",
            "price": 45.3
        },
        {
            "id":5,
            "name": "flower",
            "img": "",
            "price": 45.3
        },
        {
            "id": 6,
            "name": "flower",
            "img": "",
            "price": 45.3
        }
        ]
    },{
        "manufactored": [{}]
    }]