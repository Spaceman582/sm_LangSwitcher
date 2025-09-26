# sm_LangSwitcher

<img width="200" height="200" alt="LangSwitch" src="https://github.com/user-attachments/assets/0af24fcc-fead-4d58-8d3a-20834920487e" />

---

## ENG

⚠️ **WARNING**: The plugin only works on **WINDOWS**!

Due to Maya's issue with supporting languages other than English, non-English-speaking users face the problem of constantly switching keyboard layouts even when it is not necessary. This plugin solves that problem.

When you select any Maya window, the plugin remembers your native language and automatically switches the layout to English.

When you select any other window, the script will switch back to the language you were using when selecting the Maya window. If you originally entered Maya using the English layout, the language will not switch.

The plugin has been tested on Maya 2022-2024, but it contains no components that would interfere with using older or newer versions.

---

## INSTALLATION

1. Drop the Python file into one of the following paths:  
   - `C:\Users\<USERNAME>\Documents\maya\plug-ins`  
   - `~\maya\20xx\plug-ins`  
   - Or any other plug-in path supported by your MAYA client.

2. In the Maya window, go to **Windows menu → Settings/Preferences → Plug-in manager**, find `sm_LangSwitcher.py`, and run it.  

Afterward, a notification will appear in the console:  
// LangAutoSwitch : Already started


This means the plugin is running and working properly.

---

## ERRORS

At the moment, an error has been identified where, if after starting Maya the home window remains open and the focus is switched to another window, Maya may freeze. The error is completely random and does not always occur, and currently it is not clear what causes it.

---

## Disclaimer

The author is not responsible for the operability of Maya, loss of projects, or any other possible negative consequences. The code is provided for free, open source, and as-is. The decision to use the plugin in production is at your own risk.
---

## SUPPORTED LANGUAGES
 - **All Windows language packages***
---

## RUS

⚠️ **Внимание**: Плагин работает только на **WINDOWS**!

Из-за того, что в Maya есть проблема с поддержкой языков, кроме английского, у неанглоговорящих пользователей появляется проблема постоянного переключения языка даже тогда, когда это не нужно. Данный плагин решает эту проблему.

В случае, когда вы выбираете любое окно Maya, плагин запоминает ваш нативный язык и автоматически переключает раскладку на английский.

При выборе любого другого окна скрипт включает тот язык, с которым вы выбирали окно Maya. Если вы изначально заходили в Maya с английской раскладкой, язык переключаться не будет.

Тестировался на Maya 2022–2024, но совместим с другими версиями, так как не содержит конфликтующих компонентов.

---

## Установка

1. Скопируйте файл `sm_LangSwitcher.py` в одну из папок:
   - `C:\Users\<USERNAME>\Documents\maya\plug-ins`
   - `~\maya\20xx\plug-ins`
   - Или любую другую папку для плагинов Maya.
2. В Maya откройте меню **Windows → Settings/Preferences → Plug-in Manager**.
3. Найдите `sm_LangSwitcher.py`, отметьте **Load** или **Auto Load**.
4. После запуска в консоли появится сообщение:
// LangAutoSwitch : Already started

Это подтверждает, что плагин успешно работает.

---

## Известные ошибки

При переключении фокуса на другое окно, если главное окно Maya остается открытым, Maya может зависнуть. Ошибка возникает случайно, причина пока неизвестна.

---

## Отказ от ответственности

Автор не несет ответственности за сбои в работе Maya, потерю данных или другие негативные последствия. Код предоставляется бесплатно, с открытым исходным кодом и "как есть". Использование плагина в продакшене на ваш риск.
---

## Поддерживаемые языки
- **Все языковые пакеты Windows**
---

*License*: [MIT License](https://github.com/Spaceman582/sm_LangSwitcher/blob/main/LICENSE)
