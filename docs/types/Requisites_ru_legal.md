
## Requisites_ru_legal

### Описание типа
Requisites_ru_legal<br/>Реквизиты плательщика - юридического лица РФ.<br/>Таблица 72. Поля реквизитов юридического лица РФ<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*kpp*|False|[string](/docs/types/string.md)|КПП. 9 символов.<br/>|
|*signer_basis*|True|[string](/docs/types/string.md)|На основании чего имеет право подписывать документы.<br/>|
|*address_postal*|True|[string](/docs/types/string.md)|Физический адрес.<br/>|
|*account_r*|True|[string](/docs/types/string.md)|Расчетный счет.<br/>Допустимы только цифры. 20 символов.<br/>|
|*bic*|True|[string](/docs/types/string.md)|БИК.<br/>Допустимы только цифры. 9 символов.<br/>|
|*ogrn*|False|[string](/docs/types/string.md)|ОГРН. 13 или 15 символов.<br/>|
|*director_name*|True|[string](/docs/types/string.md)|Должность и ФИО лица, подписывающего документы.<br/>|
|*account_k*|True|[string](/docs/types/string.md)|Корреспондентский счет.<br/>Допустимы только цифры. 20 символов.<br/>|
|*director_name_alt*|True|[string](/docs/types/string.md)|Должность и ФИО представителя юр. лица (в родительном падеже).<br/>|
|*address_corporate*|True|[string](/docs/types/string.md)|Юридический адрес.<br/>|
|*corporate_name*|True|[string](/docs/types/string.md)|Название юридического лица.<br/>|
|*bank*|True|[string](/docs/types/string.md)|Наименование банка.<br/>|
|*inn*|False|[string](/docs/types/string.md)|ИНН. Допустимы только цифры. 10 или 12 цифр.<br/>|
