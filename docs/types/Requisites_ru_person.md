
## Requisites_ru_person

### Описание типа
Requisites_ru_person
Реквизиты плательщика - физического лица РФ.
Таблица 71. Поля реквизитов физического лица РФ


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|first_name|True|string|Имя.<br/>|
|passport_num|False|string|Номер и серия паспорта.<br/>|
|address_reg|False|string|Адрес регистрации.<br/>|
|birthday|False|date|День рождения.<br/>|
|inn|False|string|ИНН. Допустимы только цифры. 12 цифр.<br/>|
|last_name|True|string|Фамилия.<br/>|
|payment_type|True|string|Способ оплаты.<br/>Возможные значения:<br/>emoney – электронный платеж;<br/>wire – банковский перевод.<br/>|
|patronymic|True|string|Отчество.<br/>|
|passport_org|False|string|Кем выдан паспорт.<br/>|
|passport_issued|False|date|Дата выдачи.<br/>|
