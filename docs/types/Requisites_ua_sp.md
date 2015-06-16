
## Requisites_ua_sp

### Описание типа
Requisites_ua_sp<br/>Реквизиты плательщика – ФОП Украины.<br/>Таблица 75. Поля реквизитов ФОП Украины<br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**director_name**|True|[string](/docs/types/string.md)|Должность и ФИО лица, подписывающего документы.<br/>|
|**signer_basis**|True|[string](/docs/types/string.md)|На основании имеет право подписывать документы (“на пiдставi”).<br/>|
|**edruofop_number**|True|[string](/docs/types/string.md)|Дата и номер записи в “єдиному державному реєстрі юридичних та фiзичних осiб-пiдприємцiв”<br/>|
|**rnokpp**|True|[string](/docs/types/string.md)|РНОКПП.<br/>Допустимы только цифры. 10 символов.<br/>|
|**pdv**|False|[string](/docs/types/string.md)|Свидетельство ПДВ.<br/>Допустимы только цифры. 8 или 9 символов.<br/>|
|**account_r**|False|[string](/docs/types/string.md)|Номер счета.<br/>Допустимы только цифры. От 4 до 14 символов.<br/>|
|**ipn**|False|[string](/docs/types/string.md)|IПН.<br/>Допустимы только цифры. 15 символов<br/>|
|**corporate_name**|True|[string](/docs/types/string.md)|Название юридического лица.<br/>|
|**address_postal**|True|[string](/docs/types/string.md)|Адрес для приёма корреспонденции.<br/>|
|**director_name_alt**|True|[string](/docs/types/string.md)|Должность и ФИО представителя юр. лица (в родительном падеже).<br/>|
|**address_corporate**|True|[string](/docs/types/string.md)|Местонахождение.<br/>|
|**mfo**|False|[string](/docs/types/string.md)|МФО.<br/>Допустимы только цифры. Максимум 6 символов.<br/>|
|**unified_tax**|True|[string](/docs/types/string.md)|Является ли плательщиком единого 5% налога<br/>|
|**bank**|False|[string](/docs/types/string.md)|Банковские данные.<br/>|
|**edrpou**|True|[string](/docs/types/string.md)|ЄДРПОУ.<br/>Допустимы только цифры. 8 символов.<br/>|
