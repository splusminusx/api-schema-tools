## Requisites_ua_person
### Описание типа
Requisites_ua_person
Реквизиты плательщика – физического лица Украины.
Таблица 73. Поля реквизитов физического лица Украины

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|first_name|True|string|Имя.<br/>|
|last_name|True|string|Фамилия.<br/>|
|address_reg|False|string|Адрес регистрации.<br/>|
|rnokpp|False|string|РНОКПП.<br/>Допустимы только цифры. 10 символов.<br/>|
|passport_num|False|string|Номер и серия паспорта.<br/>|
|email|False|email|Адрес электронной почты.<br/>Проверяется на корректный адрес электронной почты.<br/>|
|address_postal|False|string|Адрес для приема корреспонденции.<br/>|
|birthday|False|date|День рождения.<br/>|
|payment_type|True|string|Способ оплаты.<br/>Возможные значения:<br/>emoney – электронный платеж;<br/>wire – банковский перевод.<br/>|
|patronymic|True|string|Отчество.<br/>|
|passport_org|False|string|Кем выдан паспорт.<br/>|
|passport_issued|False|date|Дата выдачи.<br/>|
