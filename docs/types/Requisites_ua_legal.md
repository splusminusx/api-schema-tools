
## Requisites_ua_legal

### Описание типа
Requisites_ua_legal<br/>Реквизиты плательщика – юридического лица Украины.<br/>Таблица 74. Поля реквизитов юридического лица Украины<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|director_name|True|[string](/docs/types/string.md)|Должность и ФИО лица, подписывающего документы.<br/>|
|signer_basis|True|[string](/docs/types/string.md)|На основании («на пiдставi»).<br/>|
|address_postal|True|[string](/docs/types/string.md)|Адрес для приёма корреспонденции.<br/>|
|pdv|False|[string](/docs/types/string.md)|Свидетельство ПДВ.<br/>Допустимы только цифры. 8 или 9 символов.<br/>|
|account_r|True|[string](/docs/types/string.md)|Номер счета.<br/>Допустимы только цифры. От 4 до 14 символов.<br/>|
|ipn|False|[string](/docs/types/string.md)|IПН.<br/>Допустимы только цифры. 15 символов.<br/>|
|corporate_name|True|[string](/docs/types/string.md)|Название юридического лица.<br/>|
|director_name_alt|True|[string](/docs/types/string.md)|Должность и ФИО представителя юр. лица (в родительном падеже).<br/>|
|address_corporate|True|[string](/docs/types/string.md)|Местонахождение.<br/>|
|mfo|True|[string](/docs/types/string.md)|МФО.<br/>Допустимы только цифры. 6 символов.<br/>|
|unified_tax|True|[string](/docs/types/string.md)|Является ли плательщиком единого 5% налога.<br/>В данный момент это строковое поле, куда народ пишет всякое. Уточнить, быть может это надо сделать boolean и, соответственно переделать UI.<br/>|
|bank|True|[string](/docs/types/string.md)|Банковские данные.<br/>|
|edrpou|True|[string](/docs/types/string.md)|ЄДРПОУ.<br/>Допустимы только цифры. 8 символов.<br/>|
