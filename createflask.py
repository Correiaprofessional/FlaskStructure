import os, platform


#
# Run on the folder for your Flask project
#

PATH, FILENAME = os.path.split(os.path.abspath(__file__))

#
# System Functions
#

def GetOpr():
        
    operS = platform.system()
    if operS == "Linux":
        return "L"
    if operS == "Windows":
        return "W"
    if operS == "Darwin":
        return "D"
    
OPRSYSTEM = GetOpr()
    
def RetBars():
        
    return "//" if OPRSYSTEM == "L" else "\\"

def CreateStructure():
    
    print("CREATING app/ FOLDER")
    os.mkdir(PATH + RetBars() + "app")
    print("app/ FOLDER CREATED")
    print("CREATING app/templates/ FOLDER")
    os.mkdir(PATH + RetBars() + "app" + RetBars() + "templates")
    print("app/templates FOLDER CREATED")
    print("CREATING app/templates/db/ FOLDER")
    os.mkdir(PATH + RetBars() + "app" + RetBars() + "templates" + RetBars() + "db")
    print("app/templates/db/ FOLDER CREATED")
    print("CREATING app/templates/admin/ FOLDER")
    os.mkdir(PATH + RetBars() + "app" + RetBars() + "templates" + RetBars() + "admin")
    print("app/templates/admin/ FOLDER CREATED")
    print("CREATING app/static/ FOLDER")
    os.mkdir(PATH + RetBars() + "app" + RetBars() + "static")
    print("app/static FOLDER CREATED")
    print("CREATING app/static/css/ FOLDER")
    os.mkdir(PATH + RetBars() + "app" + RetBars() + "static" + RetBars() + "css")
    print("app/static/css/ FOLDER CREATED")
    print("CREATING app/static/js FOLDER")
    os.mkdir(PATH + RetBars() + "app" + RetBars() + "static" + RetBars() + "js")
    print("app/static/js FOLDER CREATED")
    print("CREATING app/static/images/ FOLDER")
    os.mkdir(PATH + RetBars() + "app" + RetBars() + "static" + RetBars() + "images")
    print("app/static/images/ FOLDER CREATED")

def DeleteSelf():
    os.remove(PATH + RetBars() + "FlaskSt.py")

def DataFiles():
    
    print("====== CREATING PYTHON FILES =======")
    print("CREATING "+ PATH + RetBars() +"run.py")
    runFile = "from app import app \n\nif __name__ == '__main__':\n\tapp.run(debug=True)"
    CreateFile(PATH, "run.py", runFile)
    print(PATH + RetBars() +"run.py CREATED")
    
    print("CREATING "+ PATH + RetBars() +"\\app\views.py")
    runFile = "from app import app\n" 
    runFile += "from flask import render_template, request, jsonify, session, send_from_directory\n\n\n"
    runFile += "@app.route('/')\n"
    runFile += "def index():\n"
    runFile += "\treturn render_template('index.html')"
    CreateFile(PATH + RetBars() + "app" + RetBars(), "views.py", runFile)
    print(PATH + RetBars() +"\\app\\views.py CREATED")
    
    
    print("CREATING "+ PATH + RetBars() +"\\app\\__init__.py")
    runFile = "from flask import Flask\n" 
    runFile += "app = Flask(__name__)\n"
    runFile += "from app import views"
    CreateFile(PATH + RetBars() + "app" + RetBars(), "__init__.py", runFile)
    print(PATH + RetBars() +"app" +RetBars()+ "__init__.py CREATED")
    
    print("====== CREATING HTML FILES =======")
    
    print("CREATING "+ PATH + RetBars() +"\\app\\templates\\index.html")
    runFile = "<!DOCTYPE html>\n" 
    runFile += "<html lang='en'>\n"
    runFile += "<head>\n"
    runFile += "<meta charset='utf-8'>\n"
    runFile += "<meta name='viewport' content='width=device-width, initial-scale=1.0, shrink-to-fit=no'>\n"
    runFile += "<title>Flask Auto Structure</title>\n"
    runFile += "</head>\n"
    runFile += "<body>\n"
    runFile += "</body>\n"
    runFile += "<h6>The App is running</h6><br>"
    runFile += "</html>"
    CreateFile(PATH + RetBars() + "app" +RetBars()+ "templates" , "index.html", runFile)
    print(PATH + RetBars() +"\\templates\\index.html CREATED")
    
def CreateFile(stPath, stFileName, stData):
    
    f = open(stPath + RetBars() + stFileName, "w")
    f.writelines(stData)

def Main():
    CreateStructure()
    DataFiles()
    DeleteSelf()

if __name__ == "__main__":
    try:
        import flask
        Main()
    except:
        try:
            os.system("pip install flask")
            Main()
            
        except:
            os.system("pip3 install flask")
            Main()