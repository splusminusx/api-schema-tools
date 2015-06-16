
## SiteWidgetSettings

### Описание типа
SiteWidgetSettings<br/>Настройки внешнего вида виджета.<br/>Таблица 82. Поля настроек виджета<br/><br/>ПРИМЕЧАНИЯ<br/>Сервис LiveTex предполагает возможность индивидуального дизайна окна чата для конкретного сайта. В этом случае значение настроек могут не соответствовать действительности и их нельзя изменить ни в личном кабинете, ни с помощью методов Web API.<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|**is_department**|True|[boolean](/docs/types/boolean.md)|Включение/выключение выбора отдела для офлайн режима.<br/>По умолчанию – false.<br/>|
|**indent_pos**|True|[string](/docs/types/string.md)|Признак, указывающий на то, от какого края будет отталкиваться виджет.<br/>Возможные значения:<br/>left<br/>rigt<br/>top<br/>bottom<br/>|
|**label_text_offline**|True|[string](/docs/types/string.md)|Текст на ярлыке, когда доступных операторов нет.<br/>По умолчанию – "Оставить заявку".<br/>|
|**color**|False|[string](/docs/types/string.md)|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная (по умолчанию);<br/>yellow – желтая;<br/>white – белая.<br/>Поле обязательно для color_type = preset.<br/>|
|**color_type**|True|[string](/docs/types/string.md)|Тип указания цветовой схемы.<br/>Возможные значения:<br/>preset – стандартная схема (по умолчанию);<br/>custom – явное указание цветов.<br/>|
|**label_text_online**|True|[string](/docs/types/string.md)|Текст на ярлыке, когда есть доступные операторы.<br/>По умолчанию – "Начать чат, мы онлайн".<br/>|
|**color_custom**|False|[color](/docs/types/color.md)|Цвет.<br/>Поле обязательно для color_type = custom.<br/>|
|**is_embedded**|True|[boolean](/docs/types/boolean.md)|Включение/выключение встроенного окна чата.<br/>Если выключено, то будет использоваться внешнее окно чата.<br/>По умолчанию – true.<br/>|
|**banner_custom**|False|[file](/docs/types/file.md)|Загруженная баннер для banner_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с шириной от 1 до 448 px и высотой 82 px.<br/>Максимальный размер файла – 2 MB.<br/>Поле обязательно для banner_type = custom.<br/>Актуально только для внешнего окна.<br/>|
|**updated_at**|True|[datetime](/docs/types/datetime.md)|Дата последнего обновления.<br/>|
|**banner_type**|True|[string](/docs/types/string.md)|Тип баннера.<br/>Возможные значения:<br/>none – без баннера;<br/>default – стандартный баннер (по умолчанию);<br/>custom – загружаемый баннер.<br/>Актуально только для внешнего окна.<br/>|
|**offset_value**|True|[numeric](/docs/types/numeric.md)|Значение отступа в процентах.<br/>Число в диапазоне от 0 до 100. Может быть дробным.<br/>По умолчанию – 80.<br/>|
|**banner_link**|False|[string](/docs/types/string.md)|Ссылка с баннера.<br/>Поле обязательно для banner_type = custom.<br/>Актуально только для внешнего окна.<br/>|
|**position**|True|[string](/docs/types/string.md)|Положение ярлыка.<br/>Возможные значения:<br/>right – справа;<br/>bottom – снизу (по умолчанию);<br/>left – слева.<br/>|
|**is_custom**|True|[boolean](/docs/types/boolean.md)|Признак заказного дизайна виджета.<br/>Если true, то изменение некоторых настроек может не иметь должного результата, поскольку соответствующий аспект внешнего вида переопределяются заказным дизайном.<br/>Это признак доступен только для чтения.<br/>|
|**color_text**|True|[string](/docs/types/string.md)|Цвет текста.<br/>Возможные значения:<br/>light – светлый;<br/>dark – темный;<br/>auto – значение выбирается автоматически (по умолчанию). <br/>|
