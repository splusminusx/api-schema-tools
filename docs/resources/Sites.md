
# Sites

## Описание ресурса

# Методы

## updateOfflineMailSettings

### Описание метода
Изменяет настройки офлайн почты.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*from_name*|False|[string](/docs/types/string.md)|Отправитель.<br/>Максимум 60 символов.<br/>|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Включение/выключение использования внешнего почтового ящика.<br/>Если функция выключена, то письма будут отправляться через сервера LiveTex c системными значениями отправителя, темы и подписи.<br/>|
|*signature*|False|[string](/docs/types/string.md)|Подпись.<br/>Максимум 60 символов.<br/>|
|*mailbox_id*|False|[numeric](/docs/types/numeric.md)|ID почтового ящика.<br/>Если указано null, то для отправки почты будут использоваться сервера LiveTex.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|*subject*|False|[string](/docs/types/string.md)|Тема письма.<br/>Максимум 60 символов.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## showSiteCallSettings

### Описание метода
Возвращает настройки звонков указанного сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
[SiteCallSettings](/docs/types/SiteCallSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## show

### Описание метода
Возвращает данные указанного сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
[Site](/docs/types/Site.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|full||
|*admin_partner*|full||

## list

### Описание метода
Возвращает список сайтов.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*q*|False|[string](/docs/types/string.md)|Критерий поиска.<br/>Доступные поля:<br/>ids – idlist, список ID сайтов.<br/>url – string, подстрока в адресе сайта.<br/>is_managed – boolean, признак своего сайта.<br/>|
|*fields*|False|[string](/docs/types/string.md)|Список через запятую возвращаемых полей.<br/>|
|*limit*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 50.<br/>|
|*sort*|False|[string](/docs/types/string.md)|Сортировка результатов.<br/>Возможные значения:<br/>url:a – по умолчанию;<br/>updated_at:a, updated_at:d;<br/>|
|*offset*|False|[numeric](/docs/types/numeric.md)|По умолчанию – 0.<br/>|

### Результат
Array.<[Site](/docs/types/Site.md)>
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|full||
|*chief*|full||
|*chief_partner*|full||
|*operator*|full||
|*admin_partner*|full||

## WARNING: DEPRECATED

## updateChatFormSettings
## WARNING: DEPRECATED

### Описание метода
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию. Все перенесено в updateWidgetSettings.<br/>Изменяет настройки окна чата сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*offset_value*|False|[numeric](/docs/types/numeric.md)|Значение отступа.<br/>Целое число в диапазоне:<br/>от 0 до 100 для offset_type = percent;<br/>от 0 до 2000 для offset_type = pixel.<br/>|
|*color*|False|[string](/docs/types/string.md)|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>Поле обязательно для color_type = preset.<br/>|
|*photo_size*|False|[string](/docs/types/string.md)|Размер фотографии сотрудника.<br/>Возможные значения:<br/>small – маленькая, 60x70 пикселей;<br/>large – большая, 100x116 пикселей.<br/>|
|*color_text*|False|[color](/docs/types/color.md)|Цвет текста.<br/>Поле обязательно для color_type = custom.<br/>|
|*color_main*|False|[color](/docs/types/color.md)|Основной цвет.<br/>Поле обязательно для color_type = custom.<br/>|
|*is_hidden_offline*|False|[boolean](/docs/types/boolean.md)|Скрывать ярлык, если сотрудники офлайн.<br/>|
|*offset_type*|False|[string](/docs/types/string.md)|Тип отступа.<br/>Возможные значения:<br/>pixel – в пикселах;<br/>percent – в процентах.<br/>|
|*banner_type*|False|[string](/docs/types/string.md)|Тип баннера.<br/>Возможные значения:<br/>none – без баннера;<br/>default – стандартный баннер;<br/>custom – загружаемый баннер.<br/>|
|*color_background*|False|[color](/docs/types/color.md)|Цвет фона.<br/>Поле обязательно для color_type = custom.<br/>|
|*banner_custom*|False|[file](/docs/types/file.md)|Загруженная баннер для banner_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с шириной от 1 до 448 px и высотой 82 px.<br/>Поле обязательно для banner_type = custom.<br/>|
|*banner_link*|False|[string](/docs/types/string.md)|Ссылка с баннера.<br/>Поле обязательно для banner_type = custom.<br/>|
|*position*|False|[string](/docs/types/string.md)|Положение ярлыка.<br/>Возможные значения:<br/>top – сверху;<br/>right – справа;<br/>bottom – снизу;<br/>left – слева.<br/>|
|*is_label_visible*|False|[boolean](/docs/types/boolean.md)|Признак отображения ярлыка.<br/>По умолчанию – true.<br/>Если false, ярлык не будет показываться посетителю, даже при наличии доступных операторов.<br/>Это признак автоматически устанавливается в true и не может быть изменен, если подключена опция генератора лидов или для сайта включено встроенное окно чата (site.is_embedded_chat == true).<br/>Признак is_label_visible связан с полем size. При переключении из false в true поле size устанавливается в значение по умолчанию.<br/>|
|*logo_type*|False|[string](/docs/types/string.md)|Тип логотипа LiveTex.<br/>Возможные значения:<br/>animated – анимированный;<br/>static – статический.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|*background_custom*|False|[file](/docs/types/file.md)|Загруженный фон для background_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с размерами 448x605px.<br/>Поле обязательно для background_type = custom.<br/>|
|*background_typе*|False|[string](/docs/types/string.md)|Тип фона.<br/>Возможные значения:<br/>none – без фона;<br/>default – стандартный фон;<br/>custom – загружаемый фон.<br/>|
|*color_type*|False|[string](/docs/types/string.md)|Тип указания цветовой схемы.<br/>Возможные значения:<br/>preset – стандартная схема;<br/>custom – явное указание цветов.<br/>|
|*size*|False|[string](/docs/types/string.md)|Размер ярлыка.<br/>Возможные значения:<br/>small – маленький, 24x106 пикселей;<br/>large – большой, 40x178 пикселей (по умолчанию).<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## showSiteChatSettings

### Описание метода
Возвращает настройки чата для указанного сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
[SiteChatSettings](/docs/types/SiteChatSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## WARNING: DEPRECATED

## showChatWelcomeSettings
## WARNING: DEPRECATED

### Описание метода
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию. Все перенесено в showWidgetSettings.<br/>Возвращает настройки окна приветствия указанного сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
[ChatWelcomeSettings](/docs/types/ChatWelcomeSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## batchUpdate

### Описание метода
Выполняет пакетное изменение данных указанных сайтов.<br/>Метод вызывает Sites.update для каждого ID сайта и передает указанные параметры.<br/>Пример<br/>curl https://api.livetex.ru/v2/sites/batchupdate \<br/>-H "Authorization: Bearer ACCESS_TOKEN" \<br/>-d "ids=123,456,789" \<br/>-d "is_callback=false"<br/><br/>{<br/>    "results": [<br/>        {<br/>            "id": "123",<br/>            "code": 200,<br/>            "message": ""<br/>        },<br/>        {<br/>            "id": "456",<br/>            "code": 200,<br/>            "message": ""<br/>        },<br/>        {<br/>            "id": "789",<br/>            "code": 403,<br/>            "message": "Forbidden"<br/>        }<br/>    ]<br/>}<br/><br/><br/>ВНИМАНИЕ!<br/>При изменении конкретного сайта работает уровень доступа метода Sites.update в соответствующих условиях.<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_complaint*|False|[boolean](/docs/types/boolean.md)|Включение/выключение жалоб.<br/>|
|*is_callback*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности «Перезвоните мне».<br/>|
|*ids*|True|[idlist](/docs/types/idlist.md)|Список, через запятую, ID сайтов.<br/>|
|*complaint_email*|False|[string](/docs/types/string.md)|Адрес электронной почты, на который будут отправляться нотификации о поступлении новой жалобы.<br/>|
|*is_vote*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности оценки чата посетителем.<br/>|
|*is_mobile*|False|[boolean](/docs/types/boolean.md)|Включение/выключение мобильного вида виджета.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только для своих сайтов.|
|*chief*|managed|Только для своих сайтов.|
|*chief_partner*|managed|Только для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## WARNING: DEPRECATED

## showOfflineFormSettings
## WARNING: DEPRECATED

### Описание метода
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию.<br/>Возвращает настройки формы офлайн-сообщения указанного сайта.<br/>Пример запроса<br/>curl https://api.livetex.ru/v2/sites/showofflineformsettings?id=12345 \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
[OfflineFormSettings](/docs/types/OfflineFormSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## showOfflineMailSettings

### Описание метода
Возвращает настройки офлайн почты.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
[OfflineMailSettings](/docs/types/OfflineMailSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## showSiteWidgetSettings

### Описание метода
Возвращает настройки виджета для указанного сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
[SiteWidgetSettings](/docs/types/SiteWidgetSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## add

### Описание метода
Создает новый сайт.<br/>ВНИМАНИЕ!<br/>Новый сайт автоматически добавляется в поле managed_sites всем сотрудникам с ролью, имеющей is_full_by_default = true.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*prechats_chat*|False|Array.<[Prechat](/docs/types/Prechat.md)>|Массив объектов типа Prechat.<br/>Максимум 2 элемента.<br/>|
|*is_lead*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности генератора лидов.<br/>По умолчанию – true.<br/>|
|*is_call_label*|False|[boolean](/docs/types/boolean.md)|Включение/выключение ярлыка звонков.<br/>DEPRECATED!<br/>|
|*employee_ids*|False|[idlist](/docs/types/idlist.md)|Список ID сотрудников через запятую.<br/>|
|*url*|True|[string](/docs/types/string.md)|Адрес сайта.<br/>Например: www.mysite.ru<br/>|
|*is_callback*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности «Перезвоните мне».<br/>По умолчанию – true.<br/>|
|*is_complaint*|False|[boolean](/docs/types/boolean.md)|Включение/выключение жалоб.<br/>По умолчанию – false.<br/>|
|*is_hidden_offline*|False|[boolean](/docs/types/boolean.md)|Скрывать ярлык, если сотрудники офлайн.<br/>По умолчанию – false.<br/>|
|*complaint_email*|False|[email](/docs/types/email.md)|Адрес электронной почты, на который будут отправляться нотификации о поступлении новой жалобы.<br/>Обязателен, если указано is_complaint = true.<br/>|
|*is_vote*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности оценки чата посетителем.<br/>По умолчанию – true.<br/>|
|*is_mobile*|False|[boolean](/docs/types/boolean.md)|Включение/выключение мобильного вида виджета.<br/>|
|*is_site_prechats*|False|[boolean](/docs/types/boolean.md)|Признак использования пречат-полей сайта.<br/>Если false, то будут использоваться пречаты из связей отделов с сайтом.<br/>По умолчанию – true.<br/>|
|*callback_url*|False|[string](/docs/types/string.md)|Настройка Callback URL.<br/>|
|*hold_rule_id*|False|[numeric](/docs/types/numeric.md)|ID сценария удержания.<br/>|

### Результат
[Site](/docs/types/Site.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|full||
|*chief_partner*|full||
|*operator*|none||
|*admin_partner*|full||

## WARNING: DEPRECATED

## showChatFormSettings
## WARNING: DEPRECATED

### Описание метода
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию. Все перенесено в showWidgetSettings.<br/>Возвращает настройки окна чата указанного сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
[ChatFormSettings](/docs/types/ChatFormSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## updateSiteChatSettings

### Описание метода
Изменяет настройки чата для указанного сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*offline_contacts*|False|[string](/docs/types/string.md)|Запрашиваемые контактные данные в офлайн-режиме.<br/>Возможные значения:<br/>email -  запрашивается только email;<br/>phone – запрашивается только телефон;<br/>email_or_phone – запрашивается телефон или email;<br/>email_and_phone – запрашивается телефон и email.<br/>|
|*offline_confirmation*|False|[string](/docs/types/string.md)|Текст подтверждения в режиме офлайн. Отображается после успешной отправки запроса.<br/>Максимум 180 символов.<br/>|
|*offline_contacts_required*|False|[string](/docs/types/string.md)|Обязательность полей при offline_contacts=email_and_phone.<br/>Возможные значения:<br/>email – e-mail;<br/>phone – телефон;<br/>email_and_phone – email и телефон.<br/>|
|*offline_welcome*|False|[string](/docs/types/string.md)|Текст приветствия в режиме офлайн.<br/>Максимум 180 символов.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|*online_welcome*|False|[string](/docs/types/string.md)|Текст приветствия в режиме онлайн.<br/>Максимум 180 символов.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## WARNING: DEPRECATED

## updateCallLabelSettings
## WARNING: DEPRECATED

### Описание метода
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию.<br/>Изменяет звонковые настройки сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_visible*|False|[boolean](/docs/types/boolean.md)|Показывать ярлык.<br/>|
|*offset_value*|False|[numeric](/docs/types/numeric.md)|Значение отступа.<br/>Целое число в диапазоне:<br/>от 0 до 100 для offset_type = percent;<br/>от 0 до 2000 для offset_type = pixel.<br/>|
|*color*|False|[string](/docs/types/string.md)|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>|
|*offset_type*|False|[string](/docs/types/string.md)|Тип отступа.<br/>Возможные значения:<br/>pixel – в пикселах;<br/>percent – в процентах.<br/>|
|*position*|False|[string](/docs/types/string.md)|Положение ярлыка.<br/>Возможные значения:<br/>top – сверху;<br/>right – справа;<br/>bottom – снизу;<br/>left – слева.<br/>|
|*size*|False|[string](/docs/types/string.md)|Размер ярлыка.<br/>Возможные значения:<br/>small – маленький, 23x118 пикселей;<br/>large – большой, 38x174 пикселей.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|*department_id*|False|[numeric](/docs/types/numeric.md)|ID отдела.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## updateSiteWidgetSettings

### Описание метода
Изменяет настройки виджета для указанного сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_department*|False|[boolean](/docs/types/boolean.md)|Включение/выключение выбора отдела для офлайн режима.<br/>При создании сайта устанавливается в false.<br/>|
|*offset_value*|False|[numeric](/docs/types/numeric.md)|Значение отступа в процентах.<br/>Число в диапазоне от 0 до 100. Может быть дробным.<br/>|
|*label_text_offline*|False|[string](/docs/types/string.md)|Текст на ярлыке, когда доступных операторов нет.<br/>|
|*color*|False|[string](/docs/types/string.md)|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>Поле обязательно для color_type = preset.<br/>|
|*color_type*|False|[string](/docs/types/string.md)|Тип указания цветовой схемы.<br/>Возможные значения:<br/>preset – стандартная схема;<br/>custom – явное указание цветов.<br/>|
|*label_text_online*|False|[string](/docs/types/string.md)|Текст на ярлыке, когда есть доступные операторы.<br/>|
|*color_custom*|False|[color](/docs/types/color.md)|Цвет.<br/>Поле обязательно для color_type = custom.<br/>|
|*is_embedded*|False|[boolean](/docs/types/boolean.md)|Включение/выключение встроенного окна чата.<br/>Если выключено, то будет использоваться внешнее окно чата.<br/>|
|*banner_custom*|False|[file](/docs/types/file.md)|Загруженная баннер для banner_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с шириной от 1 до 448 px и высотой 82 px.<br/>Максимальный размер файла – 2 MB.<br/>Поле обязательно для banner_type = custom.<br/>Актуально только для внешнего окна.<br/>|
|*banner_type*|False|[string](/docs/types/string.md)|Тип баннера.<br/>Возможные значения:<br/>none – без баннера;<br/>default – стандартный баннер;<br/>custom – загружаемый баннер.<br/>Актуально только для внешнего окна.<br/>|
|*banner_link*|False|[string](/docs/types/string.md)|Ссылка с баннера.<br/>Поле обязательно для banner_type = custom.<br/>Актуально только для внешнего окна.<br/>|
|*position*|False|[string](/docs/types/string.md)|Положение ярлыка.<br/>Возможные значения:<br/>right – справа;<br/>bottom – снизу;<br/>left – слева.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|*color_text*|False|[string](/docs/types/string.md)|Цвет текста.<br/>Возможные значения:<br/>light – светлый;<br/>dark – темный;<br/>auto – значение выбирается автоматически.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## showSiteXWidgetSettings

### Описание метода
Возвращает настройки продукта «X-widget» для указанного сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
[SiteXWidgetSettings](/docs/types/SiteXWidgetSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## WARNING: DEPRECATED

## updateOfflineFormSettings
## WARNING: DEPRECATED

### Описание метода
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию.<br/>Обновляет настройки офлайн-формы.<br/>Пример запроса<br/>curl https://api.livetex.ru/v2/sites/updateofflineformsettings \<br/>-H "Authorization: Bearer ACCESS_TOKEN" \<br/>–d "id=12345" \<br/>–d "banner_type=none"<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*confirmation*|False|[string](/docs/types/string.md)|Текст подтверждения по умолчанию.<br/>Максимум 180 символов.<br/>|
|*contacts*|False|[string](/docs/types/string.md)|Запрашиваемые контактные данные.<br/>email -  запрашивается только email;<br/>phone – запрашивается только телефон;<br/>email_or_phone – запрашивается телефон или email;<br/>email_and_phone – запрашивается телефон и email.<br/>|
|*color*|False|[string](/docs/types/string.md)|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>|
|*required_fields*|False|[string](/docs/types/string.md)|Обязательность полей при contacts = email_and_phone.<br/>email – e-mail;<br/>phone – телефон;<br/>email_and_phone – email и телефон.<br/>Это поле обязательно при contacts = email_and_phone.<br/>|
|*welcome*|False|[string](/docs/types/string.md)|Текст приветствия по умолчанию.<br/>Максимум 180 символов.<br/>|
|*banner_custom*|False|[file](/docs/types/file.md)|Загруженная баннер для banner_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с шириной от 1 до 448 px и высотой 82 px.<br/>Поле обязательно для banner_type = custom.<br/>|
|*background_custom*|False|[file](/docs/types/file.md)|Загруженный фон для background_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с размерами 448x605px.<br/>Поле обязательно для background_type = custom.<br/>|
|*banner_type*|False|[string](/docs/types/string.md)|Тип баннера.<br/>Возможные значения:<br/>none – без баннера;<br/>default – стандартный баннер;<br/>custom – загружаемый баннер.<br/>|
|*banner_link*|False|[string](/docs/types/string.md)|Ссылка с баннера.<br/>Поле обязательно для banner_type = custom.<br/>|
|*confirmation_mobile*|False|[string](/docs/types/string.md)|Текст подтверждения по умолчанию, который отобразится в мобильных браузерах.<br/>Максимум 180 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|*background_typе*|False|[string](/docs/types/string.md)|Тип фона.<br/>Возможные значения:<br/>none – без фона;<br/>default – стандартный фон;<br/>custom – загружаемый фон.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|*welcome_mobile*|False|[string](/docs/types/string.md)|Текст приветствия по умолчанию, который отобразится в мобильных браузерах.<br/>Максимум 180 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## WARNING: DEPRECATED

## updateChatWelcomeSettings
## WARNING: DEPRECATED

### Описание метода
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию. Все перенесено в updateWidgetSettings.<br/>Изменяет настройки окна чата сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*text*|False|[string](/docs/types/string.md)|Текст приветствия.<br/>Максимум 180 символов.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## update

### Описание метода
Изменяет данные указанного сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*prechats_chat*|False|Array.<[Prechat](/docs/types/Prechat.md)>|Массив объектов типа Prechat.<br/>Максимум 2 элемента.<br/>|
|*is_lead*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности генератора лидов.<br/>|
|*is_call_label*|False|[boolean](/docs/types/boolean.md)|Включение/выключение ярлыка звонков.<br/>DEPRECATED!<br/>|
|*employee_ids*|False|[idlist](/docs/types/idlist.md)|Список ID сотрудников через запятую.<br/>Если с сайтом связан, хотя бы один отдел, то этот параметр игнорируется.<br/>|
|*url*|False|[string](/docs/types/string.md)|Адрес сайта.<br/>|
|*is_callback*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности «Перезвоните мне».<br/>|
|*is_complaint*|False|[boolean](/docs/types/boolean.md)|Включение/выключение жалоб.<br/>|
|*is_hidden_offline*|False|[boolean](/docs/types/boolean.md)|Скрывать ярлык, если сотрудники офлайн.<br/>|
|*complaint_email*|False|[email](/docs/types/email.md)|Адрес электронной почты, на который будут отправляться нотификации о поступлении новой жалобы.<br/>|
|*is_vote*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функциональности оценки чата посетителем.<br/>|
|*is_mobile*|False|[boolean](/docs/types/boolean.md)|Включение/выключение мобильного вида виджета.<br/>|
|*is_site_prechats*|False|[boolean](/docs/types/boolean.md)|Признак использования пречат-полей сайта.<br/>Если false, тоe. то будут использоваться пречаты из связей отделов с сайтом.<br/>|
|*callback_url*|False|[string](/docs/types/string.md)|Настройка Callback URL.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID редактируемого сайта.<br/>|
|*hold_rule_id*|False|[numeric](/docs/types/numeric.md)|ID сценария удержания.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только для своих сайтов.|
|*chief*|managed|Только для своих сайтов.|
|*chief_partner*|managed|Только для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## WARNING: DEPRECATED

## updateLeadFormSettings
## WARNING: DEPRECATED

### Описание метода
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию. Все перенесено в updateWidgetSettings.<br/>Обновляет настройки формы генератора лидов указанного сайта.<br/>Пример запроса<br/>curl https://api.livetex.ru/v2/sites/updateleadformsettings \<br/>-H "Authorization: Bearer ACCESS_TOKEN" \<br/>–d "id=12345" \<br/>–d "photo_type=none" \<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*is_department*|False|[boolean](/docs/types/boolean.md)|Включение/выключение выбора отдела в форме лида.<br/>|
|*photo_custom*|False|[file](/docs/types/file.md)|Загруженная картинка приветствия для photo_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с размерами 70x70px.<br/>Поле обязательно для photo_type = custom.<br/>|
|*confirmation*|False|[string](/docs/types/string.md)|Текст подтверждения по умолчанию.<br/>Максимум 180 символов.<br/>|
|*color*|False|[string](/docs/types/string.md)|Цветовая схема.<br/>Возможные значения:<br/>green – зеленая;<br/>orange – оранжевая;<br/>blue – синяя;<br/>red – красная;<br/>purple – фиолетовая;<br/>gray – серая;<br/>rose – розовая;<br/>black – черная;<br/>yellow – желтая;<br/>white – белая.<br/>Поле обязательно для color_type = preset.<br/>|
|*color_type*|False|[string](/docs/types/string.md)|Тип указания цветовой схемы.<br/>Возможные значения:<br/>preset – стандартная схема;<br/>custom – явное указание цветов.<br/>|
|*welcome*|False|[string](/docs/types/string.md)|Текст приветствия по умолчанию.<br/>Максимум 180 символов.<br/>|
|*color_main*|False|[color](/docs/types/color.md)|Основной цвет.<br/>Поле обязательно для color_type = custom.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|*label*|False|[string](/docs/types/string.md)|Надпись на ярлыке.<br/>Возможные значения:<br/>question – «Задать вопрос»;<br/>action – «Внимание! Акция»;<br/>gift – «Внимание! Подарок»;<br/>help – «Обратитесь за помощью»;<br/>best – «Посоветуем лучшее»;<br/>waiting – «Ждем Ваших вопросов»;<br/>choice – «Поможем с выбором»;<br/>consulting – «Получить консультацию».<br/>|
|*banner_type*|False|[string](/docs/types/string.md)|Тип баннера.<br/>Возможные значения:<br/>none – без баннера;<br/>default – стандартный баннер;<br/>custom – загружаемый баннер.<br/>|
|*color_background*|False|[color](/docs/types/color.md)|Цвет фона.<br/>Поле обязательно для color_type = custom.<br/>|
|*banner_custom*|False|[file](/docs/types/file.md)|Загруженный баннер для banner_type = custom.<br/>Изображение в формате JPEG, GIF или PNG с шириной от 1 до 448 px и высотой 82 px.<br/>Поле обязательно для banner_type = custom.<br/>|
|*banner_link*|False|[string](/docs/types/string.md)|Ссылка, по которой будет направлен посетитель по клику на баннере.<br/>Поле обязательно для banner_type = custom.<br/>|
|*welcome_mobile*|False|[string](/docs/types/string.md)|Текст приветствия по умолчанию, который отобразится в мобильных браузерах.<br/>Максимум 180 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|*lead_type*|False|[string](/docs/types/string.md)|Запрашиваемые контактные данные.<br/>email -  запрашивается только email;<br/>phone – запрашивается только телефон;<br/>email_or_phone – запрашивается телефон или email;<br/>email_and_phone – запрашивается телефон и email.<br/>|
|*photo_type*|False|[string](/docs/types/string.md)|Тип картинки приветствия.<br/>Возможные значения:<br/>none – без картинки;<br/>default – стандартное фото;<br/>custom – загруженное фото.<br/>|
|*confirmation_mobile*|False|[string](/docs/types/string.md)|Текст подтверждения по умолчанию, который отобразится в мобильных браузерах.<br/>Максимум 180 символов.<br/>ВНИМАНИЕ! В данный момент это поле не используется.<br/>|
|*required_fields*|False|[string](/docs/types/string.md)|Обязательность полей при lead_type = email_and_phone.<br/>email – e-mail;<br/>phone – телефон;<br/>email_and_phone – email и телефон.<br/>Поле обязательно при lead_type = email_and_phone.<br/>|
|*color_text*|False|[color](/docs/types/color.md)|Цвет текста.<br/>Поле обязательно для color_type = custom.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## WARNING: DEPRECATED

## showLeadFormSettings
## WARNING: DEPRECATED

### Описание метода
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию. Все перенесено в showWidgetSettings.<br/>Возвращает настройки формы генератора лидов указанного сайта.<br/>Пример запроса<br/>curl "https://api.livetex.ru/v2/sites/showleadformsettings?id=12345" \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
[LeadFormSettings](/docs/types/LeadFormSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## batchUpdateSiteXWidgetSettings

### Описание метода
Выполняет пакетное изменение настроек X-widget указанных сайтов.<br/>Метод вызывает Sites.updateSiteXWidgetSettings для каждого ID сайта и передает указанные параметры.<br/>Пример<br/>curl https://api.livetex.ru/v2/sites/batchupdatesitexwidgetsettings \<br/>-H "Authorization: Bearer ACCESS_TOKEN" \<br/>-d "ids=123,456,789" \<br/>-d "is_active=false"<br/><br/>{<br/>    "results": [<br/>        {<br/>            "id": "123",<br/>            "code": 200,<br/>            "message": ""<br/>        },<br/>        {<br/>            "id": "456",<br/>            "code": 200,<br/>            "message": ""<br/>        },<br/>        {<br/>            "id": "789",<br/>            "code": 403,<br/>            "message": "Forbidden"<br/>        }<br/>    ]<br/>}<br/><br/>ВНИМАНИЕ!<br/>При изменении конкретного сайта работает уровень доступа метода Sites.updateSiteXWidgetSettings в соответствующих условиях.<br/><br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*interval_end*|False|[number](/docs/types/number.md)|Конец интервала. Количество секунд от 00:00.<br/>|
|*interval_begin*|False|[number](/docs/types/number.md)|Начало интервала. Количество секунд от 00:00.<br/>|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Включение/выключение мобильного вида виджета.<br/>|
|*ids*|True|[idlist](/docs/types/idlist.md)|Список, через запятую, ID сайтов.<br/>|
|*days*|False|Array.<[numeric](/docs/types/numeric.md)>|Массив дней недели, в которые необходимо показывать приглашение к заказу обратного звонка.<br/>Понедельник – 0, вторник - 1 и т.д.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только для своих сайтов.|
|*chief*|managed|Только для своих сайтов.|
|*chief_partner*|managed|Только для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## updateSiteXWidgetSettings

### Описание метода
Изменяет настройки продукта «X-widget» для указанного сайта.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*interval_end*|False|[number](/docs/types/number.md)|Конец интервала. Количество секунд от 00:00.<br/>|
|*interval_begin*|False|[number](/docs/types/number.md)|Начало интервала. Количество секунд от 00:00.<br/>|
|*is_active*|False|[boolean](/docs/types/boolean.md)|Включение/выключение функции на сайте.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|
|*days*|False|Array.<[numeric](/docs/types/numeric.md)>|Массив дней недели, в которые необходимо показывать приглашение к заказу обратного звонка.<br/>Понедельник – 0, вторник - 1 и т.д.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## unbindAllDepartments

### Описание метода
Отвязывает все отделы от указанного сайта. При этом все сотрудники отделов напрямую связываются с сайтом.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Только для своих сайтов.|
|*chief*|managed|Только для своих сайтов.|
|*chief_partner*|managed|Только для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## updateSiteCallSettings

### Описание метода
Изменяет звонковые настройки сайта. <br/>Пример запроса<br/>curl https://api.livetex.ru/v2/sites/updatecallsettings \<br/>-H "Authorization: Bearer ACCESS_TOKEN" \<br/>–d "id=12345" \<br/>–d "background_type=none" \<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*visitor_callerid_type*|False|[string](/docs/types/string.md)|Выбор номера телефона, отображаемого посетителю при исходящем звонке.<br/>Возможные значения:<br/>livetex – номер LiveTex (по умолчанию);<br/>employee – номер, указанный в поле phone_forward_number сотрудника;<br/>custom – номер, указанный в настройке visitor_callerid_custom.<br/>|
|*visitor_callerid_custom*|False|[phone](/docs/types/phone.md)|Номер телефона, который будет отображаться посетителю при исходящем звонке при visitor_callerid_type=custom.<br/>Обязательно, если visitor_callerid_type=custom.<br/>|
|*greeting_type*|False|[string](/docs/types/string.md)|Типа мелодии приветствия.<br/>Приветствие проигрывается всем звонящим, перед соединением с оператором. Оператор отвечает только после того как мелодия полностью проиграется.<br/>Возможные значения:<br/>none – без приветствия,<br/>custom – пользовательское приветствие.<br/>|
|*employee_callerid_type*|False|[string](/docs/types/string.md)|Выбор номера телефона, отображаемого оператору при вызове X-widget.<br/>Возможные значения:<br/>livetex – номер LiveTex (по умолчанию);<br/>visitor – номер, указанный посетителем при заказе звонка.<br/>|
|*background_type*|False|[string](/docs/types/string.md)|Тип фоновой мелодии.<br/>Фоновая мелодия проигрывается во время ожидания, пока кто-нибудь из операторов не ответит на звонок.<br/>Возможные значения:<br/>none – без приветствия,<br/>default – стандартная фоновая мелодия,<br/>custom – пользовательская фоновая мелодия.<br/>|
|*background_custom*|False|[file](/docs/types/file.md)|Пользовательская фоновая мелодия.<br/>Обязательно, если background_type = custom.<br/>Поддерживаются форматы MP3, OGG.<br/>Размер загружаемого файла должен быть не более 8МB.<br/>|
|*greeting_custom*|False|[file](/docs/types/file.md)|Пользовательское приветствие.<br/>Обязательно, если greeting_type = custom.<br/>Поддерживаются форматы MP3, OGG.<br/>Размер загружаемого файла должен быть не более 8МB.<br/>|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## WARNING: DEPRECATED

## showCallLabelSettings
## WARNING: DEPRECATED

### Описание метода
ВНИМАНИЕ! Метод является устаревшим и не рекомендуется к использованию.<br/>Возвращает настройки ярлыка звонков указанного сайта.<br/>Пример запроса<br/>curl https://api.livetex.ru/v2/sites/showcalllabelsettings?id=12345 \<br/>-H "Authorization: Bearer ACCESS_TOKEN"<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
[CallLabelSettings](/docs/types/CallLabelSettings.md)
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|managed|Для своих сайтов.|
|*chief*|managed|Для своих сайтов.|
|*chief_partner*|managed|Для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||

## delete

### Описание метода
Удаляет указанный сайт.<br/>ВНИМАНИЕ!<br/>При удалении сайта удаляются все связи с отделами. При этом также удаляются отделы, оставшиеся без сайтов.<br/>При удалении сайта удаляются все его связи с объектами других сущностей, за исключением чатов, звонков и лидов и связей с сотрудниками в поле managed_sites.<br/><br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*id*|True|[numeric](/docs/types/numeric.md)|ID сайта.<br/>|

### Результат
None
### Доступы к методу

| Имя роли | доступ | Комментарий |
|---|---|---|
|*admin*|full||
|*manager*|none||
|*chief*|managed|Только для своих сайтов.|
|*chief_partner*|managed|Только для своих сайтов.|
|*operator*|none||
|*admin_partner*|full||
