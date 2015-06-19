
## Prechat

### Описание типа
Пречат-поле.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*field_type*|True|[string](/types/string)|Тип поля.<br/>Возможные значения:<br/>string – строка;<br/>list – список, в поле options необходимо указать список возможных значений для выбора через символ новой строки (LF);<br/>phone – телефон;<br/>number – число;<br/>email – email;<br/>mask – маска, в поле options необходимо указать регулярное выражение, определяющее маску.<br/>|
|*title*|True|[string](/types/string)|Название поля.<br/>|
|*is_active*|True|[boolean](/types/boolean)|Признак активности поля.<br/>Если true, то поле показывается в форме приглашения. В противном случае – нет.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата последнего обновления.<br/>|
|*is_required*|True|[boolean](/types/boolean)|Признак обязательности заполнения поля.<br/>|
|*options*|False|[string](/types/string)|Дополнительные свойства поля. Зависит от типа.<br/>Обязательное для field_type=list и field_type=mask.<br/>|
