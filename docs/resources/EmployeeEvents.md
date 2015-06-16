
# EmployeeEvents

## Описание ресурса

# Методы

## list

### Описание метода
Возвращает список события сотрудника.<br/>Массив объектов типа «EmployeeEvent».<br/>Пример<br/>curl https://api.livetex.ru/v2/employeeevents?employee_ids=12345 \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>{<br/>	"total": 2,<br/>	"results": [<br/>		{<br/>			"created_at": "2012-12-07T09:14:57+04:00",<br/>			"event_type":"online"<br/>		},<br/>		{<br/>			"created_at": "2012-12-07T12:34:23+04:00",<br/>			"event_type":"busy"<br/>		},<br/>		{<br/>			"created_at": "2012-12-07T18:10:13+04:00",<br/>			"event_type":"offline"<br/>		}<br/>	]<br/>}<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>employee_ids – idlist, список ID сотрудников;<br/>event_type;<br/>created_at.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию.<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[EmployeeEvent](/docs/types/EmployeeEvent.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|События своих сотрудников.|
|*chief*|managed|События своих сотрудников.|
|*chief_partner*|managed|События своих сотрудников.|
|*operator*|user|Свои данные.|
|*admin_partner*|full||
