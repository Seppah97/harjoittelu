pipeline {
    agent { docker { image 'mcr.microsoft.com/playwright:v1.31.0-focal' } }

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
                sh 'pip install playwright'
                sh 'playwright install --with-deps'
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