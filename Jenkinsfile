node {
    def pythonHome = tool "python3"
    stage('checkout') {
       checkout scm
    }
    stage('Preparation') { // for display purposes
       echo "Hello Preparation"
    }
    stage('Build') {
       echo "Hello Build"
    }
    stage('Test') {
       echo "Hello Test"
       bat "${pythonHome}/python -m unittest discover test"
    }
    stage('Results') {
       echo "Hello Result"
    }
    stage('Run') {
       echo "Hello Run"
       bat "${pythonHome}/python oopython/oopython.py"
    }
 }
