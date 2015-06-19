
## Requisites_ua_person

### Описание типа
Реквизиты плательщика – физического лица Украины.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*first_name*|True|[string](/types/string)|Имя.<br/>|
|*last_name*|True|[string](/types/string)|Фамилия.<br/>|
|*address_reg*|False|[string](/types/string)|Адрес регистрации.<br/>|
|*rnokpp*|False|[string](/types/string)|РНОКПП.<br/>Допустимы только цифры. 10 символов.<br/>|
|*passport_num*|False|[string](/types/string)|Номер и серия паспорта.<br/>|
|*email*|False|[email](/types/email)|Адрес электронной почты.<br/>Проверяется на корректный адрес электронной почты.<br/>|
|*address_postal*|False|[string](/types/string)|Адрес для приема корреспонденции.<br/>|
|*birthday*|False|[date](/types/date)|День рождения.<br/>|
|*payment_type*|True|[string](/types/string)|Способ оплаты.<br/>Возможные значения:<br/>emoney – электронный платеж;<br/>wire – банковский перевод.<br/>|
|*patronymic*|True|[string](/types/string)|Отчество.<br/>|
|*passport_org*|False|[string](/types/string)|Кем выдан паспорт.<br/>|
|*passport_issued*|False|[date](/types/date)|Дата выдачи.<br/>|
