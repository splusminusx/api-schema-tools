
## Requisites_ru_person

### Описание типа
Requisites_ru_person
Реквизиты плательщика - физического лица РФ.
Таблица 71. Поля реквизитов физического лица РФ


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|first_name|True|None|Имя.<br/>|
|passport_num|False|None|Номер и серия паспорта.<br/>|
|address_reg|False|None|Адрес регистрации.<br/>|
|birthday|False|None|День рождения.<br/>|
|inn|False|None|ИНН. Допустимы только цифры. 12 цифр.<br/>|
|last_name|True|None|Фамилия.<br/>|
|payment_type|True|None|Способ оплаты.<br/>Возможные значения:<br/>emoney – электронный платеж;<br/>wire – банковский перевод.<br/>|
|patronymic|True|None|Отчество.<br/>|
|passport_org|False|None|Кем выдан паспорт.<br/>|
|passport_issued|False|None|Дата выдачи.<br/>|
