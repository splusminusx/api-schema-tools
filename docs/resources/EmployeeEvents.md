
# EmployeeEvents

## Описание ресурса
EmployeeEvents

# Методы

## list

### Описание метода
EmployeeEvents.list
Возвращает список события сотрудника.
Параметры
Результат
Массив объектов типа «EmployeeEvent».
Пример
curl https://api.livetex.ru/v2/employeeevents?employee_ids=12345 \
-H "Authorization: Bearer ACCESS_TOKEN"

{
	"total": 2,
	"results": [
		{
			"created_at": "2012-12-07T09:14:57+04:00",
			"event_type":"online"
		},
		{
			"created_at": "2012-12-07T12:34:23+04:00",
			"event_type":"busy"
		},
		{
			"created_at": "2012-12-07T18:10:13+04:00",
			"event_type":"offline"
		}
	]
}
Уровень доступа для ролей


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|string|Критерий поиска.<br/>Доступные поля:<br/>employee_ids – idlist, список ID сотрудников;<br/>event_type;<br/>created_at.<br/>|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|limit|False|numeric|По умолчанию – 50.<br/>|
|sort|False|string|Сортировка результатов.<br/>Возможные значения:<br/>created_at:d – по умолчанию.<br/>|
|offset|False|numeric|По умолчанию – 0.<br/>|

### Резудьтат
Array.<[EmployeeEvent](types/EmployeeEvent.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner