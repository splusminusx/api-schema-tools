
## Payer

### Описание типа
Payer
Плательщик.
Таблица 60. Поля плательщика


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|requisites|True|[Requisites](/docs/types/Requisites.md)|Реквизиты плательщика.<br/>Тип реквизитов должен соответствовать payer_type.<br/>См. подразделы раздела Requisites.<br/>|
|is_recurring|True|[boolean](/docs/types/boolean.md)|Включение/выключение рекуррентных платежей.<br/>По умолчанию – false.<br/>|
|is_active|True|[boolean](/docs/types/boolean.md)|Признак активного плательщика.<br/>В один момент времени может быть только один активный плательщик. Таковым всегда является последний созданный плательщик.<br/>|
|created_at|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|payer_type|True|[string](/docs/types/string.md)|Тип плательщика.<br/>Возможные значения:<br/>ru_person – физическое лицо РФ;<br/>ru_legal – юридическое лицо РФ;<br/>ua_person – физическое лицо Украины;<br/>ua_legal – юридическое лицо Украины;<br/>ua_sp – ФОП Украины.<br/>|
|updated_at|True|[datetime](/docs/types/datetime.md)|Дата изменения.<br/>|
|contract|False|[Contract](/docs/types/Contract.md)|Договор.<br/>Если null, то плательщик действует по стандартному договору оферты.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID плательщика.<br/>|
|currency|True|[currency](/docs/types/currency.md)|Валюта плательщика.<br/>Устанавливается для payer_type. Только для чтения.<br/>|
|recurring_card|False|[string](/docs/types/string.md)|4 последние цифры номера карты, зарегистрированной для рекуррентных платежей.<br/>|
|recurring_order|False|[string](/docs/types/string.md)|Номер договора на рекуррентные платежи.<br/>|
|balance|True|[numeric](/docs/types/numeric.md)|Остаток на cчете.<br/>|
|balance_bonus|True|[numeric](/docs/types/numeric.md)|Остаток на подарочном счете.<br/>|
