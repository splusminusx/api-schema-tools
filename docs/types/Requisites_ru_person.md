
## Requisites_ru_person

### Описание типа
Реквизиты плательщика - физического лица РФ.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*first_name*|True|[string](/types/string)|Имя.<br/>|
|*passport_num*|False|[string](/types/string)|Номер и серия паспорта.<br/>|
|*address_reg*|False|[string](/types/string)|Адрес регистрации.<br/>|
|*birthday*|False|[date](/types/date)|День рождения.<br/>|
|*inn*|False|[string](/types/string)|ИНН. Допустимы только цифры. 12 цифр.<br/>|
|*last_name*|True|[string](/types/string)|Фамилия.<br/>|
|*payment_type*|True|[string](/types/string)|Способ оплаты.<br/>Возможные значения:<br/>emoney – электронный платеж;<br/>wire – банковский перевод.<br/>|
|*patronymic*|True|[string](/types/string)|Отчество.<br/>|
|*passport_org*|False|[string](/types/string)|Кем выдан паспорт.<br/>|
|*passport_issued*|False|[date](/types/date)|Дата выдачи.<br/>|
