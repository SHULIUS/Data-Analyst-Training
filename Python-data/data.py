# Diccionario con datos variados
data = {
    "personas": [
        {"id": 1, "nombre": "Julia", "edad": 28, "ciudad": "Madrid"},
        {"id": 2, "nombre": "Carlos", "edad": 35, "ciudad": "Barcelona"},
        {"id": 3, "nombre": "Ana", "edad": 22, "ciudad": "Valencia"},
        {"id": 4, "nombre": "Luis", "edad": 40, "ciudad": "Sevilla"},
        {"id": 5, "nombre": "María", "edad": 30, "ciudad": "Bilbao"},
        {"id": 6, "nombre": "Pedro", "edad": 27, "ciudad": "Granada"}
    ],
    "productos": [
        {"id": 101, "nombre": "Laptop", "precio": 1200.50, "stock": 15},
        {"id": 102, "nombre": "Smartphone", "precio": 800.99, "stock": 30},
        {"id": 103, "nombre": "Tablet", "precio": 450.00, "stock": 20},
        {"id": 104, "nombre": "Monitor", "precio": 300.75, "stock": 10},
        {"id": 105, "nombre": "Teclado", "precio": 50.00, "stock": 50},
        {"id": 106, "nombre": "Ratón", "precio": 25.00, "stock": 60}
    ],
    "ventas": [
        {"venta_id": 1001, "producto_id": 101, "persona_id": 1, "cantidad": 1, "total": 1200.50},
        {"venta_id": 1002, "producto_id": 102, "persona_id": 2, "cantidad": 2, "total": 1601.98},
        {"venta_id": 1003, "producto_id": 103, "persona_id": 3, "cantidad": 1, "total": 450.00},
        {"venta_id": 1004, "producto_id": 104, "persona_id": 4, "cantidad": 3, "total": 902.25},
        {"venta_id": 1005, "producto_id": 105, "persona_id": 5, "cantidad": 4, "total": 200.00},
        {"venta_id": 1006, "producto_id": 106, "persona_id": 6, "cantidad": 5, "total": 125.00}
    ],
    "categorias": [
        {"categoria_id": 1, "nombre": "Electrónica"},
        {"categoria_id": 2, "nombre": "Hogar"},
        {"categoria_id": 3, "nombre": "Ropa"},
        {"categoria_id": 4, "nombre": "Deportes"},
        {"categoria_id": 5, "nombre": "Libros"}
    ]
}



for i in data["personas"]:
    print(i["nombre"])
print("_______________________")    
for i in data["productos"]:
    print(i["nombre"])      

