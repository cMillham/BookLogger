from flask import Flask, render_template, redirect, request
import mysql.connector

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    #may need to be BookLog.html
    #to start local host server, run python3 -m http.server in terminal and navigate to that port
    name = "BookLog"
    #testing = "testing"
    #create connection between server and database
    db_connection = mysql.connector.connect(
        host="chloedb.cniykaq6ec80.us-east-1.rds.amazonaws.com",
        user="admin",
        passwd="chloe001",
        database="ChloesBookLogDB"
    )
    #Pulling a query
    mycursor = db_connection.cursor()
    mycursor.execute("select * from tblBook")
    myresult = mycursor.fetchall()
    testing = myresult
    # for x in myresult:
    #     testing = x
    #testing = myresult[0]
    return render_template('BookLog.html', name = name, testing = testing)

@app.route('/post', methods=['POST'])
def post():
    if(request.method == 'POST'):
        information = request.form
        #save form data into database
        db_connection = mysql.connector.connect(
            host="chloedb.cniykaq6ec80.us-east-1.rds.amazonaws.com",
            user="admin",
            passwd="chloe001",
            database="ChloesBookLogDB"
        )
        #Pulling a query
        mycursor = db_connection.cursor()
        mycursor.execute("insert into tblBook(fkAuthorID, title, review) values(1,'" + information["title"] + "', '" + information["review"] + "')")
        db_connection.commit()
    return redirect('/')

@app.route('/addbook', methods=['POST'])
def addbook():
    return render_template('addBookForm.html')

@app.route('/viewbook', methods=['GET'])
def viewbook():
    db_connection = mysql.connector.connect(
        host="chloedb.cniykaq6ec80.us-east-1.rds.amazonaws.com",
        user="admin",
        passwd="chloe001",
        database="ChloesBookLogDB"
    )
        #Pulling a query
    mycursor = db_connection.cursor()
    mycursor.execute("select * from tblBook where pkBookID=" + request.args.get('bookid'))
    myresult = mycursor.fetchall()
    bookDetails = myresult
    return render_template('viewBook.html', bookDetails = bookDetails)

#method definition for button routing to new page
# def gotoAddBook():
#     return redirect('/addbook')

if __name__ == "__main__":
    app.run(debug=True)


