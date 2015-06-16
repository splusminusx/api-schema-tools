# Sites
## Описание ресурса
Sites
# Методы
## updateOfflineMailSettings
### Описание метода
Sites.updateOfflineMailSettings
Изменяет настройки офлайн почты.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|from_name|False|string|Отправитель.<br/>Максимум 60 символов.<br/>|
|is_active|False|boolean|Включение/выключение использования внешнего почтового ящика.<br/>Если функция выключена, то письма будут отправляться через сервера LiveTex c системными значениями отправителя, темы и подписи.<br/>|
|signature|False|string|Подпись.<br/>Максимум 60 символов.<br/>|
|mailbox_id|False|numeric|ID почтового ящика.<br/>Если указано null, то для отправки почты будут использоваться сервера LiveTex.<br/>|
|id|True|numeric|ID сайта.<br/>|
|subject|False|string|Тема письма.<br/>Максимум 60 символов.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## showSiteCallSettings
### Описание метода
Sites.showSiteCallSettings
Возвращает настройки звонков указанного сайта.
Параметры
Результат
Объект типа «SiteCallSettings».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## show
### Описание метода
Sites.show
Возвращает данные указанного сайта.
Параметры
Результат
Объект типа «Site».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## list
### Описание метода
Sites.list
Возвращает список сайтов.
Параметры
Результат
Массив объектов типа «Site».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|q|False|string|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID сайтов.<br/>url – string, подстрока в адресе сайта.<br/>is_managed – boolean, признак своего сайта.<br/>|
|fields|False|string|Список через запятую возвращаемых полей.<br/>|
|limit|False|numeric|По умолчанию – 50.<br/>|
|sort|False|string|Сортировка результатов.<br/>Возможные значения:<br/>url:a – по умолчанию;<br/>updated_at:a, updated_at:d;<br/>|
|offset|False|numeric|По умолчанию – 0.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## WARNING: Type is DEPRECATED
## updateChatFormSettings
### Описание метода
Sites.updateChatFormSettings - DEPRECATED
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию. Все перенесено в updateWidgetSettings.
Изменяет настройки окна чата сайта.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|offset_value|False|numeric|Значение отступа.<br/>Целое число в диапазоне:<br/>от 0 до 100 для offset_type = percent;<br/>от 0 до 2000 для offset_type = pixel.<br/>|
|color|False|string|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>Поле обязательно для color_type = preset.<br/>|
|photo_size|False|string|Размер фотографии сотрудника.<br/>Возможные значения:<br/>small – маленькая, 60x70 пикселей;<br/>large – большая, 100x116 пикселей.<br/>|
|color_text|False|color|Цвет текста.<br/>Поле обязательно для color_type = custom.<br/>|
|color_main|False|color|Основной цвет.<br/>Поле обязательно для color_type = custom.<br/>|
|is_hidden_offline|False|boolean|Скрывать ярлык, если сотрудники офлайн.<br/>|
|offset_type|False|string|Тип отступа.<br/>Возможные значения:<br/>pixel – в пикселах;<br/>percent – в процентах.<br/>|
|banner_type|False|string|Тип баннера.<br/>Возможные значения:<br/>none – без баннера;<br/>default – стандартный баннер;<br/>custom – загружаемый баннер.<br/>|
|color_background|False|color|Цвет фона.<br/>Поле обязательно для color_type = custom.<br/>|
|banner_custom|False|file|Загруженная баннер для banner_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с шириной от 1 до 448 px и высотой 82 px.<br/>Поле обязательно для banner_type = custom.<br/>|
|banner_link|False|string|Ссылка с баннера.<br/>Поле обязательно для banner_type = custom.<br/>|
|position|False|string|Положение ярлыка.<br/>Возможные значения:<br/>top – сверху;<br/>right – справа;<br/>bottom – снизу;<br/>left – слева.<br/>|
|is_label_visible|False|boolean|Признак отображения ярлыка.<br/>По умолчанию – true.<br/>Если false, ярлык не будет показываться посетителю, даже при наличии доступных операторов.<br/>Это признак автоматически устанавливается в true и не может быть изменен, если подключена опция генератора лидов или для сайта включено встроенное окно чата (site.is_embedded_chat == true).<br/>Признак is_label_visible связан с полем size. При переключении из false в true поле size устанавливается в значение по умолчанию.<br/>|
|logo_type|False|string|Тип логотипа LiveTex.<br/>Возможные значения:<br/>animated – анимированный;<br/>static – статический.<br/>|
|id|True|numeric|ID сайта.<br/>|
|background_custom|False|file|Загруженный фон для background_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с размерами 448x605px.<br/>Поле обязательно для background_type = custom.<br/>|
|background_typе|False|string|Тип фона.<br/>Возможные значения:<br/>none – без фона;<br/>default – стандартный фон;<br/>custom – загружаемый фон.<br/>|
|color_type|False|string|Тип указания цветовой схемы.<br/>Возможные значения:<br/>preset – стандартная схема;<br/>custom – явное указание цветов.<br/>|
|size|False|string|Размер ярлыка.<br/>Возможные значения:<br/>small – маленький, 24x106 пикселей;<br/>large – большой, 40x178 пикселей (по умолчанию).<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## showSiteChatSettings
### Описание метода
Sites.showSiteChatSettings
Возвращает настройки чата для указанного сайта.
Параметры
Результат
Объект типа «SiteChatSettings».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## WARNING: Type is DEPRECATED
## showChatWelcomeSettings
### Описание метода
Sites.showChatWelcomeSettings – DEPRECATED
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию. Все перенесено в showWidgetSettings.
Возвращает настройки окна приветствия указанного сайта.
Параметры
Результат
Объект типа «ChatWelcomeSettings».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## batchUpdate
### Описание метода
Sites.batchUpdate
Выполняет пакетное изменение данных указанных сайтов.
Метод вызывает Sites.update для каждого ID сайта и передает указанные параметры.
Параметры
Результат
Массив объектов c ID, кодами и сообщениями об ошибке в порядке перечисления ID сайтов в запросе.
Пример
curl https://api.livetex.ru/v2/sites/batchupdate \
-H "Authorization: Bearer ACCESS_TOKEN" \
-d "ids=123,456,789" \
-d "is_callback=false"

