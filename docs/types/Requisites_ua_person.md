
## Requisites_ua_person

### Описание типа
Requisites_ua_person
Реквизиты плательщика – физического лица Украины.
Таблица 73. Поля реквизитов физического лица Украины


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|first_name|True|None|Имя.<br/>|
|last_name|True|None|Фамилия.<br/>|
|address_reg|False|None|Адрес регистрации.<br/>|
|rnokpp|False|None|РНОКПП.<br/>Допустимы только цифры. 10 символов.<br/>|
|passport_num|False|None|Номер и серия паспорта.<br/>|
|email|False|None|Адрес электронной почты.<br/>Проверяется на корректный адрес электронной почты.<br/>|
|address_postal|False|None|Адрес для приема корреспонденции.<br/>|
|birthday|False|None|День рождения.<br/>|
|payment_type|True|None|Способ оплаты.<br/>Возможные значения:<br/>emoney – электронный платеж;<br/>wire – банковский перевод.<br/>|
|patronymic|True|None|Отчество.<br/>|
|passport_org|False|None|Кем выдан паспорт.<br/>|
|passport_issued|False|None|Дата выдачи.<br/>|
