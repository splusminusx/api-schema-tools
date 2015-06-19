
## EmployeeEvent

### Описание типа
Событие сотрудника.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*console_type*|True|[string](/types/string)|Тип Пульта оператора, в котором произошло событие.<br/>Возможные значения:<br/>desktop – Пульт оператора;<br/>iphone – Мобильный пульт оператора для iOS;<br/>android – Мобильный пульт оператора для Android.<br/>|
|*employee_id*|True|[numeric](/types/numeric)|ID сотрудника.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Время события.<br/>|
|*event_type*|True|[string](/types/string)|Тип события.<br/>Возможные значения:<br/>online - сменил статус на «Онлайн»,<br/>busy - сменил статус на «Нет на месте»,<br/>offline - вышел из программы.<br/>|
