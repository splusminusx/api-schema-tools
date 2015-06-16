
## Prechat

### Описание типа
Prechat
Пречат-поле.
Таблица 63. Поля пречат-поля


### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|field_type|True|[string](/docs/types/string.md)|Тип поля.<br/>Возможные значения:<br/>string – строка;<br/>list – список, в поле options необходимо указать список возможных значений для выбора через символ новой строки (LF);<br/>phone – телефон;<br/>number – число;<br/>email – email;<br/>mask – маска, в поле options необходимо указать регулярное выражение, определяющее маску.<br/>|
|title|True|[string](/docs/types/string.md)|Название поля.<br/>|
|is_active|True|[boolean](/docs/types/boolean.md)|Признак активности поля.<br/>Если true, то поле показывается в форме приглашения. В противном случае – нет.<br/>|
|updated_at|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|is_required|True|[boolean](/docs/types/boolean.md)|Признак обязательности заполнения поля.<br/>|
|options|False|[string](/docs/types/string.md)|Дополнительные свойства поля. Зависит от типа.<br/>Обязательное для field_type=list и field_type=mask.<br/>|