{
    "results": [
        {
            "id": "123",
            "code": 200,
            "message": ""
        },
        {
            "id": "456",
            "code": 200,
            "message": ""
        },
        {
            "id": "789",
            "code": 403,
            "message": "Forbidden"
        }
    ]
}

Уровень доступа для ролей

ВНИМАНИЕ!
При изменении конкретного сайта работает уровень доступа метода Sites.update в соответствующих условиях.
### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_complaint|False|boolean|Включение/выключение жалоб.<br/>|
|is_callback|False|boolean|Включение/выключение функциональности «Перезвоните мне».<br/>|
|ids|True|idlist|Список, через запятую, ID сайтов.<br/>|
|complaint_email|False|string|Адрес электронной почты, на который будут отправляться нотификации о поступлении новой жалобы.<br/>|
|is_vote|False|boolean|Включение/выключение функциональности оценки чата посетителем.<br/>|
|is_mobile|False|boolean|Включение/выключение мобильного вида виджета.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## WARNING: Type is DEPRECATED
## showOfflineFormSettings
### Описание метода
Sites.showOfflineFormSettings – DEPRECATED
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию.
Возвращает настройки формы офлайн-сообщения указанного сайта.
Параметры
Результат
Объект типа «OfflineFormSettings».
Пример запроса
curl https://api.livetex.ru/v2/sites/showofflineformsettings?id=12345 \
-H "Authorization: Bearer ACCESS_TOKEN"
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## showOfflineMailSettings
### Описание метода
Sites.showOfflineMailSettings
Возвращает настройки офлайн почты.
Параметры
Результат
Объект типа «OfflineMailSettings».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## showSiteWidgetSettings
### Описание метода
Sites.showSiteWidgetSettings
Возвращает настройки виджета для указанного сайта.
Параметры
Результат
Объект типа «SiteWidgetSettings».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## add
### Описание метода
Sites.add
Создает новый сайт.
ВНИМАНИЕ!
Новый сайт автоматически добавляется в поле managed_sites всем сотрудникам с ролью, имеющей is_full_by_default = true.
Параметры
Результат
Объект типа «Site».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|prechats_chat|False|Array.<Prechat>|Массив объектов типа Prechat.<br/>Максимум 2 элемента.<br/>|
|is_lead|False|boolean|Включение/выключение функциональности генератора лидов.<br/>По умолчанию – true.<br/>|
|is_call_label|False|boolean|Включение/выключение ярлыка звонков.<br/>DEPRECATED!<br/>|
|employee_ids|False|idlist|Список ID сотрудников через запятую.<br/>|
|url|True|string|Адрес сайта.<br/>Например: www.mysite.ru<br/>|
|is_callback|False|boolean|Включение/выключение функциональности «Перезвоните мне».<br/>По умолчанию – true.<br/>|
|is_complaint|False|boolean|Включение/выключение жалоб.<br/>По умолчанию – false.<br/>|
|is_hidden_offline|False|boolean|Скрывать ярлык, если сотрудники офлайн.<br/>По умолчанию – false.<br/>|
|complaint_email|False|email|Адрес электронной почты, на который будут отправляться нотификации о поступлении новой жалобы.<br/>Обязателен, если указано is_complaint = true.<br/>|
|is_vote|False|boolean|Включение/выключение функциональности оценки чата посетителем.<br/>По умолчанию – true.<br/>|
|is_mobile|False|boolean|Включение/выключение мобильного вида виджета.<br/>|
|is_site_prechats|False|boolean|Признак использования пречат-полей сайта.<br/>Если false, то будут использоваться пречаты из связей отделов с сайтом.<br/>По умолчанию – true.<br/>|
|callback_url|False|string|Настройка Callback URL.<br/>|
|hold_rule_id|False|numeric|ID сценария удержания.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## WARNING: Type is DEPRECATED
## showChatFormSettings
### Описание метода
Sites.showChatFormSettings - DEPRECATED
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию. Все перенесено в showWidgetSettings.
Возвращает настройки окна чата указанного сайта.
Параметры
Результат
Объект типа «ChatFormSettings».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## updateSiteChatSettings
### Описание метода
Sites.updateSiteChatSettings
Изменяет настройки чата для указанного сайта.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|offline_contacts|False|string|Запрашиваемые контактные данные в офлайн-режиме.<br/>Возможные значения:<br/>email -  запрашивается только email;<br/>phone – запрашивается только телефон;<br/>email_or_phone – запрашивается телефон или email;<br/>email_and_phone – запрашивается телефон и email.<br/>|
|offline_confirmation|False|string|Текст подтверждения в режиме офлайн. Отображается после успешной отправки запроса.<br/>Максимум 180 символов.<br/>|
|offline_contacts_required|False|string|Обязательность полей при offline_contacts=email_and_phone.<br/>Возможные значения:<br/>email – e-mail;<br/>phone – телефон;<br/>email_and_phone – email и телефон.<br/>|
|offline_welcome|False|string|Текст приветствия в режиме офлайн.<br/>Максимум 180 символов.<br/>|
|id|True|numeric|ID сайта.<br/>|
|online_welcome|False|string|Текст приветствия в режиме онлайн.<br/>Максимум 180 символов.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## WARNING: Type is DEPRECATED
## updateCallLabelSettings
### Описание метода
Sites.updateCallLabelSettings - DEPRECATED
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию.
Изменяет звонковые настройки сайта.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_visible|False|boolean|Показывать ярлык.<br/>|
|offset_value|False|numeric|Значение отступа.<br/>Целое число в диапазоне:<br/>от 0 до 100 для offset_type = percent;<br/>от 0 до 2000 для offset_type = pixel.<br/>|
|color|False|string|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>|
|offset_type|False|string|Тип отступа.<br/>Возможные значения:<br/>pixel – в пикселах;<br/>percent – в процентах.<br/>|
|position|False|string|Положение ярлыка.<br/>Возможные значения:<br/>top – сверху;<br/>right – справа;<br/>bottom – снизу;<br/>left – слева.<br/>|
|size|False|string|Размер ярлыка.<br/>Возможные значения:<br/>small – маленький, 23x118 пикселей;<br/>large – большой, 38x174 пикселей.<br/>|
|id|True|numeric|ID сайта.<br/>|
|department_id|False|numeric|ID отдела.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## updateSiteWidgetSettings
### Описание метода
Sites.updateSiteWidgetSettings
Изменяет настройки виджета для указанного сайта.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_department|False|boolean|Включение/выключение выбора отдела для офлайн режима.<br/>При создании сайта устанавливается в false.<br/>|
|offset_value|False|numeric|Значение отступа в процентах.<br/>Число в диапазоне от 0 до 100. Может быть дробным.<br/>|
|label_text_offline|False|string|Текст на ярлыке, когда доступных операторов нет.<br/>|
|color|False|string|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>Поле обязательно для color_type = preset.<br/>|
|color_type|False|string|Тип указания цветовой схемы.<br/>Возможные значения:<br/>preset – стандартная схема;<br/>custom – явное указание цветов.<br/>|
|label_text_online|False|string|Текст на ярлыке, когда есть доступные операторы.<br/>|
|color_custom|False|color|Цвет.<br/>Поле обязательно для color_type = custom.<br/>|
|is_embedded|False|boolean|Включение/выключение встроенного окна чата.<br/>Если выключено, то будет использоваться внешнее окно чата.<br/>|
|banner_custom|False|file|Загруженная баннер для banner_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с шириной от 1 до 448 px и высотой 82 px.<br/>Максимальный размер файла – 2 MB.<br/>Поле обязательно для banner_type = custom.<br/>Актуально только для внешнего окна.<br/>|
|banner_type|False|string|Тип баннера.<br/>Возможные значения:<br/>none – без баннера;<br/>default – стандартный баннер;<br/>custom – загружаемый баннер.<br/>Актуально только для внешнего окна.<br/>|
|banner_link|False|string|Ссылка с баннера.<br/>Поле обязательно для banner_type = custom.<br/>Актуально только для внешнего окна.<br/>|
|position|False|string|Положение ярлыка.<br/>Возможные значения:<br/>right – справа;<br/>bottom – снизу;<br/>left – слева.<br/>|
|id|True|numeric|ID сайта.<br/>|
|color_text|False|string|Цвет текста.<br/>Возможные значения:<br/>light – светлый;<br/>dark – темный;<br/>auto – значение выбирается автоматически.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## showSiteXWidgetSettings
### Описание метода
Sites.showSiteXWidgetSettings
Возвращает настройки продукта «X-widget» для указанного сайта.
Параметры
Результат
Объект типа «SiteXWidgetSettings».
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## WARNING: Type is DEPRECATED
## updateOfflineFormSettings
### Описание метода
Sites.updateOfflineFormSettings - DEPRECATED
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию.
Обновляет настройки офлайн-формы.
Параметры
Результат
Метод ничего не возвращает.
Пример запроса
curl https://api.livetex.ru/v2/sites/updateofflineformsettings \
-H "Authorization: Bearer ACCESS_TOKEN" \
–d "id=12345" \
–d "banner_type=none"
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|confirmation|False|string|Текст подтверждения по умолчанию.<br/>Максимум 180 символов.<br/>|
|contacts|False|string|Запрашиваемые контактные данные.<br/>email -  запрашивается только email;<br/>phone – запрашивается только телефон;<br/>email_or_phone – запрашивается телефон или email;<br/>email_and_phone – запрашивается телефон и email.<br/>|
|color|False|string|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>|
|required_fields|False|string|Обязательность полей при contacts = email_and_phone.<br/>email – e-mail;<br/>phone – телефон;<br/>email_and_phone – email и телефон.<br/>Это поле обязательно при contacts = email_and_phone.<br/>|
|welcome|False|string|Текст приветствия по умолчанию.<br/>Максимум 180 символов.<br/>|
|banner_custom|False|file|Загруженная баннер для banner_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с шириной от 1 до 448 px и высотой 82 px.<br/>Поле обязательно для banner_type = custom.<br/>|
|background_custom|False|file|Загруженный фон для background_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с размерами 448x605px.<br/>Поле обязательно для background_type = custom.<br/>|
|banner_type|False|string|Тип баннера.<br/>Возможные значения:<br/>none – без баннера;<br/>default – стандартный баннер;<br/>custom – загружаемый баннер.<br/>|
|banner_link|False|string|Ссылка с баннера.<br/>Поле обязательно для banner_type = custom.<br/>|
|confirmation_mobile|False|string|Текст подтверждения по умолчанию, который отобразится в мобильных браузерах.<br/>Максимум 180 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|background_typе|False|string|Тип фона.<br/>Возможные значения:<br/>none – без фона;<br/>default – стандартный фон;<br/>custom – загружаемый фон.<br/>|
|id|True|numeric|ID сайта.<br/>|
|welcome_mobile|False|string|Текст приветствия по умолчанию, который отобразится в мобильных браузерах.<br/>Максимум 180 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## WARNING: Type is DEPRECATED
## updateChatWelcomeSettings
### Описание метода
Sites.updateChatWelcomeSettings - DEPRECATED
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию. Все перенесено в updateWidgetSettings.
Изменяет настройки окна чата сайта.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|text|False|string|Текст приветствия.<br/>Максимум 180 символов.<br/>|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## update
### Описание метода
Sites.update
Изменяет данные указанного сайта.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|prechats_chat|False|Array.<Prechat>|Массив объектов типа Prechat.<br/>Максимум 2 элемента.<br/>|
|is_lead|False|boolean|Включение/выключение функциональности генератора лидов.<br/>|
|is_call_label|False|boolean|Включение/выключение ярлыка звонков.<br/>DEPRECATED!<br/>|
|employee_ids|False|idlist|Список ID сотрудников через запятую.<br/>Если с сайтом связан, хотя бы один отдел, то этот параметр игнорируется.<br/>|
|url|False|string|Адрес сайта.<br/>|
|is_callback|False|boolean|Включение/выключение функциональности «Перезвоните мне».<br/>|
|is_complaint|False|boolean|Включение/выключение жалоб.<br/>|
|is_hidden_offline|False|boolean|Скрывать ярлык, если сотрудники офлайн.<br/>|
|complaint_email|False|email|Адрес электронной почты, на который будут отправляться нотификации о поступлении новой жалобы.<br/>|
|is_vote|False|boolean|Включение/выключение функциональности оценки чата посетителем.<br/>|
|is_mobile|False|boolean|Включение/выключение мобильного вида виджета.<br/>|
|is_site_prechats|False|boolean|Признак использования пречат-полей сайта.<br/>Если false, тоe. то будут использоваться пречаты из связей отделов с сайтом.<br/>|
|callback_url|False|string|Настройка Callback URL.<br/>|
|id|True|numeric|ID редактируемого сайта.<br/>|
|hold_rule_id|False|numeric|ID сценария удержания.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## WARNING: Type is DEPRECATED
## updateLeadFormSettings
### Описание метода
Sites.updateLeadFormSettings - DEPRECATED
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию. Все перенесено в updateWidgetSettings.
Обновляет настройки формы генератора лидов указанного сайта.
Параметры
Результат
Метод ничего не возвращает.
Пример запроса
curl https://api.livetex.ru/v2/sites/updateleadformsettings \
-H "Authorization: Bearer ACCESS_TOKEN" \
–d "id=12345" \
–d "photo_type=none" \
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|is_department|False|boolean|Включение/выключение выбора отдела в форме лида.<br/>|
|photo_custom|False|file|Загруженная картинка приветствия для photo_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с размерами 70x70px.<br/>Поле обязательно для photo_type = custom.<br/>|
|confirmation|False|string|Текст подтверждения по умолчанию.<br/>Максимум 180 символов.<br/>|
|color|False|string|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>Поле обязательно для color_type = preset.<br/>|
|color_type|False|string|Тип указания цветовой схемы.<br/>Возможные значения:<br/>preset – стандартная схема;<br/>custom – явное указание цветов.<br/>|
|welcome|False|string|Текст приветствия по умолчанию.<br/>Максимум 180 символов.<br/>|
|color_main|False|color|Основной цвет.<br/>Поле обязательно для color_type = custom.<br/>|
|id|True|numeric|ID сайта.<br/>|
|label|False|string|Надпись на ярлыке.<br/>Возможные значения:<br/>question – «Задать вопрос»;<br/>action – «Внимание! Акция»;<br/>gift – «Внимание! Подарок»;<br/>help – «Обратитесь за помощью»;<br/>best – «Посоветуем лучшее»;<br/>waiting – «Ждем Ваших вопросов»;<br/>choice – «Поможем с выбором»;<br/>consulting – «Получить консультацию».<br/>|
|banner_type|False|string|Тип баннера.<br/>Возможные значения:<br/>none – без баннера;<br/>default – стандартный баннер;<br/>custom – загружаемый баннер.<br/>|
|color_background|False|color|Цвет фона.<br/>Поле обязательно для color_type = custom.<br/>|
|banner_custom|False|file|Загруженный баннер для banner_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с шириной от 1 до 448 px и высотой 82 px.<br/>Поле обязательно для banner_type = custom.<br/>|
|banner_link|False|string|Ссылка, по которой будет направлен посетитель по клику на баннере.<br/>Поле обязательно для banner_type = custom.<br/>|
|welcome_mobile|False|string|Текст приветствия по умолчанию, который отобразится в мобильных браузерах.<br/>Максимум 180 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|lead_type|False|string|Запрашиваемые контактные данные.<br/>email -  запрашивается только email;<br/>phone – запрашивается только телефон;<br/>email_or_phone – запрашивается телефон или email;<br/>email_and_phone – запрашивается телефон и email.<br/>|
|photo_type|False|string|Тип картинки приветствия.<br/>Возможные значения:<br/>none – без картинки;<br/>default – стандартное фото;<br/>custom – загруженное фото.<br/>|
|confirmation_mobile|False|string|Текст подтверждения по умолчанию, который отобразится в мобильных браузерах.<br/>Максимум 180 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|required_fields|False|string|Обязательность полей при lead_type = email_and_phone.<br/>email – e-mail;<br/>phone – телефон;<br/>email_and_phone – email и телефон.<br/>Поле обязательно при lead_type = email_and_phone.<br/>|
|color_text|False|color|Цвет текста.<br/>Поле обязательно для color_type = custom.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## WARNING: Type is DEPRECATED
## showLeadFormSettings
### Описание метода
Sites.showLeadFormSettings - DEPRECATED
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию. Все перенесено в showWidgetSettings.
Возвращает настройки формы генератора лидов указанного сайта.
Параметры
Результат
Объект типа «LeadFormSettings».
Пример запроса
curl "https://api.livetex.ru/v2/sites/showleadformsettings?id=12345" \
-H "Authorization: Bearer ACCESS_TOKEN"
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## batchUpdateSiteXWidgetSettings
### Описание метода
Sites.batchUpdateSiteXWidgetSettings
Выполняет пакетное изменение настроек X-widget указанных сайтов.
Метод вызывает Sites.updateSiteXWidgetSettings для каждого ID сайта и передает указанные параметры.
Параметры
Результат
Массив объектов c ID-сайта, кодами и сообщениями об ошибке в порядке перечисления ID сайтов в запросе.
Пример
curl https://api.livetex.ru/v2/sites/batchupdatesitexwidgetsettings \
-H "Authorization: Bearer ACCESS_TOKEN" \
-d "ids=123,456,789" \
-d "is_active=false"

