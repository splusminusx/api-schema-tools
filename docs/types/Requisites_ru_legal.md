
## Requisites_ru_legal

### Описание типа
Requisites_ru_legal
Реквизиты плательщика - юридического лица РФ.
Таблица 72. Поля реквизитов юридического лица РФ


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|kpp|False|string|КПП. 9 символов.<br/>|
|signer_basis|True|string|На основании чего имеет право подписывать документы.<br/>|
|address_postal|True|string|Физический адрес.<br/>|
|account_r|True|string|Расчетный счет.<br/>Допустимы только цифры. 20 символов.<br/>|
|bic|True|string|БИК.<br/>Допустимы только цифры. 9 символов.<br/>|
|ogrn|False|string|ОГРН. 13 или 15 символов.<br/>|
|director_name|True|string|Должность и ФИО лица, подписывающего документы.<br/>|
|account_k|True|string|Корреспондентский счет.<br/>Допустимы только цифры. 20 символов.<br/>|
|director_name_alt|True|string|Должность и ФИО представителя юр. лица (в родительном падеже).<br/>|
|address_corporate|True|string|Юридический адрес.<br/>|
|corporate_name|True|string|Название юридического лица.<br/>|
|bank|True|string|Наименование банка.<br/>|
|inn|False|string|ИНН. Допустимы только цифры. 10 или 12 цифр.<br/>|
