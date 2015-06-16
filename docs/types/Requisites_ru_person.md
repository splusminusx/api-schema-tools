
## Requisites_ru_person

### Описание типа
Requisites_ru_person<br/>Реквизиты плательщика - физического лица РФ.<br/>Таблица 71. Поля реквизитов физического лица РФ<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|first_name|True|[string](/docs/types/string.md)|Имя.<br/>|
|passport_num|False|[string](/docs/types/string.md)|Номер и серия паспорта.<br/>|
|address_reg|False|[string](/docs/types/string.md)|Адрес регистрации.<br/>|
|birthday|False|[date](/docs/types/date.md)|День рождения.<br/>|
|inn|False|[string](/docs/types/string.md)|ИНН. Допустимы только цифры. 12 цифр.<br/>|
|last_name|True|[string](/docs/types/string.md)|Фамилия.<br/>|
|payment_type|True|[string](/docs/types/string.md)|Способ оплаты.<br/>Возможные значения:<br/>emoney – электронный платеж;<br/>wire – банковский перевод.<br/>|
|patronymic|True|[string](/docs/types/string.md)|Отчество.<br/>|
|passport_org|False|[string](/docs/types/string.md)|Кем выдан паспорт.<br/>|
|passport_issued|False|[date](/docs/types/date.md)|Дата выдачи.<br/>|
