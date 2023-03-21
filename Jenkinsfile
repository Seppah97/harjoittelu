pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    environment {
        DB_ENGINE = 'sqlite'
    }

    stages {
        stage('Test') {
            steps {
                echo "Database engine is ${DB_ENGINE}"
                sh 'pytest'

            }
        }

        stage('Deployment') {
            steps {
                sh 'echo Tämä on julkaisu'
            }
        }
    }
    
    post {
        
        always{
            echo 'Tämä on päättynyt'
        }
        
    }
}