<https://avtosalon.pythonanywhere.com/api/>

the avto-slon API has the following endpoints:

|Method | Endpoint | Description |
| --- | --- |--- |
|Post | <a  href="#car/"`CarViewSet`> </a>| add a new car |
|Get | <a  href="#car/"`CarViewSet`> </a>| get a list of all cars |
|Get | <a  href="#car/{id}"`Carget`> </a>| get a car by id |
|Put | <a  href="#car/{id}"`CarViewSet`> </a>| update a car by id |
|Post | <a  href="#car/delete/<int:pk>/"`CarViewdelete`> </a>| delete a car by id |
| --- | --- |--- |
|Post | <a href="konfigurator/"`KonfiguratorViewSet`> </a>| add a new konfigurator |
|Get | <a href="konfigurator/"`KonfiguratorViewSet`> </a>| get a list of all konfigurators |
|Get | <a href="konfiguratorget/<int:pk>/"`Konfiguratorget`> </a>| get a konfigurator by id |
|Put | <a href="konfigurator/{id}"`KonfiguratorViewSet`> </a>| update a konfigurator by id |
|Post | <a href="konfigurator/delete/<int:pk>/"`Konfiguratordelete`> </a>| delete a konfigurator by id |
| --- | --- |--- |
|Post | <a href="dilery/"`DileryViewSet`> </a>| add a new loction |
|Get | <a href="dilery/"`DileryViewSet`> </a>| get a list of all locations |
|Put | <a href="dilery/{id}"`DileryViewSet`> </a>| update a location by id |
|Post | <a href="dilery/delete/<int:pk>/"`Dilerydelete`> </a>| delete a location by id |
| --- | --- |--- |
|Post | <a href = "extiyot_qisimlar/" `Extiyot_qisimlarView`> </a>| add a new extiyot_qisimlar |
|Get | <a href = "extiyot_qisimlar/" `Extiyot_qisimlarView`> </a>| get a list of all extiyot_qisimlar |
|Put | <a href = "extiyot_qisimlar/{id}" `Extiyot_qisimlarView`> </a>| update a extiyot_qisimlar by id |
|Post | <a href = "extiyotqisimlar_delet/<int:pk>/" `Extiyot_qisimlardelete`> </a>| delete a extiyot_qisimlar by id |
| --- | --- |--- |
|Post | <a href = "sub_extiyotqisimlar/" `Sub_extiyotqisimlarView`> </a>| add a new extiyot qisimlar |
|Get | <a href = "sub_extiyotqisimlar/" `Sub_extiyotqisimlarView`> </a>| get a list of all extiyot qisimlar |
|Put | <a href = "sub_extiyotqisimlar/{id}" `Sub_extiyotqisimlarView`> </a>| update a extiyot qisimlar by id |
|Post | <a href = "sub_extiyot_delet/<int:pk>/" `Sub_extiyot_delet`> </a>| delete a extiyot qisimlar by id |
| --- | --- |--- |
|Post | <a herf = "usercreate/" `Usercreateviews`> </a>| add a new user |
|Post | <a herf = "userlogout/" `Userlogoutviews`> </a>| user logout|
|Post | <a herf = "userlogin/" `Userloginviews`> </a>| user log in|
| --- | --- | --- |
|Post | <a herf = "cartcar/" `CartView`> </a>| | cart car by id|
|Get | <a herf = "cartcar/" `CartView`> </a>| | get a list of all cart car |
|Post | <a herf = "cartcar/delete/<int:pk>/" `CartViewdelete`> </a>| | delete a cart car by id|
|Post | <a herf = "cartcardelete/" `Cartdelete`> </a>| | delete all cart car |
| --- | --- | --- |
|Post | <a herf = "cart_extiyotqisimlar" `Cart_extiyotqisimlarView`> </a>| | cart extiyot qisimlar by id|
|Get | <a herf = "cart_extiyotqisimlar" `Cart_extiyotqisimlarView`> </a>| | get a list of all cart extiyot qisimlar |
|Post | <a herf = "cart_extiyotqisimlar/delete/<int:pk>/" `Cart_extiyotqisimlarViewdelete`> </a>| | delete a cart extiyot qisimlar by id|
|Post | <a herf = "cart_extiyotqisimlardelete/<int:pk>/" `Cart_extiyotqisimlardelete`> </a>| | delete all cart extiyot qisimlar |
| --- | --- | --- |
|Post | <a herf = "likecar/" `LikeCarViews`> </a> | like car by id|
|Get | <a herf = "likecar/" `LikeCarViews`> </a> | get a list of all like car |
|Post | <a herf = "likeupdate/<int:pk>/" `LikeUpdate`> </a> | Update a like car by id|
|Post | <a herf = "likecardelete/<int:pk>/" `LikeCardelete`> </a> | delete all like car |
| --- | --- | --- |





