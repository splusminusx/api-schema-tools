
## Requisites_ru_legal

### Описание типа
Реквизиты плательщика - юридического лица РФ.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*kpp*|False|[string](/types/string)|КПП. 9 символов.<br/>|
|*signer_basis*|True|[string](/types/string)|На основании чего имеет право подписывать документы.<br/>|
|*address_postal*|True|[string](/types/string)|Физический адрес.<br/>|
|*account_r*|True|[string](/types/string)|Расчетный счет.<br/>Допустимы только цифры. 20 символов.<br/>|
|*bic*|True|[string](/types/string)|БИК.<br/>Допустимы только цифры. 9 символов.<br/>|
|*ogrn*|False|[string](/types/string)|ОГРН. 13 или 15 символов.<br/>|
|*director_name*|True|[string](/types/string)|Должность и ФИО лица, подписывающего документы.<br/>|
|*account_k*|True|[string](/types/string)|Корреспондентский счет.<br/>Допустимы только цифры. 20 символов.<br/>|
|*director_name_alt*|True|[string](/types/string)|Должность и ФИО представителя юр. лица (в родительном падеже).<br/>|
|*address_corporate*|True|[string](/types/string)|Юридический адрес.<br/>|
|*corporate_name*|True|[string](/types/string)|Название юридического лица.<br/>|
|*bank*|True|[string](/types/string)|Наименование банка.<br/>|
|*inn*|False|[string](/types/string)|ИНН. Допустимы только цифры. 10 или 12 цифр.<br/>|
