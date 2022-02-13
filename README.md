# BurgerZilla

YemekSepeti Python Web Development Bootcamp Final Projesi

## API Kullanımı

Postman collection ile ya da 
auth servisleri için localhost:5000
restaurant ve customer servisleri için localhost:5000/api ile swagger dökümanlarına erişilebilir.

  
## Bilgisayarınızda Çalıştırın

Projeyi klonlayın

```bash
    git clone https://github.com/aysberna/burgerzilla.git
```

Proje dizinine gidin

```bash
    cd burgerzilla
```

Virtual environment oluşturun

```bash
    python -m venv env
    . venv/bin/activate # Windows için
    source env/bin/activate # Linux-MacOS için
```
Gerekli paketleri yükleyin

```bash
    pip install -r requirements.txt
```

Ön tanımlı verileri yükleyin (Kullanıcı, restoran, menu, ürünler)
user-> email: email='customer1@customer.com', 'password:12345678'
restaoran-> email='user1@user.com', password='12345678'
ürün-> name='Bombili burger', menu_id=1
menü-> name='Dombili burger menu', restaurant_id='1'

```bash
    flask initialvalues
```

Sunucuyu çalıştırın

```bash
    flask run
```

Testleri çalıştırın

```bash
    flask test
```


## Dockerda Çalıştırın

Dockerda projeyi oluşturun

```bash
    docker build -t burgerzillalatest .
```

Postgresql bağlantısı için compose yapın

```bash
    docker compose up --build web
```

Flaskın çalıştığı adresten (localhost) dökümanlara ve servislere erişebilirsiniz.

## Veri tabanı şeması

![Burgerzilla_models](https://user-images.githubusercontent.com/4121960/153591356-b0bf3db6-35c2-46b2-b4c8-9733ee1e3f92.png)

  
## Dizin Yapısı

```
burgerzilla
├─ .env
├─ .gitignore
├─ README.md
├─ YemekSepeti.postman_collection.json
├─ app
│  ├─ __init__.py
│  ├─ api
│  │  ├─ __init__.py
│  │  ├─ customers
│  │  │  ├─ __init__.py
│  │  │  ├─ controller.py
│  │  │  ├─ dto.py
│  │  │  ├─ service.py
│  │  │  └─ utils.py
│  │  ├─ restaurants
│  │  │  ├─ __init__.py
│  │  │  ├─ controller.py
│  │  │  ├─ dto.py
│  │  │  ├─ service.py
│  │  │  └─ utils.py
│  │  └─ user
│  │     ├─ __init__.py
│  │     ├─ controller.py
│  │     ├─ dto.py
│  │     ├─ service.py
│  │     └─ utils.py
│  ├─ auth
│  │  ├─ __init__.py
│  │  ├─ controller.py
│  │  ├─ dto.py
│  │  ├─ service.py
│  │  └─ utils.py
│  ├─ extensions.py
│  ├─ models
│  │  ├─ __init__.py
│  │  ├─ menu.py
│  │  ├─ order.py
│  │  ├─ order_detail.py
│  │  ├─ product.py
│  │  ├─ restaurant.py
│  │  ├─ schemas.py
│  │  └─ user.py
│  └─ utils.py
├─ config.py
│  └─ texts.py
├─ defaults.txt
├─ requirements.txt
├─ runservice.py
└─ tests
   ├─ __init__.py
   ├─ test_auth_api.py
   ├─ test_config.py
   ├─ test_restaurant_api.py
   ├─ test_restaurant_model.py
   ├─ test_user_api.py
   ├─ test_user_model.py
   └─ utils
      ├─ __init__.py
      ├─ base.py
      └─ common.py

```
  
  
 ## Proje Yemeksepeti Bootcamp dersleri ve İbrahim Ediz'in oluşturdugu örnek projeler baz alınarak geliştirilmiştir.
