# Csl2Pdf

**MOVED TO:** [https://github.com/EliseyP/HymnographyCSL](https://github.com/EliseyP/HymnographyCSL)

`LibreOffice` расширение для быстрой компиляции открытого документа с помощью инструмента  
[https://github.com/EliseyP/csl_odt2tex](https://github.com/EliseyP/csl_odt2tex) 


При первом запуске будет предложен диалог выбора каталога, в котором находится скрипт `csl2tex.py`.  
В дальнейшем это значение хранится в `user-config` каталоге в файле `csl2pdf.rc`.  
Для Linux: `~/.config/libreoffice/4/user/csl2pdf.rc`

`Pdf`-файл (а также промежуточный `.tex` файл) сохраняется в том же каталоге, что и открытый документ. Имя файла, если не изменено в диалоге, совпадает с именем открытого `odt`-документа (без расширения).  

### Toolbar:  
![Диалог](/src/Images/Csl2Pdf_gui_26.png) - запуск диалога.  
![Цветной](/src/Images/Csl2Pdf_red_26.png) - тихий запуск (цветной PDF).  
![Черно-белый](/src/Images/Csl2Pdf_26.png) - тихий запуск (черно-белый PDF).
