
## Requisites_ua_sp

### Описание типа
Реквизиты плательщика – ФОП Украины.<br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*director_name*|True|[string](/types/string)|Должность и ФИО лица, подписывающего документы.<br/>|
|*signer_basis*|True|[string](/types/string)|На основании имеет право подписывать документы (“на пiдставi”).<br/>|
|*edruofop_number*|True|[string](/types/string)|Дата и номер записи в “єдиному державному реєстрі юридичних та фiзичних осiб-пiдприємцiв”<br/>|
|*rnokpp*|True|[string](/types/string)|РНОКПП.<br/>Допустимы только цифры. 10 символов.<br/>|
|*pdv*|False|[string](/types/string)|Свидетельство ПДВ.<br/>Допустимы только цифры. 8 или 9 символов.<br/>|
|*account_r*|False|[string](/types/string)|Номер счета.<br/>Допустимы только цифры. От 4 до 14 символов.<br/>|
|*ipn*|False|[string](/types/string)|IПН.<br/>Допустимы только цифры. 15 символов<br/>|
|*corporate_name*|True|[string](/types/string)|Название юридического лица.<br/>|
|*address_postal*|True|[string](/types/string)|Адрес для приёма корреспонденции.<br/>|
|*director_name_alt*|True|[string](/types/string)|Должность и ФИО представителя юр. лица (в родительном падеже).<br/>|
|*address_corporate*|True|[string](/types/string)|Местонахождение.<br/>|
|*mfo*|False|[string](/types/string)|МФО.<br/>Допустимы только цифры. Максимум 6 символов.<br/>|
|*unified_tax*|True|[string](/types/string)|Является ли плательщиком единого 5% налога<br/>|
|*bank*|False|[string](/types/string)|Банковские данные.<br/>|
|*edrpou*|True|[string](/types/string)|ЄДРПОУ.<br/>Допустимы только цифры. 8 символов.<br/>|
