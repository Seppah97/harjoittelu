pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    environment {
        DB_ENGINE = 'sqlite'
        SECRET_INPUT = credientals('testi_secret')
    }

    stages {
        stage('Test') {
            steps {
                echo SECRET_INPUT

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