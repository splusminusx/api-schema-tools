
## Site

### Описание типа
Сайт.<br/><br/>Контроллер: Sites.<br/>
### Поля

| Имя поля | Необходимость | Тип данных | Комментарий |
|---|---|---|---|
|*department_site_bindings*|False|Array.<[DepartmentSiteBinding](/types/DepartmentSiteBinding)>|Список связей сайта с отделами.<br/>|
|*is_lead*|True|[boolean](/types/boolean)|Включение/выключение функциональности генератора лидов.<br/>|
|*updated_at*|True|[datetime](/types/datetime)|Дата последнего обновления.<br/>|
|*offline_form_settings*|False|[OfflineFormSettings](/types/OfflineFormSettings)|Настройки офлайн формы.<br/>DEPRECATED!<br/>|
|*x_widget_settings*|True|[SiteXWidgetSettings](/types/SiteXWidgetSettings)|Настройки продукта «X-widget».<br/>|
|*is_site_prechats*|True|[boolean](/types/boolean)|Признак использования пречат-полей сайта.<br/>Если false, то будут использоваться пречаты из связей отделов с сайтом.<br/>|
|*id*|True|[numeric](/types/numeric)|ID сайта.<br/>|
|*call_label_settings*|True|[CallLabelSettings](/types/CallLabelSettings)|Настройки ярлыка звонка.<br/>DEPRECATED!<br/>|
|*prechats_chat*|False|Array.<[Prechat](/types/Prechat)>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|*is_comlaint*|True|[boolean](/types/boolean)|Включение/выключение жалоб.<br/>|
|*hold_rule*|False|[HoldRule](/types/HoldRule)|Сценарий удержания.<br/>|
|*is_mobile*|True|[boolean](/types/boolean)|Включение/выключение мобильного вида виджета.<br/>|
|*widget_settings*|True|[SiteWidgetSettings](/types/SiteWidgetSettings)|Настройки виджета.<br/>|
|*prechats_lead*|False|Array.<[Prechat](/types/Prechat)>|Массив пречат-полей.<br/>Максимум 2 элемента.<br/>|
|*complaint_email*|False|[email](/types/email)|Адрес электронной почты, на который будут отправляться нотификации о поступлении новой жалобы.<br/>|
|*is_hidden_offline*|True|[boolean](/types/boolean)|Скрывать ярлык, если сотрудники офлайн.<br/>|
|*is_vote*|True|[boolean](/types/boolean)|Включение/выключение функциональности оценки чата посетителем.<br/>|
|*chat_welcome_settings*|True|[ChatWelcomeSettings](/types/ChatWelcomeSettings)|Настройки окна приветствия.<br/>DEPRECATED!<br/>|
|*call_settings*|True|[SiteCallSettings](/types/SiteCallSettings)|Звонковые настройки сайта.<br/>|
|*chat_form_settings*|True|[ChatFormSettings](/types/ChatFormSettings)|Настройки ярлыка и окна чата.<br/>DEPRECATED!<br/>|
|*is_deleted*|True|[boolean](/types/boolean)|Признак удаленного объекта.<br/>|
|*url*|True|[string](/types/string)|Адрес сайта.<br/>|
|*is_callback*|True|[boolean](/types/boolean)|Включение/выключение функциональности «Перезвоните мне».<br/>|
|*employees*|False|Array.<[Employee](/types/Employee)>|Список сотрудников, связанных с данным сайтом.<br/>|
|*lead_form_settings*|False|[LeadFormSettings](/types/LeadFormSettings)|Настройки формы генератора лидов.<br/>DEPRECATED!<br/>|
|*is_managed*|True|[boolean](/types/boolean)|True, если сайт входит в число своих сайтов сотрудника, вызывающего метод.<br/>Это признак доступен только для чтения.<br/>|
|*is_custom_buttons*|True|[boolean](/types/boolean)|Признак заказного дизайна кнопок.<br/>Если true, то изменение некоторых визуальных настроек кнопок чата и звонка может не иметь должного результата, поскольку соответствующий аспект внешнего вида переопределяются заказным дизайном.<br/>Это признак доступен только для чтения.<br/>|
|*offline_mail_settings*|True|[OfflineMailSettings](/types/OfflineMailSettings)|Настройки офлайн почты.<br/>|
|*callback_url*|False|[string](/types/string)|Настройка Callback URL.<br/>|
|*created_at*|True|[datetime](/types/datetime)|Дата создания.<br/>|
