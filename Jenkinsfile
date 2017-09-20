node {
    def pythonHome = tool "python3"
    stage('Checkout') {
       checkout scm
    }
    stage('Preparation') { // for display purposes
       echo "Hello Preparation"
       bat "${pythonHome}/python --version"
    }
    stage('Test') {
       echo "Hello Test"
       bat "${pythonHome}/python -m unittest discover test"
    }
    stage('Run') {
       echo "Hello Run"
       bat "${pythonHome}/python oopython/oopython.py"
    }
 }
