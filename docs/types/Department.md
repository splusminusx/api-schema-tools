
## Department

### Описание типа
Отдел.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
|*is_deleted*|True|[boolean](/types/boolean)|Признак удаленного объекта.<br/>|
|*title*|True|[string](/types/string)|Название отдела.<br/>|
|*employees*|True|Array.<[Employee](/types/Employee)>|Список сотрудников отдела.<br/>|
|*sites*|True|Array.<[Site](/types/Site)>|Список сайтов, c которыми связан отдел.<br/>Кроме полей сайта возвращается также поле "alias" - string, псевдоним отдела на данном сайте.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата последнего обновления.<br/>|
|*is_managed*|True|[boolean](/types/boolean)|True, если отдел входит в число своих отделов сотрудника, вызывающего метод.<br/>|
|*id*|True|[numeric](/types/numeric)|ID отдела.<br/>|
