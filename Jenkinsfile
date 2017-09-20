node {
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
       bat "python -m unittest discover test"
    }
    stage('Results') {
       echo "Hello Result"
    }
    stage('Run') {
       echo "Hello Run"
       bat "python oopython/oopython.py"
    }
 }