{
    "results": [
        {
            "id": "123",
            "code": 200,
            "message": ""
        },
        {
            "id": "456",
            "code": 200,
            "message": ""
        },
        {
            "id": "789",
            "code": 403,
            "message": "Forbidden"
        }
    ]
}
Уровень доступа для ролей

ВНИМАНИЕ!
При изменении конкретного сайта работает уровень доступа метода Sites.updateSiteXWidgetSettings в соответствующих условиях.


### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|interval_end|False|number|Конец интервала. Количество секунд от 00:00.<br/>|
|interval_begin|False|number|Начало интервала. Количество секунд от 00:00.<br/>|
|is_active|False|boolean|Включение/выключение мобильного вида виджета.<br/>|
|ids|True|idlist|Список, через запятую, ID сайтов.<br/>|
|days|False|Array.<numeric>|Массив дней недели, в которые необходимо показывать приглашение к заказу обратного звонка.<br/>Понедельник – 0, вторник - 1 и т.д.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## updateSiteXWidgetSettings
### Описание метода
Sites.updateSiteXWidgetSettings
Изменяет настройки продукта «X-widget» для указанного сайта.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|interval_end|False|number|Конец интервала. Количество секунд от 00:00.<br/>|
|interval_begin|False|number|Начало интервала. Количество секунд от 00:00.<br/>|
|is_active|False|boolean|Включение/выключение функции на сайте.<br/>|
|id|True|numeric|ID сайта.<br/>|
|days|False|Array.<numeric>|Массив дней недели, в которые необходимо показывать приглашение к заказу обратного звонка.<br/>Понедельник – 0, вторник - 1 и т.д.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## unbindAllDepartments
### Описание метода
Sites.unbindAllDepartments
Отвязывает все отделы от указанного сайта. При этом все сотрудники отделов напрямую связываются с сайтом.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## updateSiteCallSettings
### Описание метода
Sites.updateSiteCallSettings
Изменяет звонковые настройки сайта. 
Параметры
Результат
Метод ничего не возвращает.
Пример запроса
curl https://api.livetex.ru/v2/sites/updatecallsettings \
-H "Authorization: Bearer ACCESS_TOKEN" \
–d "id=12345" \
–d "background_type=none" \
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|visitor_callerid_type|False|string|Выбор номера телефона, отображаемого посетителю при исходящем звонке.<br/>Возможные значения:<br/>livetex – номер LiveTex (по умолчанию);<br/>employee – номер, указанный в поле phone_forward_number сотрудника;<br/>custom – номер, указанный в настройке visitor_callerid_custom.<br/>|
|visitor_callerid_custom|False|phone|Номер телефона, который будет отображаться посетителю при исходящем звонке при visitor_callerid_type=custom.<br/>Обязательно, если visitor_callerid_type=custom.<br/>|
|greeting_type|False|string|Типа мелодии приветствия.<br/>Приветствие проигрывается всем звонящим, перед соединением с оператором. Оператор отвечает только после того как мелодия полностью проиграется.<br/>Возможные значения:<br/>none – без приветствия,<br/>custom – пользовательское приветствие.<br/>|
|employee_callerid_type|False|string|Выбор номера телефона, отображаемого оператору при вызове X-widget.<br/>Возможные значения:<br/>livetex – номер LiveTex (по умолчанию);<br/>visitor – номер, указанный посетителем при заказе звонка.<br/>|
|background_type|False|string|Тип фоновой мелодии.<br/>Фоновая мелодия проигрывается во время ожидания, пока кто-нибудь из операторов не ответит на звонок.<br/>Возможные значения:<br/>none – без приветствия,<br/>default – стандартная фоновая мелодия,<br/>custom – пользовательская фоновая мелодия.<br/>|
|background_custom|False|file|Пользовательская фоновая мелодия.<br/>Обязательно, если background_type = custom.<br/>Поддерживаются форматы MP3, OGG.<br/>Размер загружаемого файла должен быть не более 8МB.<br/>|
|greeting_custom|False|file|Пользовательское приветствие.<br/>Обязательно, если greeting_type = custom.<br/>Поддерживаются форматы MP3, OGG.<br/>Размер загружаемого файла должен быть не более 8МB.<br/>|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## WARNING: Type is DEPRECATED
## showCallLabelSettings
### Описание метода
Sites.showCallLabelSettings - DEPRECATED
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию.
Возвращает настройки ярлыка звонков указанного сайта.
Параметры
Результат
Объект типа «CallLabelSettings».
Пример запроса
curl https://api.livetex.ru/v2/sites/showcalllabelsettings?id=12345 \
-H "Authorization: Bearer ACCESS_TOKEN"
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner## delete
### Описание метода
Sites.delete
Удаляет указанный сайт.
ВНИМАНИЕ!
При удалении сайта удаляются все связи с отделами. При этом также удаляются отделы, оставшиеся без сайтов.
При удалении сайта удаляются все его связи с объектами других сущностей, за исключением чатов, звонков и лидов и связей с сотрудниками в поле managed_sites.
Параметры
Результат
Метод ничего не возвращает.
Уровень доступа для ролей

### Поля
| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|id|True|numeric|ID сайта.<br/>|
### Доступы к методу
| Имя роли | доступ | Комментарий |
|---|---|---|
|admin|manager|chief|chief_partner|operator|admin_partner