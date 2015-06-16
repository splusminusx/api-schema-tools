
## Department

### Описание типа
Department<br/>Отдел.<br/>Таблица 33. Поля отдела<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|created_at|True|[datetime](/docs/types/datetime.md)|Дата создания.<br/>|
|is_deleted|True|[boolean](/docs/types/boolean.md)|Признак удаленного объекта.<br/>|
|title|True|[string](/docs/types/string.md)|Название отдела.<br/>|
|employees|True|Array.<[Employee](/docs/types/Employee.md)>|Список сотрудников отдела.<br/>|
|sites|True|Array.<[Site](/docs/types/Site.md)>|Список сайтов, c которыми связан отдел.<br/>Кроме полей сайта возвращается также поле "alias" - string, псевдоним отдела на данном сайте.<br/>|
|updated_at|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|is_managed|True|[boolean](/docs/types/boolean.md)|True, если отдел входит в число своих отделов сотрудника, вызывающего метод.<br/>|
|id|True|[numeric](/docs/types/numeric.md)|ID отдела.<br/>|
