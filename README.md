# Library app
Allows get the list of books (uploaded from .csv file) and opinions (also uploaded from .csv) for specific book.
There are two endpoint available:

## List of books
- /api/books

## Book detail with opinions
- /api/books/<str:title>


The application is contenerized and it uses Makefile to handle commands in a nice way.

## To start app
 
     make run
 
## To create migrations
 
     make migrations
 
## To create superuser
 
     make superuser
 
## To run tests

     make test


Books and opinions have to be uploaded using management command.
They need to be saved in .csv file with proper format and column order, spearated by `;`.
Firstly books need to be uploaded, then opinions for books. 

## Book columns order 
- ISBN;Tytuł;Autor;Gatunek;

## Opinion columns order
- ISNB;Ocena;Opis;


## To upload books

    make populate_books args="--filename=books.csv"


- books.csv is .csv file name, placed in root folder.

## To upload opinions

    make populate_opinions args="--file=opinions.csv"


 - opinions.csv is .csv file name, placed in root folder.
