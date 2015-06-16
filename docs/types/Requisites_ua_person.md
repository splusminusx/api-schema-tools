
## Requisites_ua_person

### Описание типа
Requisites_ua_person<br/>Реквизиты плательщика – физического лица Украины.<br/>Таблица 73. Поля реквизитов физического лица Украины<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**first_name**|True|[string](/docs/types/string.md)|Имя.<br/>|
|**last_name**|True|[string](/docs/types/string.md)|Фамилия.<br/>|
|**address_reg**|False|[string](/docs/types/string.md)|Адрес регистрации.<br/>|
|**rnokpp**|False|[string](/docs/types/string.md)|РНОКПП.<br/>Допустимы только цифры. 10 символов.<br/>|
|**passport_num**|False|[string](/docs/types/string.md)|Номер и серия паспорта.<br/>|
|**email**|False|[email](/docs/types/email.md)|Адрес электронной почты.<br/>Проверяется на корректный адрес электронной почты.<br/>|
|**address_postal**|False|[string](/docs/types/string.md)|Адрес для приема корреспонденции.<br/>|
|**birthday**|False|[date](/docs/types/date.md)|День рождения.<br/>|
|**payment_type**|True|[string](/docs/types/string.md)|Способ оплаты.<br/>Возможные значения:<br/>emoney – электронный платеж;<br/>wire – банковский перевод.<br/>|
|**patronymic**|True|[string](/docs/types/string.md)|Отчество.<br/>|
|**passport_org**|False|[string](/docs/types/string.md)|Кем выдан паспорт.<br/>|
|**passport_issued**|False|[date](/docs/types/date.md)|Дата выдачи.<br/>|
