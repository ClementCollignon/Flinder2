/*Copyright (c) DevSec Studio. All rights reserved.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

/*-----QWidget-----*/
QWidget
{
	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(27, 39, 50, 255),stop:1 rgba(47, 53, 74, 255));
	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(69,78,94, 255),stop:1 rgba(47, 53, 74, 255));
	background-color: #454e5e;
	background-color: #474B6B;
	color: #000000;

}

/*---- QStatusBar ----*/
QStatusBar
{
    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(27, 39, 50, 255),stop:1 rgba(47, 53, 74, 255));
}

/*----QTextEdit----*/
QTextEdit
{
    background-color: transparent;
    color: #c2c7d5;
    font-size: 30px;
}

/*-----QLabel-----*/
QLabel
{
	background-color: transparent;
	color: #c2c7d5;
	color: #FEFEFD;
	font-size: 30px;

}

/*-----QLabel-----*/
QGraphicsView
{
	background-color: transparent;
    border: 1px solid #F4F1DE;

}


/*-----QToolButton-----*/
QToolButton
{
	background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:1, y2:0.511, stop:0 rgba(0, 172, 149, 255),stop:0.995192 rgba(54, 197, 177, 255));
	background-color: rgba(0, 172, 149, 255);
	background-color: transparent;
	color: #FEFEFD;
	font-size: 24px;
	font-weight: bold;
	border: 3px solid #81B29A;
	border-radius: 0px;
	padding: 16px;

}


QToolButton::pressed
{
	background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:1, y2:0.511, stop:0 rgba(0, 207, 179, 255),stop:1 rgba(70, 255, 230, 255));
    background-color: #81B29A;
}

QToolButton::hover
{
    border: 6px solid #81B29A;
    
}

/*-----QPushButton-----*/
QPushButton
{
	background-color: transparent;
	color: #FEFEFD;
	font-size: 26px;
	font-weight: bold;
	border: 3px solid #81B29A;
	border-radius: 0px;
	padding: 20px;

}


QPushButton::pressed
{
    background-color: #81B29A;
}


QPushButton::hover
{
    border: 6px solid #81B29A;
    
}

/*-----QCheckBox-----*/
QCheckBox
{
	background-color: transparent;
	color: #fff;
	color: #FEFEFD;
	font-size: 30px;
	font-weight: bold;
	border: none;
	border-radius: 10px;

}


/*-----QCheckBox-----*/
QCheckBox::indicator
{
    color: #b1b1b1;
    background-color: #323232;
    border: 2px solid darkgray;
    width: 40px;
    height: 40px;

}


QCheckBox::indicator:checked
{
    image:url("./ressources/check.png");
	background-color: #E07A5F;
	background-color: #81B29A;
    border: 2px solid #607cff;
    border: 2px solid #E07A5F;

}


QCheckBox::indicator:unchecked:hover
{
    border: 2px solid #81B29A;

}


QCheckBox::disabled
{
	color: #656565;

}


QCheckBox::indicator:disabled
{
	background-color: #656565;
	color: #656565;
    border: 2px solid #656565;

}


/*-----QLineEdit-----*/
QLineEdit
{
	background-color: #c2c7d5;
	color: #000;
	font-weight: bold;
	border: none;
	border-radius: 4px;
	padding: 6px;
	font-size: 30px;
}


/*-----QListView-----*/
QListView
{
	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(50, 61, 80, 255),stop:1 rgba(44, 49, 69, 255));
	background-color: #3D405B;
	color: #fff;
	font-size: 40px;
	font-weight: bold;
	border: 2px solid #191919;
	border: 0px solid #191919;
	show-decoration-selected: 0;

}


QListView::item
{
	color: #31cecb;
	color: #F4F1DE;
	background-color: #454e5e;
	border: none;
	padding: 10px;
	border-radius: 0px;
    height: 180px;
	padding-left : 20px;
	

}

QListView::item:selected
{
	color: #31cecb;
	color: #E07A5F;
	background-color: #474B6B;

}


QListView::item:!selected
{
	color:white;
	background-color: transparent;
	border: none;
	padding-left : 20px;

}


QListView::item:!selected:hover
{
	color: #bbbcba;
	background-color: #52567A;
	
	border: none;
	padding-left : 20px;

}


/*-----QTreeView-----*/
QTreeView 
{
	background-color: #232939;
	show-decoration-selected: 0;
	color: #c2c8d7;

}


QTreeView::item 
{
	border-top-color: transparent;
	border-bottom-color: transparent;

}


QTreeView::item:hover 
{
	background-color: #606060;
	color: #fff;

}


QTreeView::item:selected 
{
	background-color: #0ab19a;
	color: #fff;

}


QTreeView::item:selected:active
{
	background-color: #0ab19a;
	color: #fff;

}


QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings 
{
	image: url(://tree-closed.png);

}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings  
{
	image: url(://tree-open.png);

}


/*-----QTableView & QTableWidget-----*/
QTableView
{
    background-color: #232939;
	border: 2px solid gray;
    color: #f0f0f0;
    gridline-color: #232939;
    outline : 0;

}


QTableView::disabled
{
    background-color: #242526;
    border: 2px solid #32414B;
    color: #656565;
    gridline-color: #656565;
    outline : 0;

}


QTableView::item:hover 
{
    background-color: #606060;
    color: #f0f0f0;

}


QTableView::item:selected 
{
	background-color: #0ab19a;
    color: #F0F0F0;

}


QTableView::item:selected:disabled
{
    background-color: #1a1b1c;
    border: 4px solid #525251;
    color: #656565;

}


QTableCornerButton::section
{
	background-color: #343a49;
    color: #fff;

}


QHeaderView::section
{
	color: #fff;
	border-top: 0px;
	border-bottom: 2px solid gray;
	border-right: 2px solid gray;
	background-color: #343a49;
    margin-top:2px;
	margin-bottom:2px;
	padding: 10px;

}


QHeaderView::section:disabled
{
    background-color: #525251;
    color: #656565;

}


QHeaderView::section:checked
{
    color: #fff;
    background-color: #0ab19a;

}


QHeaderView::section:checked:disabled
{
    color: #656565;
    background-color: #525251;

}


QHeaderView::section::vertical::first,
QHeaderView::section::vertical::only-one
{
    border-top: 2px solid #353635;

}


QHeaderView::section::vertical
{
    border-top: 2px solid #353635;

}


QHeaderView::section::horizontal::first,
QHeaderView::section::horizontal::only-one
{
    border-left: 2px solid #353635;

}


QHeaderView::section::horizontal
{
    border-left: 2px solid #353635;

}


/*-----QScrollBar-----*/
QScrollBar:horizontal 
{
    background-color: transparent;
    height: 16px;
    margin: 0px;
    padding: 0px;

}


QScrollBar::handle:horizontal 
{
    border: none;
	min-width: 200px;
    background-color: #56576c;

}


QScrollBar::add-line:horizontal, 
QScrollBar::sub-line:horizontal,
QScrollBar::add-page:horizontal, 
QScrollBar::sub-page:horizontal 
{
    width: 0px;
    background-color: transparent;

}


QScrollBar:vertical 
{
    background-color: transparent;
    width: 16px;
    margin: 0;

}


QScrollBar::handle:vertical 
{
    border: none;
	min-height: 200px;
    background-color: #56576c;

}


QScrollBar::add-line:vertical, 
QScrollBar::sub-line:vertical,
QScrollBar::add-page:vertical, 
QScrollBar::sub-page:vertical 
{
    height: 0px;
    background-color: transparent;

}


