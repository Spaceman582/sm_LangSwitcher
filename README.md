# sm_LangSwitcher

###ENG

WARNING, the plugin only works on WINDOWS!

Due to Maya's issue with supporting languages other than English, non-English-speaking users face the problem of constantly switching keyboard layouts even when it is not necessary. This plugin solves that problem.

When you select any Maya window, the plugin remembers your native language and automatically switches the layout to English.

When you select any other window, the script will switch back to the language you were using when selecting the Maya window. If you originally entered Maya using the English layout, the language will not switch.

The plugin has been tested on Maya 2022-2024, but it contains no components that would interfere with using older or newer versions.



###RUS

Внимание, плагин работает только на WINDOWS!

Из-за того, что в Maya есть проблема с поддержкой языков, кроме английского, у неанглоговорящих пользователей появляется проблема постоянного переключения языка даже тогда, когда это не нужно.
Данный плагин решает эту проблему. В случае, когда вы выбираете любое окно Maya, плагин запоминает ваш нативный язык и автоматически переключает раскладку на английский.
При выборе любого другого окна скрипт включает тот язык, с которым вы выбирали окно Maya. Если вы изначально заходили в Maya с английской раскладкой, язык переключаться не будет.
Плагин тестировался на Maya 2022–2024, но в нём нет компонентов, которые бы мешали работе на более старой или более новой версии.




###INSTALLATION

Drop the Python file into C:\Users\*USERNAME*\Documents\maya\plug-ins

or ~\maya\20xx\plug-ins

or any other plug-in path supported by your MAYA client.

In the Maya window, go to Windows menu --> Settings/Preferences/Plug-in manager, find sm_LangSwitcher.py, and run it. Afterward, a notification will appear in the console:



// LangAutoSwitch : Already started

This means the plugin is running and working properly.

If you encounter any errors, you can contact me at

LinkedIn or Telegram Аnd describe the problem. If I have enough information, I'll try to fix it.




###ERRORS

At the moment, an error has been identified where, if after starting Maya the home window remains open and the focus is switched to another window, Maya may freeze. The error is completely random and does not always occur, and currently it is not clear what causes it.




###Disclaimer
##ENG
Attention: the author is not responsible for the operability of Maya, loss of projects, or any other possible negative consequences. The code is provided for free, open source, and as-is. The decision to use the plugin in production is at your own risk.

###RUS
Внимание, автор не несёт ответственности за работоспособность Maya, потерю проектов и другие возможные негативные последствия. Код поставляется бесплатно, в открытом доступе и предоставляется в таком виде, в каком есть. Решение об использовании плагина в продакшене вы принимаете на свой страх и риск.
