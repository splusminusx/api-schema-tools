
## Payer

### Описание типа
Плательщик.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*requisites*|True|[Requisites](/types/Requisites)|Реквизиты плательщика.<br/>Тип реквизитов должен соответствовать payer_type.<br/>См. подразделы раздела Requisites.<br/>|
|*is_recurring*|True|[boolean](/types/boolean)|Включение/выключение рекуррентных платежей.<br/>По умолчанию – false.<br/>|
|*is_active*|True|[boolean](/types/boolean)|Признак активного плательщика.<br/>В один момент времени может быть только один активный плательщик. Таковым всегда является последний созданный плательщик.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*payer_type*|True|[string](/types/string)|Тип плательщика.<br/>Возможные значения:<br/>ru_person – физическое лицо РФ;<br/>ru_legal – юридическое лицо РФ;<br/>ua_person – физическое лицо Украины;<br/>ua_legal – юридическое лицо Украины;<br/>ua_sp – ФОП Украины.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата изменения.<br/>|
|*contract*|False|[Contract](/types/Contract)|Договор.<br/>Если null, то плательщик действует по стандартному договору оферты.<br/>|
|*id*|True|[numeric](/types/numeric)|ID плательщика.<br/>|
|*currency*|True|[currency](/types/currency)|Валюта плательщика.<br/>Устанавливается для payer_type. Только для чтения.<br/>|
|*recurring_card*|False|[string](/types/string)|4 последние цифры номера карты, зарегистрированной для рекуррентных платежей.<br/>|
|*recurring_order*|False|[string](/types/string)|Номер договора на рекуррентные платежи.<br/>|
|*balance*|True|[numeric](/types/numeric)|Остаток на cчете.<br/>|
|*balance_bonus*|True|[numeric](/types/numeric)|Остаток на подарочном счете.<br/>|
