
## Site

### Описание типа
Site
Сайт.
Таблица 79. Поля сайта

Контроллер: Sites.

### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|department_site_bindings|False|Array.<DepartmentSiteBinding>|Список связей сайта с отделами.<br/>|
|is_lead|True|boolean|Включение/выключение функциональности генератора лидов.<br/>|
|updated_at|True|datetime|Дата последнего обновления.<br/>|
|offline_form_settings|False|OfflineFormSettings|Настройки офлайн формы.<br/>DEPRECATED!<br/>|
|x_widget_settings|True|SiteXWidgetSettings|Настройки продукта «X-widget».<br/>|
|is_site_prechats|True|boolean|Признак использования пречат-полей сайта.<br/>Если false, то будут использоваться пречаты из связей отделов с сайтом.<br/>|
|id|True|numeric|ID сайта.<br/>|
|call_label_settings|True|CallLabelSettings|Настройки ярлыка звонка.<br/>DEPRECATED!<br/>|
|prechats_chat|False|Array.<Prechat>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|is_comlaint|True|boolean|Включение/выключение жалоб.<br/>|
|hold_rule|False|HoldRule|Сценарий удержания.<br/>|
|is_mobile|True|boolean|Включение/выключение мобильного вида виджета.<br/>|
|widget_settings|True|SiteWidgetSettings|Настройки виджета.<br/>|
|prechats_lead|False|Array.<Prechat>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|complaint_email|False|email|Адрес электронной почты, на который будут отправляться нотификации о поступлении новой жалобы.<br/>|
|is_hidden_offline|True|boolean|Скрывать ярлык, если сотрудники офлайн.<br/>|
|is_vote|True|boolean|Включение/выключение функциональности оценки чата посетителем.<br/>|
|chat_welcome_settings|True|ChatWelcomeSettings|Настройки окна приветствия.<br/>DEPRECATED!<br/>|
|call_settings|True|SiteCallSettings|Звонковые настройки сайта.<br/>|
|chat_form_settings|True|ChatFormSettings|Настройки ярлыка и окна чата.<br/>DEPRECATED!<br/>|
|is_deleted|True|boolean|Признак удаленного объекта.<br/>|
|url|True|string|Адрес сайта.<br/>|
|is_callback|True|boolean|Включение/выключение функциональности «Перезвоните мне».<br/>|
|employees|False|Array.<Employee>|Список сотрудников, связанных с данным сайтом.<br/>|
|lead_form_settings|False|LeadFormSettings|Настройки формы генератора лидов.<br/>DEPRECATED!<br/>|
|is_managed|True|boolean|True, если сайт входит в число своих сайтов сотрудника, вызывающего метод.<br/>Это признак доступен только для чтения.<br/>|
|is_custom_buttons|True|boolean|Признак заказного дизайна кнопок.<br/>Если true, то изменение некоторых визуальных настроек кнопок чата и звонка может не иметь должного результата, поскольку соответствующий аспект внешнего вида переопределяются заказным дизайном.<br/>Это признак доступен только для чтения.<br/>|
|offline_mail_settings|True|OfflineMailSettings|Настройки офлайн почты.<br/>|
|callback_url|False|string|Настройка Callback URL.<br/>|
|created_at|True|datetime|Дата создания.<br/>|
