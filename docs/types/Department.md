
## Department

### Описание типа
Department
Отдел.
Таблица 33. Поля отдела


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|created_at|True|datetime|Дата создания.<br/>|
|is_deleted|True|boolean|Признак удаленного объекта.<br/>|
|title|True|string|Название отдела.<br/>|
|employees|True|Array.<[Employee](/docs/types/Employee.md)>|Список сотрудников отдела.<br/>|
|sites|True|Array.<[Site](/docs/types/Site.md)>|Список сайтов, c которыми связан отдел.<br/>Кроме полей сайта возвращается также поле "alias" - string, псевдоним отдела на данном сайте.<br/>|
|updated_at|True|datetime|Дата последнего обновления.<br/>|
|is_managed|True|boolean|True, если отдел входит в число своих отделов сотрудника, вызывающего метод.<br/>|
|id|True|numeric|ID отдела.<br/>|
