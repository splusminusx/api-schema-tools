
## EmployeeEvent

### Описание типа
EmployeeEvent<br/>Событие сотрудника.<br/>Таблица 38. Поля события сотрудника<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|console_type|True|[string](/docs/types/string.md)|Тип Пульта оператора, в котором произошло событие.<br/>Возможные значения:<br/>desktop – Пульт оператора;<br/>iphone – Мобильный пульт оператора для iOS;<br/>android – Мобильный пульт оператора для Android.<br/>|
|employee_id|True|[numeric](/docs/types/numeric.md)|ID сотрудника.<br/>|
|created_at|True|[datetime](/docs/types/datetime.md)|Время события.<br/>|
|event_type|True|[string](/docs/types/string.md)|Тип события.<br/>Возможные значения:<br/>online - сменил статус на «Онлайн»,<br/>busy - сменил статус на «Нет на месте»,<br/>offline - вышел из программы.<br/>|
