pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    environment {
        DB_ENGINE = 'sqlite'
        SECRET_INPUT = credentials('testi_secret')
    }

    stages {
        stage('Test') {
            steps {
                echo SECRET_INPUT
                
                sh './test.sh'
            }
        }

        stage('Deployment') {
            steps {
                sh 'echo Tämä on julkaisu'
                input('Tämä on testi-inputti')
            }
        }
    }
    
    post {
        
        always{
            echo 'Tämä on päättynyt'
        }
        
    }
}