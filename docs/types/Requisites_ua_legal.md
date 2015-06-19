
## Requisites_ua_legal

### Описание типа
Реквизиты плательщика – юридического лица Украины.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*director_name*|True|[string](/types/string)|Должность и ФИО лица, подписывающего документы.<br/>|
|*signer_basis*|True|[string](/types/string)|На основании («на пiдставi»).<br/>|
|*address_postal*|True|[string](/types/string)|Адрес для приёма корреспонденции.<br/>|
|*pdv*|False|[string](/types/string)|Свидетельство ПДВ.<br/>Допустимы только цифры. 8 или 9 символов.<br/>|
|*account_r*|True|[string](/types/string)|Номер счета.<br/>Допустимы только цифры. От 4 до 14 символов.<br/>|
|*ipn*|False|[string](/types/string)|IПН.<br/>Допустимы только цифры. 15 символов.<br/>|
|*corporate_name*|True|[string](/types/string)|Название юридического лица.<br/>|
|*director_name_alt*|True|[string](/types/string)|Должность и ФИО представителя юр. лица (в родительном падеже).<br/>|
|*address_corporate*|True|[string](/types/string)|Местонахождение.<br/>|
|*mfo*|True|[string](/types/string)|МФО.<br/>Допустимы только цифры. 6 символов.<br/>|
|*unified_tax*|True|[string](/types/string)|Является ли плательщиком единого 5% налога.<br/>В данный момент это строковое поле, куда народ пишет всякое. Уточнить, быть может это надо сделать boolean и, соответственно переделать UI.<br/>|
|*bank*|True|[string](/types/string)|Банковские данные.<br/>|
|*edrpou*|True|[string](/types/string)|ЄДРПОУ.<br/>Допустимы только цифры. 8 символов.<br/>|
