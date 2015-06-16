## WARNING: Type is DEPRECATED
## OfflineFormSettings
### Описание типа
OfflineFormSettings - DEPRECATED
ВНИМАНИЕ! Сущность является устаревшей после ее объединения с LeadFormSettings.
Настройки офлайн-формы.
Таблица 56. Настройки офлайн-формы

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|confirmation|True|string|Текст подтверждения по умолчанию. Максимум 180 символов.<br/>|
|contacts|False|string|Запрашиваемые контактные данные.<br/>email -  запрашивается только email;<br/>phone – запрашивается только телефон;<br/>email_or_phone – запрашивается телефон или email;<br/>email_and_phone – запрашивается телефон и email.<br/>|
|color|False|string|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная,<br/>yellow – желтая;<br/>white – белая.<br/>|
|required_fields|False|string|Обязательность полей при contacts = email_and_phone.<br/>email – e-mail;<br/>phone – телефон;<br/>email_and_phone – email и телефон.<br/>Это поле обязательно при contacts = email_and_phone.<br/>|
|welcome|True|string|Текст приветствия по умолчанию. Максимум 180 символов.<br/>|
|banner_custom|False|file|Загруженная баннер для banner_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с шириной от 1 до 448 px и высотой 82 px.<br/>Поле обязательно для banner_type = custom.<br/>|
|background_custom|False|file|Загруженный фон для background_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с размерами 448x605px.<br/>Поле обязательно для background_type = custom.<br/>|
|updated_at|True|datetime|Дата последнего обновления.<br/>|
|banner_type|True|string|Тип баннера.<br/>Возможные значения:<br/>none – без баннера;<br/>default – стандартный баннер;<br/>custom – загружаемый баннер.<br/>|
|is_custom|True|boolean|Признак заказного дизайна офлайн-формы.<br/>Если true, то изменение некоторых настроек может не иметь должного результата, поскольку соответствующий аспект внешнего вида переопределяются заказным дизайном.<br/>Это признак доступен только для чтения.<br/>|
|banner_link|False|string|Ссылка с баннера.<br/>Поле обязательно для banner_type = custom.<br/>|
|confirmation_mobile|True|string|Текст подтверждения по умолчанию, который отобразится в мобильном браузере. Максимум 180 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|background_typе|True|string|Тип фона.<br/>Возможные значения:<br/>none – без фона;<br/>default – стандартный фон;<br/>custom – загружаемый фон.<br/>|
|welcome_mobile|True|string|Текст приветствия по умолчанию, который отобразиться в мобильном браузере. Максимум 180 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|