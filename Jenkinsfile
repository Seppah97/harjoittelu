pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Test') {
            steps {
                sh 'echo Tämä on testivaihe'
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